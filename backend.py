import os
from typing import List, Tuple, Dict, Any
from pathlib import Path
import tempfile
import logging
from dataclasses import dataclass
from typing_extensions import TypedDict

import PyPDF2
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document
from langgraph.graph import StateGraph, END

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GraphState(TypedDict):
    """State for the RAG agent graph."""
    query: str
    context: List[Document]
    response: str
    citations: List[str]

@dataclass
class PDFDocument:
    """Represents a processed PDF document."""
    filename: str
    page_numbers: List[int]
    content: str

class PDFRAGAgent:
    def __init__(self):
        """Initialize the PDF RAG Agent with necessary components."""
        self.embeddings = OpenAIEmbeddings()
        self.llm = ChatOpenAI(temperature=0)
        self.vector_store = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.processed_docs: List[PDFDocument] = []
        self._initialize_graph()

    def _initialize_graph(self):
        """Initialize the LangGraph workflow."""
        self.workflow = StateGraph(GraphState)
        self.workflow.add_node("retrieve", self._retrieve_context)
        self.workflow.add_node("generate", self._generate_response)
        self.workflow.add_edge("retrieve", "generate")
        self.workflow.add_edge("generate", END)
        self.graph = self.workflow.compile()

    def process_pdf(self, pdf_file) -> None:
        """Process a PDF file and store its embeddings."""
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(pdf_file.read())
                tmp_path = tmp_file.name

            loader = PyPDFLoader(tmp_path)
            pages = loader.load()
            chunks = self.text_splitter.split_documents(pages)
            pdf_doc = PDFDocument(
                filename=pdf_file.name,
                page_numbers=list(range(len(pages))),
                content="\n".join([chunk.page_content for chunk in chunks])
            )
            self.processed_docs.append(pdf_doc)

            if self.vector_store is None:
                self.vector_store = Chroma.from_documents(
                    documents=chunks,
                    embedding=self.embeddings
                )
            else:
                self.vector_store.add_documents(chunks)

            os.unlink(tmp_path)
        except Exception as e:
            logger.error(f"Error processing PDF {pdf_file.name}: {str(e)}")
            raise

    def _retrieve_context(self, state: GraphState) -> dict:
        """Retrieve relevant context for the query."""
        if not self.vector_store:
            return {"context": [], "query": state["query"]}
        docs = self.vector_store.similarity_search(
            state["query"],
            k=3
        )
        return {"context": docs, "query": state["query"]}

    def _generate_response(self, state: GraphState) -> dict:
        """Generate a response using retrieved context."""
        if not state["context"]:
            return {
                "response": "No relevant information found in the uploaded documents.",
                "citations": []
            }
        context = "\n\n".join([doc.page_content for doc in state["context"]])
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant that answers questions based on the provided context. Include specific citations from the source documents in your response."),
            ("human", "Context:\n{context}\n\nQuestion: {question}")
        ])
        messages = prompt.format_messages(context=context, question=state["query"])
        response = self.llm.invoke(messages)
        citations = [
            f"Document: {doc.metadata.get('source', 'Unknown')}, Page: {doc.metadata.get('page', 'Unknown')}"
            for doc in state["context"]
        ]
        return {
            "response": response.content,
            "citations": citations
        }

    def query(self, question: str) -> Tuple[str, List[str]]:
        """Process a query through the RAG workflow."""
        try:
            state = {"query": question}
            result = self.graph.invoke(state)
            return result["response"], result["citations"]
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return "An error occurred while processing your query.", []
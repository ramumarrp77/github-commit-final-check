import os
from typing import Dict, List, TypedDict
from pathlib import Path
import tempfile

import PyPDF2
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph, END

class RAGState(TypedDict):
    """State for the RAG agent."""
    query: str
    context: List[Document]
    response: str
    sources: List[Dict]

class PDFRAGAgent:
    def __init__(self, api_key: str):
        """Initialize the PDF RAG Agent with OpenAI API key."""
        os.environ["OPENAI_API_KEY"] = api_key
        
        self.embeddings = OpenAIEmbeddings()
        self.llm = ChatOpenAI(temperature=0)
        self.vector_store = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        
        # Initialize the graph
        self.graph = self._create_graph()
        
    def _create_graph(self) -> StateGraph:
        """Create the RAG workflow graph."""
        workflow = StateGraph(RAGState)
        
        # Add nodes
        workflow.add_node("retrieve", self._retrieve_context)
        workflow.add_node("generate", self._generate_response)
        
        # Add edges
        workflow.add_edge("retrieve", "generate")
        workflow.add_edge("generate", END)
        
        return workflow.compile()
    
    def _retrieve_context(self, state: RAGState) -> RAGState:
        """Retrieve relevant context from the vector store."""
        if not self.vector_store:
            return {
                **state,
                "context": [],
                "sources": []
            }
        
        results = self.vector_store.similarity_search_with_score(
            state["query"],
            k=3
        )
        documents = [doc for doc, _ in results]
        return {
            **state,
            "context": documents
        }
    
    def _generate_response(self, state: RAGState) -> RAGState:
        """Generate a response using the retrieved context."""
        if not state["context"]:
            return {
                **state,
                "response": "No relevant information found in the uploaded documents.",
                "sources": []
            }
        
        # Create prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant that answers questions based on the provided context. "
                      "Always be truthful and if you're not sure about something, say so."),
            ("user", "Context:\n{context}\n\nQuestion: {question}")
        ])
        
        # Create chain
        chain = prompt | self.llm | StrOutputParser()
        
        # Prepare context and generate response
        context_str = "\n".join(doc.page_content for doc in state["context"])
        response = chain.invoke({
            "context": context_str,
            "question": state["query"]
        })
        
        # Prepare sources
        sources = []
        for doc in state["context"]:
            sources.append({
                "file": doc.metadata.get("source", "Unknown"),
                "page": doc.metadata.get("page", 0),
                "text": doc.page_content[:200] + "..."
            })
        
        return {
            **state,
            "response": response,
            "sources": sources
        }
    
    def process_pdf(self, pdf_file) -> None:
        """Process a PDF file and add it to the vector store."""
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(pdf_file.read())
            tmp_path = tmp_file.name
        
        try:
            # Load PDF
            loader = PyPDFLoader(tmp_path)
            pages = loader.load()
            
            # Add source filename to metadata
            for page in pages:
                page.metadata["source"] = pdf_file.name
            
            # Split into chunks
            chunks = self.text_splitter.split_documents(pages)
            
            # Initialize or update vector store
            if self.vector_store is None:
                self.vector_store = Chroma.from_documents(
                    documents=chunks,
                    embedding=self.embeddings
                )
            else:
                self.vector_store.add_documents(chunks)
                
        finally:
            # Clean up temporary file
            os.unlink(tmp_path)
    
    def get_response(self, query: str) -> Dict:
        """Get a response for a query using the RAG workflow."""
        # Initialize state
        initial_state = {
            "query": query,
            "context": [],
            "response": "",
            "sources": []
        }
        
        # Run the graph
        final_state = self.graph.invoke(initial_state)
        
        return {
            "answer": final_state["response"],
            "sources": final_state["sources"]
        }
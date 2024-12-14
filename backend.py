import os
from typing import Dict, List, TypedDict, Optional
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor
import chromadb

class AgentState(TypedDict):
    query: str
    documents: Optional[List[Document]]
    response: Optional[str]
    error: Optional[str]


def create_retrieval_node():
    def retrieve_documents(state: AgentState) -> AgentState:
        try:
            vectorstore = Chroma(
                collection_name="pdf_collection",
                embedding_function=OpenAIEmbeddings()
            )
            docs = vectorstore.similarity_search(state["query"], k=3)
            return {"documents": docs, "query": state["query"]}
        except Exception as e:
            return {"error": f"Retrieval error: {str(e)}", "query": state["query"]}
    return retrieve_documents


def create_generation_node():
    def generate_response(state: AgentState) -> AgentState:
        try:
            if state.get("error"):
                return state
                
            llm = ChatOpenAI(temperature=0)
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant that provides information based on the given documents. Always cite sources with file names and page numbers."),
                ("user", "Answer the following question using the provided documents:\nQuestion: {query}\nDocuments: {documents}\nRemember to cite sources.")
            ])
            
            chain = prompt | llm
            response = chain.invoke({
                "query": state["query"],
                "documents": "\n".join([f"From {doc.metadata.get('source', 'unknown')}, page {doc.metadata.get('page', 'unknown')}: {doc.page_content}" for doc in state["documents"]])
            })
            
            return {
                "query": state["query"],
                "documents": state["documents"],
                "response": response.content
            }
        except Exception as e:
            return {"error": f"Generation error: {str(e)}", "query": state["query"]}
    return generate_response


class PDFAgent:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        
    def process_pdf(self, file_path: str) -> bool:
        try:
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            
            # Add source metadata
            for doc in documents:
                doc.metadata["source"] = os.path.basename(file_path)
            
            splits = self.text_splitter.split_documents(documents)
            
            vectorstore = Chroma(
                collection_name="pdf_collection",
                embedding_function=OpenAIEmbeddings()
            )
            vectorstore.add_documents(splits)
            return True
        except Exception as e:
            print(f"Error processing PDF: {str(e)}")
            return False
            
    def create_agent_graph(self) -> StateGraph:
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("retrieve", create_retrieval_node())
        workflow.add_node("generate", create_generation_node())
        
        # Add edges
        workflow.set_entry_point("retrieve")
        workflow.add_edge("retrieve", "generate")
        workflow.add_edge("generate", END)
        
        return workflow.compile()
    
    def query(self, question: str) -> Dict:
        graph = self.create_agent_graph()
        result = graph.invoke({"query": question})
        
        if result.get("error"):
            return {"success": False, "error": result["error"]}
        
        return {
            "success": True,
            "response": result["response"],
            "sources": [
                {
                    "file": doc.metadata.get("source", "unknown"),
                    "page": doc.metadata.get("page", "unknown")
                }
                for doc in result["documents"]
            ]
        }
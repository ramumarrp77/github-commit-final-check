import os
import PyPDF2
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Initialize global variables
embeddings_store = None
vector_store = None

# Define the state schema for LangGraph
class GraphState:
    def __init__(self, question: str, generation: str, documents: list):
        self.question = question
        self.generation = generation
        self.documents = documents

# Load PDF function
def load_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text() + '\n'
    return text

# Generate embeddings function
def generate_embeddings(pdf_text):
    global embeddings_store, vector_store
    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings()  # Ensure OpenAI API Key is set in environment
    # Generate embeddings
    embedding_vector = embeddings.embed_documents([pdf_text])
    # Store embeddings locally using Chroma
    vector_store = Chroma.from_embeddings(embedding_vector)
    embeddings_store = embeddings

# Search documents function
def search_documents(query):
    global vector_store
    if vector_store is None:
        raise ValueError('Embeddings not generated yet.')
    # Perform semantic search
    results = vector_store.similarity_search(query)
    return results

# Generate response function
def generate_response(query):
    global vector_store
    if vector_store is None:
        raise ValueError('Embeddings not generated yet.')
    # Create a RetrievalQA chain
    llm = OpenAI()  # Ensure OpenAI API Key is set in environment
    qa_chain = RetrievalQA(llm=llm, retriever=vector_store.as_retriever())
    response = qa_chain.run(query)
    return response
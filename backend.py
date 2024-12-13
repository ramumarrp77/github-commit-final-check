import os
import PyPDF2
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Initialize global variables
embeddings = OpenAIEmbeddings()
vectorstore = None

# Load PDF and extract text

def load_pdf(uploaded_file):
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + '\n'
        return text
    except Exception as e:
        raise ValueError(f"Failed to load PDF: {e}")

# Generate embeddings and store them locally

def generate_embeddings(uploaded_file):
    global vectorstore
    pdf_text = load_pdf(uploaded_file)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    doc_splits = text_splitter.split_text(pdf_text)
    vectorstore = Chroma.from_texts(doc_splits, embeddings)
    return vectorstore

# Search documents using semantic search

def search_documents(query):
    if vectorstore is None:
        return []
    results = vectorstore.similarity_search(query)
    return results

# Generate response using retrieved documents

def generate_response(query):
    if vectorstore is None:
        return "No documents available. Please upload a PDF and generate embeddings first."
    retriever = vectorstore.as_retriever()
    llm = OpenAI(temperature=0)
    qa_chain = RetrievalQA(llm=llm, retriever=retriever)
    response = qa_chain.run(query)
    return response
import os
import PyPDF2
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Initialize global variables
embeddings_store = Chroma(collection_name="pdf_embeddings")


def load_pdf(uploaded_file):
    """
    Load a PDF file and extract its text.
    
    Args:
        uploaded_file: The PDF file to load.
    
    Returns:
        str: The extracted text from the PDF.
    """
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + '\n'
    return text


def generate_embeddings(pdf_text):
    """
    Generate embeddings for the given PDF text and store them locally.
    
    Args:
        pdf_text (str): The text extracted from the PDF.
    """
    embeddings = OpenAIEmbeddings().embed_documents([pdf_text])
    embeddings_store.add_documents([pdf_text], embeddings)


def search_documents(query):
    """
    Search for relevant documents based on the query.
    
    Args:
        query (str): The search query.
    
    Returns:
        list: A list of relevant documents.
    """
    results = embeddings_store.similarity_search(query)
    return results


def generate_response(query):
    """
    Generate a response based on the query and retrieved documents.
    
    Args:
        query (str): The search query.
    
    Returns:
        str: The generated response.
    """
    retriever = embeddings_store.as_retriever()
    llm = OpenAI(temperature=0)
    qa_chain = RetrievalQA(llm=llm, retriever=retriever)
    response = qa_chain.run(query)
    return response
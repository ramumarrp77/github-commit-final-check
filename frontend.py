import streamlit as st
import os
from backend import load_pdf, generate_embeddings, search_documents, generate_response

# Streamlit UI
st.title("LangGraph PDF-Based RAG Agent")

# Sidebar for OpenAI API Key
api_key = st.sidebar.text_input("Enter your OpenAI API Key:")

# PDF Upload
uploaded_files = st.file_uploader("Upload PDF files", type=['pdf'], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            # Load PDF
            pdf_text = load_pdf(uploaded_file)
            st.write(f"Loaded {uploaded_file.name}")
            st.text_area("PDF Content", pdf_text, height=300)
        except Exception as e:
            st.error(f"Error loading {uploaded_file.name}: {e}")

# Generate Embeddings
if st.button("Generate Embeddings"):
    if uploaded_files:
        for uploaded_file in uploaded_files:
            try:
                embeddings = generate_embeddings(uploaded_file)
                st.success(f"Embeddings generated for {uploaded_file.name}")
            except Exception as e:
                st.error(f"Error generating embeddings for {uploaded_file.name}: {e}")
    else:
        st.warning("Please upload a PDF first.")

# Search Query
query = st.text_input("Enter your search query:")
if st.button("Search"):
    if query:
        try:
            results = search_documents(query)
            st.write("Search Results:")
            for result in results:
                st.write(result)
        except Exception as e:
            st.error(f"Error searching documents: {e}")
    else:
        st.warning("Please enter a query to search.")

# Generate Response
if st.button("Generate Response"):
    if query:
        try:
            response = generate_response(query)
            st.write("Response:")
            st.write(response)
        except Exception as e:
            st.error(f"Error generating response: {e}")
    else:
        st.warning("Please enter a query to generate a response.")
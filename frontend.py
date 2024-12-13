import streamlit as st
import os
from backend import load_pdf, generate_embeddings, search_documents, generate_response

# Sidebar for OpenAI API Key
st.sidebar.header('Configuration')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# PDF Upload
st.title('LangGraph PDF-Based RAG Agent')
uploaded_files = st.file_uploader('Upload PDF files', type='pdf', accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Load PDF
        pdf_text = load_pdf(uploaded_file)
        st.write(f'Loaded {uploaded_file.name}')
        st.text_area('PDF Content', pdf_text, height=300)

        # Generate embeddings
        if st.button('Generate Embeddings'):
            embeddings = generate_embeddings(pdf_text)
            st.success('Embeddings generated and stored locally.')

# Query Input
query = st.text_input('Enter your query:')

if st.button('Search'):
    if query:
        results = search_documents(query)
        st.write('### Search Results:')
        for result in results:
            st.write(result)

# Generate Response
if st.button('Generate Response'):
    if query:
        response = generate_response(query)
        st.write('### Response:')
        st.write(response)
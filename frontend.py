import streamlit as st
import tempfile
import os
from backend import PDFAgent

st.set_page_config(page_title="PDF RAG Agent", layout="wide")

# Initialize session state
if "pdf_agent" not in st.session_state:
    st.session_state.pdf_agent = None
if "processed_files" not in st.session_state:
    st.session_state.processed_files = set()

# Sidebar for OpenAI API Key
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    st.caption("Enter your OpenAI API key to enable the agent.")
    
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
        if st.session_state.pdf_agent is None:
            st.session_state.pdf_agent = PDFAgent()

# Main content
st.title("📚 PDF RAG Agent")

# File uploader
uploaded_files = st.file_uploader(
    "Upload PDF documents",
    type="pdf",
    accept_multiple_files=True
)

# Process uploaded files
if uploaded_files and openai_api_key:
    for uploaded_file in uploaded_files:
        if uploaded_file.name not in st.session_state.processed_files:
            with st.spinner(f"Processing {uploaded_file.name}..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    tmp_file_path = tmp_file.name
                
                if st.session_state.pdf_agent.process_pdf(tmp_file_path):
                    st.session_state.processed_files.add(uploaded_file.name)
                    st.success(f"Successfully processed {uploaded_file.name}")
                else:
                    st.error(f"Failed to process {uploaded_file.name}")
                
                os.unlink(tmp_file_path)

# Query interface
if st.session_state.processed_files:
    st.write("### Ask Questions")
    query = st.text_input("Enter your question about the uploaded documents")
    
    if query and st.session_state.pdf_agent:
        with st.spinner("Generating response..."):
            result = st.session_state.pdf_agent.query(query)
            
            if result["success"]:
                st.write("#### Answer")
                st.write(result["response"])
                
                st.write("#### Sources")
                for source in result["sources"]:
                    st.caption(f"📄 {source['file']} - Page {source['page']}")
            else:
                st.error(result["error"])
elif openai_api_key:
    st.info("Please upload some PDF documents to get started.")
else:
    st.warning("Please enter your OpenAI API key in the sidebar to get started.")
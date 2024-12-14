import streamlit as st
from backend import PDFRAGAgent
import os

st.set_page_config(page_title="PDF RAG Agent", layout="wide")

# Initialize session state
if "rag_agent" not in st.session_state:
    st.session_state.rag_agent = None

# Sidebar for API key
with st.sidebar:
    st.title("Configuration")
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        if st.session_state.rag_agent is None:
            st.session_state.rag_agent = PDFRAGAgent()

# Main content
st.title("PDF RAG Agent")

# File uploader
uploaded_files = st.file_uploader("Upload PDF Documents", type=['pdf'], accept_multiple_files=True)

if uploaded_files and api_key:
    if st.button("Process PDFs"):
        with st.spinner("Processing PDFs..."):
            for pdf_file in uploaded_files:
                st.session_state.rag_agent.process_pdf(pdf_file)
        st.success("PDFs processed successfully!")

    # Query interface
    st.subheader("Ask Questions")
    user_query = st.text_input("Enter your question about the documents")
    
    if user_query:
        with st.spinner("Generating response..."):
            response, citations = st.session_state.rag_agent.query(user_query)
            
            # Display response
            st.write("### Response")
            st.write(response)
            
            # Display citations
            if citations:
                st.write("### Sources")
                for citation in citations:
                    st.write(f"- {citation}")

elif not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
elif not uploaded_files:
    st.info("Please upload PDF documents to begin.")
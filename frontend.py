import streamlit as st
from backend import PDFRAGAgent

def main():
    st.set_page_config(page_title="PDF RAG Agent", layout="wide")
    
    # Sidebar for API key
    with st.sidebar:
        st.title("Configuration")
        api_key = st.text_input("Enter OpenAI API Key", type="password")
        st.caption("Your API key is required for processing")
        
        # Initialize agent when API key is provided
        if api_key:
            agent = PDFRAGAgent(api_key)
            st.session_state['agent'] = agent
            st.success("Agent initialized successfully!")
        else:
            st.warning("Please enter your OpenAI API key to continue")
            st.stop()
    
    st.title("PDF RAG Agent")
    
    # File upload section
    uploaded_files = st.file_uploader(
        "Upload PDF Documents", 
        type=['pdf'], 
        accept_multiple_files=True
    )
    
    if uploaded_files:
        # Process uploaded files
        with st.spinner("Processing PDF documents..."):
            for pdf_file in uploaded_files:
                if pdf_file.name not in st.session_state.get('processed_files', []):
                    agent.process_pdf(pdf_file)
                    if 'processed_files' not in st.session_state:
                        st.session_state.processed_files = []
                    st.session_state.processed_files.append(pdf_file.name)
        
        st.success(f"Processed {len(uploaded_files)} PDF documents")
        
        # Query section
        st.subheader("Ask Questions")
        query = st.text_input("Enter your question about the documents")
        
        if query:
            with st.spinner("Generating response..."):
                response = agent.get_response(query)
                
                # Display response
                st.markdown("### Response")
                st.write(response['answer'])
                
                # Display sources
                st.markdown("### Sources")
                for source in response['sources']:
                    st.markdown(f"- **{source['file']}** (Page {source['page']})")
                    st.markdown(f"  > {source['text']}")

if __name__ == "__main__":
    main()
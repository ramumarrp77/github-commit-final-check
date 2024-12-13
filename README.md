# LangGraph PDF-Based RAG Agent

## Project Description
The **LangGraph PDF-Based RAG Agent** is a local application designed to assist users in retrieving information from PDF documents. By leveraging semantic search and contextual response generation, this agent allows users to upload PDF files, query them using natural language, and receive informative responses that cite the sources of the information.

### Key Features
- **PDF Loading and Processing**: Users can upload and load PDF documents from local storage.
- **Semantic Embedding Generation**: The agent generates and stores embeddings locally for efficient reuse, avoiding the need for reprocessing.
- **Semantic Search**: A semantic search index is built using the embeddings, enabling natural language queries to retrieve relevant passages or sections from the PDFs.
- **Contextual Response Generation**: The agent combines retrieved passages with language model capabilities to generate clear and informative responses, citing sources including the PDF file name and page number.

## Code Structure

```
project-root/
│
├── frontend.py          # Streamlit frontend for user interaction
├── backend.py           # Backend logic for processing PDFs and generating responses
├── requirements.txt     # List of dependencies required for the project
└── README.md            # Project documentation

```

### Key Files and Modules
- **frontend.py**: Contains the Streamlit application that allows users to upload PDFs, enter queries, and display responses.
- **backend.py**: Implements the PDF processing, semantic embedding generation, and response generation logic.
- **requirements.txt**: Lists the necessary Python packages for the project.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps
1. **Clone the repository**:
   <bash>
   git clone https://github.com/yourusername/langgraph-pdf-rag-agent.git
   cd langgraph-pdf-rag-agent
   </bash>

2. **Set up the development environment** (optional but recommended):
   <bash>
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   </bash>

3. **Install dependencies**:
   <bash>
   pip install -r requirements.txt
   </bash>

4. **Run the application**:
   <bash>
   streamlit run frontend.py
   </bash>

## Dependencies
- `langgraph==0.2.53`
- `streamlit`
- `PyPDF2`
- `langchain_openai`
- `langchain_community`
- `langchain`
- `langchain_core`

## Configuration Instructions
- To use the application, you will need an OpenAI API key. Enter your API key in the sidebar of the Streamlit application after launching it.

## Usage Examples
1. Upload one or more PDF documents using the file uploader.
2. Enter a question related to the content of the uploaded PDFs in the query input box.
3. The agent will process the PDFs and generate a response based on the query, citing the relevant sources.

## Troubleshooting Tips
- If you encounter issues with PDF processing, ensure that the PDF files are not corrupted and are in a supported format.
- Make sure your OpenAI API key is valid and has the necessary permissions.
- If the application fails to start, check the terminal for error messages and ensure all dependencies are installed correctly.

This README provides a comprehensive overview of the LangGraph PDF-Based RAG Agent, guiding users through setup, usage, and troubleshooting.
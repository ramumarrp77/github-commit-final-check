# LangGraph PDF-Based RAG Agent

## Project Description
The LangGraph PDF-Based RAG Agent is a local application designed to assist users in retrieving information from PDF documents. By leveraging semantic search and contextual response generation, this agent allows users to upload PDF files, query them using natural language, and receive informative responses that cite the sources accurately. This project addresses the challenge of efficiently extracting relevant information from large volumes of PDF documents, making it easier for users to find the information they need.

## Key Features
- **PDF Loading and Processing**: Users can upload and load PDF documents from local storage.
- **Semantic Embedding Generation**: The agent generates and stores embeddings locally to enable efficient reuse and avoid reprocessing.
- **Semantic Search**: A semantic search index is built using the embeddings, allowing for natural language querying to retrieve the most relevant passages or sections from the PDFs.
- **Contextual Response Generation**: The agent combines retrieved passages with language model capabilities to generate clear and informative responses, citing sources including the PDF file name and page number.

## Code Structure

```
project-root/
│
├── frontend.py          # Streamlit frontend for user interaction
├── backend.py           # Backend logic for PDF processing and querying
├── requirements.txt     # List of dependencies for the project
└── README.md            # Project documentation

```

### Key Files and Modules
- **frontend.py**: Contains the Streamlit application that allows users to upload PDFs, enter queries, and display results.
- **backend.py**: Implements the core logic for processing PDFs, generating embeddings, and querying the documents.
- **requirements.txt**: Lists all the necessary Python packages required to run the application.

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
- `tempfile`
- `os`
- `typing`
- `langchain_openai`
- `langchain_community`
- `langchain`
- `chromadb`

## Configuration Instructions
- To use the application, you will need an OpenAI API key. Enter your API key in the sidebar of the Streamlit application to enable the agent's functionality.

## Usage Examples
1. **Upload PDF Documents**: Use the file uploader in the sidebar to upload one or more PDF documents.
2. **Ask Questions**: After processing the PDFs, enter your question in the provided text input field to retrieve relevant information.
3. **View Responses**: The application will display the generated response along with citations for the sources used.

## Troubleshooting Tips
- Ensure that your OpenAI API key is valid and entered correctly.
- If you encounter issues with PDF processing, check the format and content of the uploaded PDFs.
- For any errors during execution, refer to the console output for debugging information.

This README provides a comprehensive overview of the LangGraph PDF-Based RAG Agent, guiding users through setup, usage, and troubleshooting.
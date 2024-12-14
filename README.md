# LangGraph PDF-Based RAG Agent

## Project Description
The **LangGraph PDF-Based RAG Agent** is a local application designed to assist users in retrieving information from PDF documents. By leveraging semantic search and contextual response generation, this agent allows users to upload PDF files, query them using natural language, and receive informative responses with proper citations. The main problem this project addresses is the difficulty in extracting relevant information from large volumes of PDF documents efficiently.

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
- **frontend.py**: Contains the Streamlit application that allows users to upload PDFs, enter queries, and display responses.
- **backend.py**: Implements the PDF processing, embedding generation, semantic search, and response generation logic.
- **requirements.txt**: Lists all the necessary Python packages required to run the application.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- An OpenAI API key (for using OpenAI models)

### Installation Steps
1. **Clone the repository**:
   <bash>
   git clone https://github.com/yourusername/langgraph-pdf-rag-agent.git
   cd langgraph-pdf-rag-agent
   </bash>

2. **Set up the development environment**:
   It is recommended to use a virtual environment. You can create one using:
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
- `langchain_community`
- `langchain`
- `langchain_openai`
- `langchain_core`
- `langchain.prompts`
- `typing_extensions`
- `tempfile`
- `logging`
- `dataclasses`
- `os`
- `pathlib`

## Configuration Instructions
1. Open the application in your web browser (usually at `http://localhost:8501`).
2. In the sidebar, enter your OpenAI API key to enable the agent\'s capabilities.

## Usage Examples
1. **Upload PDF Documents**: Click on the file uploader to select and upload your PDF documents.
2. **Ask Questions**: Enter your question in the provided text input and click "Process PDFs" to retrieve relevant information.
3. **View Responses**: The agent will display the generated response along with citations from the uploaded documents.

## Troubleshooting Tips
- If you encounter issues with PDF processing, ensure that the files are not corrupted and are in the correct format.
- Make sure your OpenAI API key is valid and has the necessary permissions.
- Check the console for any error messages that may indicate what went wrong during processing or querying.

This README provides a comprehensive overview of the LangGraph PDF-Based RAG Agent, guiding users through setup, usage, and troubleshooting.
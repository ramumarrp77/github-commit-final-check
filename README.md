# LangGraph PDF-Based RAG Agent

## Project Description
The **LangGraph PDF-Based RAG Agent** is a local application designed to assist users in retrieving information from PDF documents. It allows users to upload PDF files, generate semantic embeddings, perform natural language queries, and generate contextual responses based on the retrieved information. This project addresses the challenge of efficiently extracting and utilizing information from large volumes of PDF documents, making it easier for users to find relevant content quickly.

## Key Features
- **PDF Loading and Processing**: Users can upload and load PDF documents from their local storage.
- **Semantic Embedding Generation**: The application generates and stores embeddings locally to avoid reprocessing.
- **Semantic Search**: Users can perform natural language queries to retrieve the most relevant passages or sections from the PDFs.
- **Contextual Response Generation**: The agent combines retrieved passages with language model capabilities to generate clear and informative responses, citing sources including the PDF file name and page number.

## Code Structure

```
/langgraph_pdf_rag_agent
│
├── frontend.py          # Streamlit UI for user interaction
├── backend.py           # Backend logic for PDF processing and embedding generation
└── requirements.txt     # List of dependencies required for the project

```

### Key Files and Modules
- **frontend.py**: Contains the Streamlit user interface, allowing users to upload PDFs, generate embeddings, search documents, and generate responses.
- **backend.py**: Implements the core functionality for loading PDFs, generating embeddings, searching documents, and generating responses using OpenAI\'s language model.
- **requirements.txt**: Lists the necessary Python packages for the project.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- An OpenAI API key (for using OpenAI\'s language model)

### Installation Steps
1. **Clone the repository**:
   <bash>
   git clone https://github.com/yourusername/langgraph_pdf_rag_agent.git
   cd langgraph_pdf_rag_agent
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
- `numpy`
- `langchain`

## Configuration Instructions
- Before running the application, ensure you have your OpenAI API key ready. You will be prompted to enter it in the sidebar of the Streamlit interface.

## Usage Examples
1. **Upload PDF Files**: Use the file uploader to select and upload one or more PDF documents.
2. **Generate Embeddings**: After loading a PDF, click the button to generate embeddings for the document.
3. **Search Documents**: Enter a search query in the input field and click "Search" to retrieve relevant sections from the uploaded PDFs.
4. **Generate Response**: Click the "Generate Response" button to receive a contextual response based on your query, including citations from the PDF.

## Troubleshooting Tips
- If you encounter issues with PDF loading, ensure that the files are not corrupted and are in the correct format.
- For API-related errors, verify that your OpenAI API key is valid and has the necessary permissions.
- If the application is slow, consider optimizing the PDF size or the number of documents being processed simultaneously.

This README provides a comprehensive overview of the LangGraph PDF-Based RAG Agent, guiding users through setup, usage, and troubleshooting.
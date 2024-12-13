# LangGraph PDF-Based RAG Agent

## Project Description
The **LangGraph PDF-Based RAG Agent** is a local application designed to assist users in retrieving information from PDF documents. It allows users to upload PDFs, generate semantic embeddings, perform semantic searches, and generate contextual responses based on user queries. This project addresses the challenge of efficiently extracting relevant information from large volumes of text contained in PDF files, making it easier for users to find and understand the information they need.

## Key Features
- **PDF Loading and Processing**: Users can upload and load PDF documents from their local storage.
- **Semantic Embedding Generation**: The application generates and stores embeddings locally to avoid reprocessing.
- **Semantic Search**: Users can perform natural language queries to retrieve the most relevant passages or sections from the PDFs.
- **Contextual Response Generation**: The agent combines retrieved passages with language model capabilities to generate clear and informative responses, citing sources including the PDF file name and page number.

## Code Structure

```
/langgraph-pdf-agent
│
├── frontend.py          # Streamlit frontend for user interaction
├── backend.py           # Backend logic for PDF processing and embedding generation
└── requirements.txt     # List of dependencies required for the project

```

### Key Files and Modules
- **frontend.py**: This file contains the Streamlit application that provides the user interface for uploading PDFs, generating embeddings, searching documents, and generating responses.
- **backend.py**: This file includes the core logic for loading PDFs, generating embeddings, performing semantic searches, and generating responses using the OpenAI language model.
- **requirements.txt**: This file lists all the necessary Python packages required to run the application.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- An OpenAI API key (for using OpenAI models)

### Installation Steps
1. **Clone the repository**:
   <bash>
   git clone https://github.com/yourusername/langgraph-pdf-agent.git
   cd langgraph-pdf-agent
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
- Set your OpenAI API key in the Streamlit sidebar when prompted. This key is necessary for generating embeddings and responses using OpenAI\'s models.

## Usage Examples
1. **Upload PDF**: Click on the "Upload PDF files" button to select and upload your PDF documents.
2. **Generate Embeddings**: After loading a PDF, click the "Generate Embeddings" button to create embeddings for the uploaded document.
3. **Search Documents**: Enter your query in the text input field and click the "Search" button to retrieve relevant passages from the PDFs.
4. **Generate Response**: Click the "Generate Response" button to get a contextual response based on your query.

## Troubleshooting Tips
- If you encounter issues with loading PDFs, ensure that the files are not corrupted and are in the correct format.
- If embeddings are not generated, check that your OpenAI API key is correctly set and that you have internet access.
- For any errors related to missing packages, ensure that all dependencies in `requirements.txt` are installed correctly.

Feel free to contribute to the project by submitting issues or pull requests!
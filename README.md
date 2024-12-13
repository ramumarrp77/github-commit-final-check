# LangGraph PDF-Based RAG Agent

## Project Description
The **LangGraph PDF-Based RAG Agent** is a local application designed to assist users in retrieving information from PDF documents. It allows users to upload PDF files, generate semantic embeddings, perform natural language queries, and generate contextual responses based on the retrieved information. This project addresses the challenge of efficiently extracting and utilizing information from large volumes of text contained in PDF files.

## Key Features
- **PDF Loading and Processing**: Users can upload and load PDF documents from local storage.
- **Semantic Embedding Generation**: The application generates and stores embeddings locally for efficient reuse.
- **Semantic Search**: Users can perform natural language queries to retrieve relevant passages or sections from the PDFs.
- **Contextual Response Generation**: The agent combines retrieved passages with language model capabilities to generate informative responses, including citations for sources.

## Code Structure

```
/langgraph_pdf_rag_agent
│
├── frontend.py          # Streamlit UI for user interaction
├── backend.py           # Core logic for PDF processing, embedding generation, and response generation
└── requirements.txt     # List of dependencies required for the project

```

### Key Files and Modules
- **frontend.py**: Contains the Streamlit user interface, allowing users to upload PDFs, generate embeddings, search documents, and generate responses.
- **backend.py**: Implements the core functionalities, including loading PDFs, generating embeddings, searching documents, and generating responses using a language model.
- **requirements.txt**: Lists the necessary Python packages for the project.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps
1. **Clone the repository**:
   <bash>
   git clone https://github.com/yourusername/langgraph_pdf_rag_agent.git
   cd langgraph_pdf_rag_agent
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
- `numpy`
- `langchain`

## Configuration Instructions
- Ensure you have an OpenAI API key to utilize the language model features. You can enter your API key in the sidebar of the Streamlit application.

## Usage Examples
1. **Upload PDF Files**: Use the file uploader to select and upload one or more PDF documents.
2. **Generate Embeddings**: Click the "Generate Embeddings" button to create embeddings for the uploaded PDFs.
3. **Search Documents**: Enter a search query in the input field and click "Search" to retrieve relevant passages.
4. **Generate Response**: After performing a search, enter a query and click "Generate Response" to receive a contextual answer based on the retrieved information.

## Troubleshooting Tips
- If you encounter issues loading a PDF, ensure the file is not corrupted and is in a supported format.
- If embeddings fail to generate, check that the PDF contains extractable text.
- For search queries returning no results, verify that the embeddings have been generated successfully.

Feel free to reach out for any issues or contributions to enhance the LangGraph PDF-Based RAG Agent!
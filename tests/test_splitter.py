from langchain_community.document_loaders import PyMuPDFLoader
from test_loader import document_list
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(document_list)

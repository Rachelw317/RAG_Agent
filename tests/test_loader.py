from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

raw_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
documents = []

for pdf_file in raw_dir.glob("*.pdf"):
    loader = PyPDFLoader(str(pdf_file))
    file_documents = loader.load()
    documents.extend(file_documents)

print(f"Loaded {len(documents)} documents from {len(list(raw_dir.glob('*.pdf')))} PDF files.")
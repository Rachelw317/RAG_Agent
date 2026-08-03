from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from pathlib import Path


raw_file_dir = Path(__file__).resolve().parent.parent / "data" / "raw"

document_list = []

for file in raw_file_dir.iterdir():
    if file.suffix == ".pdf":
        loader = PyMuPDFLoader(file)
        document_list.extend(loader.load())


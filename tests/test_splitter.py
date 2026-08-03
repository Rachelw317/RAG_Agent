from langchain_community.document_loaders import PyMuPDFLoader
from test_loader import document_list
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(document_list)

print(f"Number of chunks: {len(chunks)}")
print(f"First chunk type: {type(chunks[0])}")
print(f"First chunk content: {chunks[0].page_content[:]}")
print(f"Second chunk content: {chunks[1].page_content[:]}")

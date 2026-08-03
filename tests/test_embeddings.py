from test_splitter import chunks

from FlagEmbedding import FlagModel

# Load BGE model
model = FlagModel('BAAI/bge-base-en-v1.5')

# encode the queries and corpus
embeddings = model.encode(chunks, batch_size=8, show_progress_bar=True)
print(f"Embeddings:\n{embeddings.shape}")


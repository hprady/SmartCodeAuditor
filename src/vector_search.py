import chromadb
from embedding_engine import get_code_embedding

# initialize database
client = chromadb.Client()

collection = client.create_collection("bug_patterns")


def add_bug_pattern(code, fix, description):

    embedding = get_code_embedding(code)

    collection.add(
        documents=[code],
        embeddings=embedding.tolist(),
        metadatas=[{
            "fix": fix,
            "description": description
        }],
        ids=[code]
    )


def search_similar_bug(code):

    embedding = get_code_embedding(code)

    results = collection.query(
        query_embeddings=embedding.tolist(),
        n_results=3
    )

    return results
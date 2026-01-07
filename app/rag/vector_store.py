from chromadb import Client
from chromadb.config import Settings
from pathlib import Path

# Persistent storage path
CHROMA_PATH = Path("app/chroma")

# Singleton client (VERY IMPORTANT)
_client = None
_collection = None


def get_vector_store():
    global _client, _collection

    if _client is None:
        _client = Client(
            Settings(
                persist_directory=str(CHROMA_PATH),
                anonymized_telemetry=False,
            )
        )

    if _collection is None:
        _collection = _client.get_or_create_collection(name="documents")

    return _collection


def add_documents(texts: list[str], metadatas: list[dict]):
    collection = get_vector_store()

    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=[f"doc-{i}" for i in range(len(texts))],
    )

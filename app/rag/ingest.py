from app.rag.vector_store import add_documents


def simple_chunk(text: str, chunk_size: int = 500):
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


def ingest_text(text: str):
    chunks = simple_chunk(text)

    metadatas = [{"source": "manual"} for _ in chunks]

    add_documents(chunks, metadatas)

    return len(chunks)

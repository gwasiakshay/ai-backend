from app.rag.vector_store import get_vector_store


def retrieve_chunks(query: str, k: int = 3):
    collection = get_vector_store()

    results = collection.query(
        query_texts=[query],
        n_results=k,
    )

    return results["documents"][0]

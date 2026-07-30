from app.rag.embedding_service import generate_embeddings
from app.rag.vector_store import search_chunks


def semantic_search(
        query : str,
        user_id : int,
        limit:int=5
):
    query_embedding = generate_embeddings([query])[0]
    results = search_chunks(
        query_embedding,
        user_id,
        limit
    )

    if not results["documents"] or not results["documents"][0]:
        return []

    return results["documents"][0]

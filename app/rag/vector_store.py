import chromadb
from app.rag.embedding_service import generate_embeddings
client = chromadb.PersistentClient(
    path="../storage/chroma"
)

collection = client.get_or_create_collection(
    name = "document_chunks"
)

def generate_chunk_id(
    document_id:int,
    index:int
)->str:
    return f"document_{document_id}_chunk_{index}"


def generate_metadata(
        user_id:int,
        document_id:int,
        index:int
)->dict:
    return {
            "document_id": document_id,
            "user_id": user_id,
            "chunk_index": index
        }


def store_document_chunks(
        chunks:list[str],
        embeddings:list[list[float]],
        document_id:int,
        user_id:int
)->None:
    if not chunks:
        return

    if len(chunks) != len(embeddings):
        raise ValueError(
            "Number of chunks and embeddings must match"
        )
    chunk_ids = []
    metadatas = []
    for index,chunk in enumerate(chunks):
        chunk_ids.append(generate_chunk_id(document_id,index))
        metadatas.append(generate_metadata(user_id,document_id,index))

    collection.add(
        ids=chunk_ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def delete_document_chunks(
        document_id : int
):
    collection.delete(
        where={"document_id":document_id}
    )

def search_chunks(
        query_embedding : list[float],
        user_id : int,
        limit : int = 5
):
    return collection.query(
        query_embeddings = [query_embedding],
        n_results = limit,
        where = {"user_id":user_id},
        include=["documents", "metadatas", "distances"]
    )




# texts = ["The vehicle shall detect pedestrians within 100 milliseconds.",
#         "The PostgreSQL database stores user account information.",
#         "JWT access tokens expire after thirty minutes."]
#
# embedding = generate_embeddings(texts)
#
# collection.add(
#     ids=["test_chunk_1","test_chunk_2","test_chunk_3"],
#     documents=texts,
#     embeddings=embedding,
#     metadatas=[
#         {
#             "document_id":1,
#             "user_id":1,
#             "chunk_index":0
#         },
#         {
#             "document_id":2,
#             "user_id":4,
#             "chunk_index":4
#         },
#         {
#             "document_id":3,
#             "user_id":5,
#             "chunk_index":3
#         }
#     ]
# )
#
# result = collection.get(
#     ids=["test_chunk_1"],
#     include=["documents","embeddings","metadatas"]
# )
#
# # print(result)
#
# question = "How long before the JWT token expires?"
#
# question_embedding = generate_embeddings([question])[0]
#
# print(collection.query(
#     query_embeddings=[question_embedding],
#     n_results=1,
#     include=["documents", "metadatas", "distances"]
# ))


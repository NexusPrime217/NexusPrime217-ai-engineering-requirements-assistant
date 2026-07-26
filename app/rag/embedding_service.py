from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "The vehicle shall detect pedestrians.",
    "The car must identify people in its path.",
    "The database stores user passwords."
]

# embedding = model.encode(texts)

# similarity_ab=cos_sim(embedding[0],embedding[1])
# similarity_bc=cos_sim(embedding[1],embedding[2])
# similarity_ca=cos_sim(embedding[0],embedding[2])

# print(similarity_ab)
# print(similarity_bc)
# print(similarity_ca)


def generate_embeddings(
        chunks:list[str]
)->list[list[float]]:
    if not chunks:
        return []
    embeddings = model.encode(chunks)
    return embeddings.tolist()

# print(generate_embeddings(texts))

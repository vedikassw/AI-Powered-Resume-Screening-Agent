from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once (important)
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_similarity(resume_text, job_description):
    embeddings = model.encode([resume_text, job_description])

    similarity_score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(float(similarity_score) * 100, 2)

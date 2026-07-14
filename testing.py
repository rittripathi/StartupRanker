from app.embeddings import get_embedding

vec = get_embedding("A subscription box for spices")
print(len(vec))
print(vec[:5])
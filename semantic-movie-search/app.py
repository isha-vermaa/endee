import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading dataset...")

data = pd.read_csv("tmdb_5000_movies.csv")

movies = data["overview"].dropna().head(500).tolist()

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

movie_embeddings = model.encode(movies)

query = input("Enter a movie theme: ")

query_embedding = model.encode([query])

similarities = np.dot(movie_embeddings, query_embedding.T)

top_results = np.argsort(similarities, axis=0)[-5:][::-1]

print("\nRecommended Movies:\n")

for idx in top_results:
    print(movies[idx[0]])

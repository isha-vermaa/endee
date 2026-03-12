import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading movie dataset...")

# Load dataset
data = pd.read_csv("tmdb_5000_movies.csv")

# Take movie descriptions
movies = data["overview"].dropna().head(500).tolist()

print("Loading AI model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert movie descriptions into embeddings
movie_embeddings = model.encode(movies)

# User input
query = input("Enter movie theme: ")

# Convert query to embedding
query_embedding = model.encode([query])

# Calculate similarity
similarities = np.dot(movie_embeddings, query_embedding.T)

# Get top 5 similar movies
top_results = np.argsort(similarities, axis=0)[-5:][::-1]

print("\nRecommended Movies:\n")

for idx in top_results:
    print(movies[idx[0]])

# Semantic Movie Search using Endee Vector Database

## Project Overview
This project demonstrates a semantic movie recommendation system using vector embeddings and similarity search.  
Movie descriptions are converted into embeddings and relevant movies are retrieved based on semantic similarity.

The project showcases how **vector databases like Endee** enable AI applications such as semantic search, recommendation systems, and Retrieval Augmented Generation (RAG).


## Problem Statement
Users often struggle to find relevant content using traditional keyword search.

This project solves the problem by converting movie descriptions into vector embeddings and retrieving similar results.

## Technology Used
Python  
Sentence Transformers  
Endee Vector Database  

## Example Use Case
User Query:
space mission

Results:
Interstellar  
The Martian  
Gravity


## System Design

User Query  
↓  
Convert query into vector embedding using Sentence Transformers  
↓  
Store movie embeddings in vector database (Endee)  
↓  
Perform semantic similarity search  
↓  
Retrieve most relevant movie descriptions  

---

## How Endee Vector Database is Used

This project demonstrates the concept of semantic search using vector embeddings.  
Movie descriptions from the TMDB dataset are converted into vector embeddings using the Sentence Transformers model.

These embeddings can be efficiently stored and searched using a vector database such as **Endee**.  
Vector databases allow similarity search by comparing embeddings rather than relying on keyword matching.

This enables AI applications such as:

- Semantic search
- Recommendation systems
- Retrieval Augmented Generation (RAG)
- AI knowledge assistants

Endee provides high-performance vector indexing and retrieval, making it suitable for large-scale AI applications.


## Setup Instructions

Clone the repository:

git clone https://github.com/isha-vermaa/endee

Navigate to project folder:

cd semantic-movie-search

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

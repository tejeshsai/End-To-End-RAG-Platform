import pytest
from src.embeddings.vector_store import VectorStore


def test_vector_store():
    vector_store = VectorStore(name="test_vector_store")
    vector_store.add_documents("1", text="alpha beta", embedding=[1.0, 0.0])
    vector_store.add_documents("2", text="gamma delta", embedding=[0.0, 1.0])

    results = vector_store.query(query_embedding=[0.9, 0.0], top_k=1)
    assert vector_store.name == "test_vector_store"
    assert len(results["documents"]) == 1

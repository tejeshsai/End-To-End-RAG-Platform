from chromadb import PersistentClient
import os
class VectorStore:
    def __init__(self, name : str):
        db_path = "chroma_db"
        os.makedirs(db_path, exist_ok = True)
        self.client = PersistentClient(path = f"chroma_db")
        self.collection = self.client.get_or_create_collection(name = name)
        self.name = name

    def add_documents(self, doc_id : str, text : str, embedding : list[float]):
        self.collection.add(
            documents = [text],
            ids = [doc_id],
            embeddings = [embedding]
        )

    def query(self, query_embedding : list[float], top_k : int = 3) -> list[str]:
        results = self.collection.query(
            query_embeddings= [query_embedding],
            n_results = top_k
        )
        return results

    def count(self) -> int:
        return self.collection.count()
            
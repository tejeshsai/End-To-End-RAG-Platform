from chromadb import PersistentClient

class VectorStore:
    def __init__(self, name : str):
        self.client = PersistentClient(path = f"chroma_db")
        self.collection = self.client.get_or_create_collection(name = name)

    def add_documents(self, doc_id : str, text : str, embedding : list[float]):
        self.collection.add(
            documents = [text],
            ids = [doc_id],
            embeddings = [embedding]
        )

    def query(self, query_embedding : list[float], k : int = 3) -> list[str]:
        results = self.collection.query(
            query_embeddings= [query_embedding],
            n_results = k
        )
        return results

    def count(self) -> int:
        return self.collection.count()
            
from typing import List
from pathlib import Path

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions


class ECCVectorStore:
    """
    Handles vector storage for ECC content using ChromaDB.
    """

    def __init__(self, persist_dir: str = "chroma_store"):
        self.persist_dir = Path(persist_dir)
        self.persist_dir.mkdir(parents=True, exist_ok=True)

        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        self.client = chromadb.Client(
            Settings(
                persist_directory=str(self.persist_dir),
                anonymized_telemetry=False
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="ecc_controls",
            embedding_function=self.embedding_function
        )

    def add_documents(self, documents: List[str]):
        """
        Store text chunks as vectors.
        """
        ids = [f"doc_{i}" for i in range(len(documents))]
        self.collection.add(
            documents=documents,
            ids=ids
        )

    def get_collection(self):
        return self.collection

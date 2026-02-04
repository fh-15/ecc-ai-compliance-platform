from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from pathlib import Path


def build_vector_store(documents: list):
    persist_directory = Path(__file__).parent / "chroma_db"

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=str(persist_directory)
    )

    vectorstore.persist()
    return vectorstore

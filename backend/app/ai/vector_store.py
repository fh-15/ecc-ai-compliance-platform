from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings


def create_vector_store(docs, persist_dir="./chroma"):
    embeddings = OpenAIEmbeddings()
    return Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persist_dir
    )

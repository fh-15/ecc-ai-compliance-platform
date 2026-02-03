from app.ai.loader import load_pdf
from app.ai.splitter import split_documents
from app.ai.vector_store import create_vector_store

PDF_PATH = "backend/app/ai/data/ecc_10_controls.pdf"


def build_index():
    documents = load_pdf(PDF_PATH)
    chunks = split_documents(documents)
    create_vector_store(chunks)
    print("Vector store built successfully")


if __name__ == "__main__":
    build_index()

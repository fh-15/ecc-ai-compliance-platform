from langchain.document_loaders import PyPDFLoader
from pathlib import Path


def load_ecc_pdf() -> list:
    pdf_path = Path(__file__).parent / "data" / "ecc_10_controls.pdf"

    if not pdf_path.exists():
        raise FileNotFoundError("ECC PDF file not found")

    loader = PyPDFLoader(str(pdf_path))
    return loader.load()

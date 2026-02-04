from pathlib import Path
from typing import List

import fitz  # PyMuPDF
from langchain.schema import Document


def load_pdf(pdf_path: str) -> List[Document]:
    """
    Load ECC PDF file and return LangChain Document objects.
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Provided file is not a PDF")

    document = fitz.open(pdf_path)
    documents: List[Document] = []

    for page_number in range(len(document)):
        page = document.load_page(page_number)
        text = page.get_text("text")

        if not text:
            continue

        cleaned_text = _clean_text(text)

        documents.append(
            Document(
                page_content=cleaned_text,
                metadata={
                    "source": pdf_path.name,
                    "page": page_number + 1
                }
            )
        )

    document.close()
    return documents


def _clean_text(text: str) -> str:
    """
    Normalize text for downstream AI processing.
    """
    return (
        text.replace("\x00", "")
        .replace("\r", "\n")
        .strip()
    )

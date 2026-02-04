from pathlib import Path
from typing import List

import fitz  # PyMuPDF


class ECCPDFLoader:
    """
    Responsible for loading ECC controls from the official PDF document.
    This class is the SINGLE source of truth for ECC textual content.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

        if not self.pdf_path.exists():
            raise FileNotFoundError(
                f"ECC PDF not found at path: {self.pdf_path}"
            )

        if self.pdf_path.suffix.lower() != ".pdf":
            raise ValueError("Provided ECC file must be a PDF")

    def load_text(self) -> str:
        """
        Extract full text from the ECC PDF.
        Returns:
            str: Complete extracted text
        """
        document = fitz.open(self.pdf_path)
        extracted_pages: List[str] = []

        for page_number in range(len(document)):
            page = document.load_page(page_number)
            text = page.get_text("text").strip()

            if text:
                extracted_pages.append(text)

        document.close()

        if not extracted_pages:
            raise ValueError("ECC PDF loaded but no text could be extracted")

        return "\n\n".join(extracted_pages)

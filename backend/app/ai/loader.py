from pathlib import Path
from typing import List
import fitz  # PyMuPDF


class PDFLoader:
    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {self.pdf_path}")

        if self.pdf_path.suffix.lower() != ".pdf":
            raise ValueError("Provided file is not a PDF")

    def load_text(self) -> str:
        """
        Extract full text from the PDF in reading order.
        """
        document = fitz.open(self.pdf_path)
        pages_text: List[str] = []

        for page_number in range(len(document)):
            page = document.load_page(page_number)
            text = page.get_text("text")

            if text:
                cleaned = self._clean_text(text)
                pages_text.append(cleaned)

        document.close()
        return "\n".join(pages_text)

    @staticmethod
    def _clean_text(text: str) -> str:
        """
        Normalize text for downstream AI processing.
        """
        return (
            text.replace("\x00", "")
            .replace("\r", "\n")
            .strip()
        )

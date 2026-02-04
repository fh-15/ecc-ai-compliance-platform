from typing import List
import re


class TextSplitter:
    def __init__(
        self,
        chunk_size: int = 800,
        overlap: int = 100
    ):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks suitable for vector storage.
        """
        paragraphs = self._split_by_paragraphs(text)
        chunks: List[str] = []

        current_chunk = ""

        for paragraph in paragraphs:
            if len(current_chunk) + len(paragraph) <= self.chunk_size:
                current_chunk += paragraph + "\n"
            else:
                chunks.append(current_chunk.strip())

                # overlap handling
                overlap_text = current_chunk[-self.overlap:]
                current_chunk = overlap_text + paragraph + "\n"

        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        return chunks

    @staticmethod
    def _split_by_paragraphs(text: str) -> List[str]:
        """
        Split text by logical paragraphs / headings.
        """
        blocks = re.split(r"\n\s*\n", text)
        return [b.strip() for b in blocks if b.strip()]

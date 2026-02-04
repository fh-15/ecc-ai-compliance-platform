from app.ai.loader import load_ecc_pdf
from app.ai.splitter import split_documents
from app.ai.vector_store import build_vector_store
from app.ai.engine import build_ai_engine
from app.ai.prompts import ASSESSMENT_PROMPT, GUIDANCE_PROMPT
from app.domain.ecc_controls import ECC_CONTROLS


class AIAuditService:
    """
    This service connects ECC audit logic with the AI engine.
    It supports two modes:
    1. Assessment (generate audit questions)
    2. Guidance (explain gaps and implementation steps)
    """

    def __init__(self):
        documents = load_ecc_pdf()
        chunks = split_documents(documents)
        self.vectorstore = build_vector_store(chunks)
        self.ai_engine = build_ai_engine(self.vectorstore)

    def generate_assessment_questions(self, control_code: str) -> str:
        """
        Generates assessment questions for a specific ECC control.
        """
        prompt = ASSESSMENT_PROMPT.replace("{context}", control_code)
        response = self.ai_engine.run(prompt)
        return response

    def generate_guidance(self, control_code: str) -> str:
        """
        Generates implementation guidance for a specific ECC control.
        """
        prompt = GUIDANCE_PROMPT.replace("{context}", control_code)
        response = self.ai_engine.run(prompt)
        return response

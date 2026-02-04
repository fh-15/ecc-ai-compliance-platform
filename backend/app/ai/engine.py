from typing import Literal

from app.ai.prompts import ASSESSMENT_PROMPT, GUIDANCE_PROMPT
from app.ai.vector_store import ECCVectorStore

from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA


class ECCAIEngine:
    """
    Main AI engine for ECC compliance.
    Supports two modes:
    - assessment: generate audit questions
    - guidance: provide implementation guidance
    """

    def __init__(self):
        # Local vector store (ECC only)
        self.vector_store = ECCVectorStore().get_collection()

        # Local LLM (no API key, no cloud)
        self.llm = Ollama(
            model="llama3",
            temperature=0
        )

        # Retriever
        self.retriever = self.vector_store.as_retriever(
            search_kwargs={"k": 4}
        )

    def run(
        self,
        query: str,
        mode: Literal["assessment", "guidance"]
    ) -> str:
        """
        Run the AI engine in the specified mode.
        """

        if mode == "assessment":
            prompt_template = ASSESSMENT_PROMPT
        elif mode == "guidance":
            prompt_template = GUIDANCE_PROMPT
        else:
            raise ValueError("Invalid AI mode")

        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.retriever,
            chain_type="stuff",
            return_source_documents=False
        )

        prompt = prompt_template.replace("{context}", query)
        response = qa_chain.run(prompt)

        return response

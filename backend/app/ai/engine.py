from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from app.ai.prompts import ASSESSMENT_PROMPT, GUIDANCE_PROMPT


def build_ai_engine(vector_store, mode: str):
    llm = ChatOpenAI(temperature=0)

    prompt = ASSESSMENT_PROMPT if mode == "assessment" else GUIDANCE_PROMPT

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )

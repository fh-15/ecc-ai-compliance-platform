from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from app.ai.prompts import SYSTEM_RULES


def build_ai_engine(vectorstore):
    llm = ChatOpenAI(
        model_name="gpt-4",
        temperature=0
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa_chain

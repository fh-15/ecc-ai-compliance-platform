from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from app.ai.prompts import SYSTEM_PROMPT


def build_ai_engine(vectorstore):
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={
            "system_prompt": SYSTEM_PROMPT
        }
    )

    return qa_chain

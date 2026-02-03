from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

from app.ai.prompts import ASSESSMENT_PROMPT, GUIDANCE_PROMPT


def load_vector_store(persist_dir="./chroma"):
    embeddings = OpenAIEmbeddings()
    return Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )


def build_ai_engine(mode: str):
    vector_store = load_vector_store()

    llm = ChatOpenAI(
        temperature=0,
        max_tokens=500
    )

    prompt = ASSESSMENT_PROMPT if mode == "assessment" else GUIDANCE_PROMPT

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )

from langchain.chains import RetrievalQA
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

from app.backend.settings import settings


def answer_question(question: str) -> str:
    chat = ChatOpenAI(openai_api_key=settings.openai_api_key)
    embeddings = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)
    db = Chroma(
        persist_directory="./temp/emb",
        embedding_function=embeddings
    )

    retriever = db.as_retriever()

    chain = RetrievalQA.from_chain_type(
        llm=chat,
        retriever=retriever,
        chain_type="stuff"
    )

    output = chain.invoke({"query": question})

    return output["result"]

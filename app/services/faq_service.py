from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

from app.backend.settings import settings
from app.backend.vector_stores.pinecone_vector_store import vector_store


def answer_question(question: str) -> str:
    chat = ChatOpenAI(openai_api_key=settings.openai_api_key)

    chain = RetrievalQA.from_chain_type(
        llm=chat,
        retriever=vector_store.as_retriever(),
        chain_type="stuff"
    )

    output = chain.invoke({"query": question})

    return output["result"]
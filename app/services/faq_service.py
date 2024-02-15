from langchain.chains import ConversationChain, RetrievalQA

from app.backend.llms.chatopenai import chat
from app.backend.vector_stores.pgvector_vector_store_base import vector_store_base


def answer_simple_chat(question: str) -> str:
    chain = ConversationChain(llm=chat)

    output = chain.predict(input=question)

    return output


def answer_question(question: str) -> str:
    chain = RetrievalQA.from_chain_type(
        llm=chat, retriever=vector_store_base.as_retriever(), chain_type="stuff"
    )

    output = chain.invoke({"query": question})

    return output["result"]

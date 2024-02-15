from langchain.chains import ConversationChain, RetrievalQA
from langchain.memory import ConversationBufferMemory

from app.backend.llms.chatopenai import chat
from app.backend.vector_stores.pgvector_vector_store_base import vector_store_base


def handle_conversation_prompt(prompt: str) -> str:
    chain = ConversationChain(llm=chat, verbose=True, memory=ConversationBufferMemory())

    output = chain.predict(input=prompt)

    return output


def handle_faq_question(question: str) -> str:
    chain = RetrievalQA.from_chain_type(
        llm=chat, retriever=vector_store_base.as_retriever(), chain_type="stuff"
    )

    output = chain.invoke({"query": question})

    return output["result"]

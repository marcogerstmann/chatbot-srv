from langchain.chains import ConversationChain, RetrievalQA

from app.backend.chat.llms.chatopenai import chat
from app.backend.chat.memories.postgres_memory import build_memory
from app.backend.chat.vector_stores.pgvector_vector_store_base import vector_store


def handle_conversation_prompt(prompt: str, session_id: str) -> str:
    chain = ConversationChain(llm=chat, verbose=True, memory=build_memory(session_id))

    output = chain.predict(input=prompt)

    return output


def handle_faq_question(question: str) -> str:
    # TODO: Use ConversationalRetrievalChain instead of RetrievalQA to have memory
    chain = RetrievalQA.from_chain_type(
        llm=chat, retriever=vector_store.as_retriever(), chain_type="stuff"
    )

    output = chain.invoke({"query": question})

    return output["result"]

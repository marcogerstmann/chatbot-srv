from typing import Type

from langchain.agents.tools import BaseTool
from langchain_core.retrievers import BaseRetriever
from pydantic import BaseModel, Field


class GetContextInput(BaseModel):
    query: str = Field(description="should be a search query")


class GetContextTool(BaseTool):
    name = "get_context"
    description = "ALWAYS get the relevant context from this database before answering the users question."
    args_schema: Type[BaseModel] = GetContextInput

    retriever: BaseRetriever

    def __init__(self, retriever: BaseRetriever):
        super(GetContextTool, self).__init__(retriever=retriever)
        self.retriever = retriever

    def _run(self, query: str):
        return self.retriever.get_relevant_documents(query)

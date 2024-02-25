from typing import Type

from langchain.agents.tools import BaseTool
from pydantic import BaseModel, Field


class NoAnswerInput(BaseModel):
    question: str = Field(description="The question to which no answer is available.")


class NoAnswerTool(BaseTool):
    name = "no_answer"
    description = "Run this if you don't know the answer to the users question."
    args_schema: Type[BaseModel] = NoAnswerInput

    # def __init__(self):
    #     super().__init__()
    #     # return_direct means that the current agent run will be stopped
    #     # and the output of this tool can be used directly
    #     self.return_direct = True

    def _run(self, question: str):
        # TODO: Implement
        print(f"To be implemented: {question}")
        return "Das weiß ich leider nicht."

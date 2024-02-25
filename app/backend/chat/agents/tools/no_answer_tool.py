from datetime import datetime
from typing import Type

from langchain.agents.tools import BaseTool
from pydantic import BaseModel, Field

from app.constants import QUESTIONS_WITHOUT_ANSWER_GOOGLE_SHEET
from app.services.google_api_service import add_as_row_to_google_spreadsheet


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
        print(
            f'Assistant didn\'t know the answer to this question: "{question}"'
        )  # TODO: Use logger
        spreadsheet_id = QUESTIONS_WITHOUT_ANSWER_GOOGLE_SHEET
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        values = [timestamp, question]
        add_as_row_to_google_spreadsheet(spreadsheet_id, values)

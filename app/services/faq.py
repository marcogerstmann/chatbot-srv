from app.backend.settings import settings


def answer_question(question: str) -> str:
    print(settings.openai_api_key)
    print(question)
    return "The answer is 42"

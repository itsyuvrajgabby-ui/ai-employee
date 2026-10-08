from openai import OpenAI

from .config import settings


client = OpenAI(
    api_key=settings.openai_api_key
)


SYSTEM_PROMPT = """
You are an AI employee for a business.

Your job is to help employees with legitimate business tasks.

Rules:

1. Be accurate and honest.
2. Never invent company information.
3. If information is unavailable, say so.
4. Never claim an action was completed unless the application
   actually completed it.
5. Protect confidential business information.
6. Give practical and concise answers.
"""


def ask_ai(message: str, company_context: str = "") -> str:

    prompt = f"""
Company information:

{company_context}

Employee request:

{message}
"""

    response = client.responses.create(
        model=settings.ai_model,
        instructions=SYSTEM_PROMPT,
        input=prompt,
    )

    return response.output_text

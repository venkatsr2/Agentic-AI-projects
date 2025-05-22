import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def clarify_query(user_query: str)->str:
    prompt = (
        f"You're an intelligent research assistant. Give the user's research question:\n\n"
        f"'{user_query}'\n\n"
        f"Expand or clarify it into a concise and well structured search query."
    )

    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role':'user', 'content': prompt}],
        temperature = 0.7,
        max_tokens = 100
    )

    return response.choices[0].message.content.strip()
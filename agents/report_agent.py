from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def genrate_report(refined_query, summaries):
    prompt = f"""You are a research assistant. Using the following summaries, generate a structured, well-written report answering the research query: "{refined_query}"
    
    Summaries:
    {summaries}
    Make sure the report is clear, organized, and suitable for professional audience. """

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user", "content":prompt}]
    )

    return response.choices[0].message.content
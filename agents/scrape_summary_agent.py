import os
from dotenv import load_dotenv
from newspaper import Article
from openai import OpenAI

load_dotenv()

client  = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def scrape_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return None
    
def summarize_text(text, max_words = 200):
    prompt = f'summarize the following article in under {max_words} words: \n\n{text}'

    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role':'user', 'content': prompt}],
        temperature = 0.7
    )
    
    return response.choices[0].message.content.strip()

def summarize_article(url):
    content = scrape_article(url)
    if not content:
        return None
    return summarize_text(content)

import os
from dotenv import load_dotenv
from serpapi import GoogleSearch
from duckduckgo_search import DDGS

load_dotenv()

def serpapi_search(query, num_results = 5):
    api_key = os.getenv('SERPAPI_KEY')
    if not api_key:
        return []
    search = GoogleSearch({
        'q': query,
        'api_key': api_key,
        'num': num_results
    })

    results = search.get_dict().get('organic_results', [])
    return [r.get('link') for r in results if r.get('link')]

def duckduckgo_search(query, num_results = 5):
    with DDGS() as ddgs:
        results = ddgs.text(query)
        return [r['href'] for r in results][:num_results]
    
def search_web(query, num_results = 5):
    links = serpapi_search(query, num_results)
    if links:
        return links
    return duckduckgo_search(query, num_results)
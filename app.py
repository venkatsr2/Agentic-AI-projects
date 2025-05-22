from dotenv import load_dotenv
import os
load_dotenv()
open_api_key = os.getenv("OPEN_API_KEY")
serpapi_key = os.getenv("SERPAPI_KEY")

from agents.input_agent import clarify_query
from agents.search_agent import search_web
from agents.scrape_summary_agent import summarize_article
from agents.report_agent import genrate_report

def auto_research(user_query):
    print(f'User Query: {user_query}')

    refined_query = clarify_query(user_query)
    print(f'\nRefined Query: {refined_query}')

    links = search_web(refined_query)
    print('\nTop Links:')
    for i,link in enumerate(links):
        print(f'{i}. {link}')

    print('\nSummaries:\n')
    summaries = ""

    for idx,link in enumerate(links, start = 1):
        summary = summarize_article(link)
        if summary:
            print(f'{idx}. Summary from {link}:\n{summary}\n')
            summaries += f"\nSummary from {link}: \n{summary}\n"
        else:
            print(f'{idx}. Failed to summarize {link}.\n')

    report = genrate_report(refined_query, summaries)
    print("\nFinal Report: \n")
    print(report)


if __name__ == "__main__":
    query = input('Enter your research query: ')
    auto_research(query)
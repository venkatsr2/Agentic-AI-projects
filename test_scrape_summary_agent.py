from agents.scrape_summary_agent import summarize_article
url = 'https://www.nexford.edu/insights/how-will-ai-affect-jobs'
summary = summarize_article(url)

print('summary:\n', summary)
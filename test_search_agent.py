from agents.search_agent import search_web
query = 'How will advancements in artificial intelligence impact the demand for and nature of data-related jobs in the future?'
results = search_web(query)

for i,link in enumerate(results):
    print(f"{i}.{link}")
from agents.input_agent import clarify_query

user_query = 'How AI will affect data related jobs in future?'
refined = clarify_query(user_query)
print('refined query: ', refined)

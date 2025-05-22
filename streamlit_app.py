import streamlit as st
from agents.input_agent import clarify_query
from agents.search_agent import search_web
from agents.scrape_summary_agent import summarize_article
from agents.report_agent import genrate_report

st.set_page_config(page_title="AutoReasearcher", layout = 'wide')
st.title("AutoResearcher - Agentic AI Assistant")

query = st.text_input('Enter your research topic:', placeholder = 'e.g., Impact of Gen AI on Education')

if st.button("Run Research") and query:
    with st.spinner('Refining your query...'):
        refined_query = clarify_query(query)
        st.success('Refined Query:')
        st.write(refined_query)

    with st.spinner("Searching for relevant articles..."):
        links = search_web(refined_query)
        st.success(f'found {len(links)} relevant article(s).')
        for i,link in enumerate(links):
            print(f"{i}. [{link}]({link})")

    st.markdown("---")
    st.subheader("Summaries")
    summaries = ""

    for idx,link in enumerate(links, 1):
        with st.spinner(f"Summarizing article {idx}..."):
            summary = summarize_article(link)
            if summary:
                st.markdown(f"**Summary {idx}**")
                st.markdown(summary)
                summaries += f"\nSummary from {link}: \n{summary}\n"
            else:
                st.warning(f"Could not summarize article {idx}.")
        
    with st.spinner(f"Generating Final Report..."):
        report = genrate_report(refined_query, summaries)
        st.markdown("###Final Report")
        st.text_area("Generated Report:", value = report, height = 400)
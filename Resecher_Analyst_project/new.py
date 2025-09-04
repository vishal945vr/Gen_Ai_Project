import streamlit as st
import feedparser
import urllib.parse

st.title("📰 Google News for Companies")

company_name = st.text_input("Enter Company Name")

def get_google_news(company_name):
    query = urllib.parse.quote(company_name)
    url = f"https://news.google.com/rss/search?q={query}"
    feed = feedparser.parse(url)
    return feed.entries

if st.button("Get News"):
    with st.spinner("Fetching news..."):
        news = get_google_news(company_name)
        if news:
            for entry in news[:10]:  # Show top 10 news
                st.markdown(f"### [{entry.title}]({entry.link})")
                st.markdown(f"📅 {entry.published}")
                st.write("---")
        else:
            st.warning("No news found.")




#streamlit run c:\Users\vrooo\OneDrive\Desktop\Coding\venv\new.py
   

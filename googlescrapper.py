from itertools import count
from gurls.names import NAMES
from gnews import GNews
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

# def main(source:list):
#     interval = 1

#     url = []

#     for i in source:
#         links = f'https://news.google.com/{i[2:]}'
#         decoded_url = gnewsdecoder(links, interval=interval)
#         url.append(decoded_url['decoded_url'])

#     return url

def StartDate(months):
    days = months * 30
    start_date = datetime.today().date() - timedelta(days=days)
    return start_date

def MainRun():
    for i in range(len(NAMES)):
        st.markdown(f'**Scraping {NAMES[i]}**')
        # print(f'**Scraping {NAMES[i]}**')


        google_news = GNews(
            language='en',
            country='IN',
            start_date = StartDate(3),
            end_date=datetime.today().date()
        )

        TITLE = []
        LINKS = []
        PUBLISH_DATE = []

        response = google_news.get_news(NAMES[i])

        for i in response:
            TITLE.append(i['title'])
            PUBLISH_DATE.append(i['published date'])
            LINKS.append(i['url'])

        DATA = {'Headline' : TITLE,
                "publish Date": PUBLISH_DATE,
                'Links' : LINKS}

        st.dataframe(pd.DataFrame(DATA))
        # print(pd.DataFrame(DATA))


# if __name__ == "__main__":
#     MainRun(months=months)

# MainRun(months)

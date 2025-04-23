from urls import URLS
from paths import PATHS
from names import NAMES
import requests
from bs4 import BeautifulSoup
import pandas as pd
from googlenewsdecoder import gnewsdecoder
import streamlit as st

def main(source:list):
    st.markdown("Starting to clean the links")
    interval = 1

    url = []

    for i in source:
        st.markdown(i)
        links = f'https://news.google.com/{i[2:]}'
        decoded_url = gnewsdecoder(links, interval=interval)
        url.append(decoded_url['decoded_url'])

    return url


def fetchAndSaveToFile(url, path):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    r = requests.get(url, headers)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(r.text)


def clearFileContent(path):
    with open(path, 'w') as f:
        f.write(" ")


def MainRun():
    for i in range(len(URLS)):
        st.markdown(f'**Scraping {NAMES[i]}**')

        clearFileContent(PATHS[i])
        fetchAndSaveToFile(URLS[i], PATHS[i])

        st.markdown("After scrapping")

        file_path = PATHS[i]

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        st.markdown(
            'After reading scrapped data'
        )

        soup = BeautifulSoup(content)

        all_a_tags = soup.find_all('a')

        TITLE = []
        LINKS = []

        for j in all_a_tags:
            if j.get_text(strip=True):
                LINKS.append(j.get('href'))
                TITLE.append(j.text)

        st.markdown('After scapping links and texts')

        LINKS = main(LINKS[16:24])

        st.markdown("After cleaing links")

        DATA = {'Headline' : TITLE[16:24],
                'Links' : LINKS}

        st.dataframe(pd.DataFrame(DATA))


if __name__ == "__main__":
    MainRun()

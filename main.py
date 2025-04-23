from urls import URLS
from paths import PATHS
from names import NAMES
import requests
import pandas as pd
from googlenewsdecoder import gnewsdecoder
import streamlit as st
from stqdm import stqdm

def main(source:list):
    interval = 1

    url = []
    for i in stqdm(source):
        links = f'https://news.google.com/{i[2:]}'
        decoded_url = gnewsdecoder(links, interval=interval)
        url.append(decoded_url['decoded_url'])

    return url


def fetchAndSaveToFile(url, path):
    r = requests.get(url)
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

        file_path = PATHS[i]

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content)

        all_a_tags = soup.find_all('a')

        TITLE = []
        LINKS = []

        for j in all_a_tags:
            if j.get_text(strip=True):
                LINKS.append(j.get('href'))
                TITLE.append(j.text)

        LINKS = main(LINKS[16:24])

        DATA = {'Headline' : TITLE[16:24],
                'Links' : LINKS}

        trim_front = file_path[5:]
        file_name = trim_front[:-5]

        st.dataframe(pd.DataFrame(DATA))


if __name__ == "__main__":
    MainRun()

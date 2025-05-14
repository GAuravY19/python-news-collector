import requests
from datetime import datetime, timedelta
import streamlit as st

import pandas as pd

API_KEY = 'AIzaSyBUZmne5tIBHDs0BkaeHcbTiZNnECPonyM'


BAJAJ = 'UCJeZ0QNDYn48bx1ytiqKl4A'
CHOLA = 'UC86J9DiJmUmCX4yTZOOf0oA'
FUTURE = 'UCpAL2Ytdn4XdwUD-RalsXlg'
GODIGIT = 'UCm9FwBnApFhOp4xYG1sA8vg'
HDFC_ERGO = 'UCENvtDiiQ8LNvdBatZDIpwQ'
ICICI = 'UC05VfcUlVM7r3AZ4wjuslAA'
RELIANCE = 'UCGVeKdUiXCQ8Pi8vx0NUMlg'
ROYAL = 'UCIUtkK5kXjxB4CiavucdnXA'
SBI = 'UCmJqZPkDV39lYOK0q8FG7sA'
TATA = 'UCzz6b0_0QZfPnr8TP3Hv6ww'
ZUNO = 'UCfoDKfU5cD2dCpgywf20nmg'
CARE = 'UCeuWUBVK8UNOcEM0iJRLPTw'
MANIPAL = 'UC37bhMrd6tZI1nVNCUWj5Zg'
NIVA = 'UCW6uUMlk7QwNsZx9K8HjsWQ'
STAR = "UCLJux67EoAJ1qNe1JKErO8g"
DIITO = "UCyKj-yaTpbnWZY90ajxB8WQ"
POLICYBAZAAR = 'UC8aYNHtHDHLakP7H-5RaxQA'
POLICYX = "UCqhzVsnH1UqlxEtu4p9vM6g"

CHANNEL_ID = [BAJAJ, CHOLA, FUTURE, GODIGIT, HDFC_ERGO, ICICI, RELIANCE, ROYAL, SBI, TATA, ZUNO, CARE, MANIPAL, NIVA, STAR, DIITO, POLICYBAZAAR, POLICYX]

NAMES = ['Bajaj Allianz General Insurance', 'Chola MS', 'Future Generali', 'GO DIGIT', 'Hdfc Egro', 'Icici lombard', 'reliance general insurance',
         'royal sundaram', 'sbi general', 'tata aig', 'zuno general', 'care health insurance', 'mainpal cigna health insurance',
         'niva bupa health insurance', 'star health & allied', 'ditto insurance', 'policybazaar', 'policyx']




def main_youtube():

    for i in range(len(CHANNEL_ID)):

        VIDEO_TITLE = []
        VIDEO_DESC = []
        VIDEO_URL = []

        st.markdown(f'**Scrapping {NAMES[i]}**')

        url = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID[i]}&part=snippet,id&order=date&maxResults=50'

        response = requests.get(url)
        data = response.json()

        for item in data.get('items', []):

            if item['id']['kind'] == 'youtube#video':
                video_id = item['id']['videoId']
                video_url = f'https://www.youtube.com/watch?v={video_id}'

                dates = item['snippet']['publishedAt'][:10]
                dates = datetime.strptime(dates, '%Y-%m-%d')

                if dates < datetime.now() - timedelta(days=30):
                    break

                snippet = item['snippet']
                title = snippet['title']
                description = snippet['description']

                VIDEO_TITLE.append(title)
                VIDEO_URL.append(video_url)
                VIDEO_DESC.append(description)

        Data = {'Video Title' : VIDEO_TITLE,
                'Video URL' : VIDEO_URL,
                'Video Description' : VIDEO_DESC}

        st.dataframe(pd.DataFrame(Data))







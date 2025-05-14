from email import contentmanager
from bs4 import BeautifulSoup
import requests
from utils import fetchAndSaveToFile, clearFileContent

url = 'https://www.business-standard.com/search?q=hdfc%20ergo%20general%20insurance%20company'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com'
}
r = requests.get(url, headers=headers)

path = 'aditya.html'
fetchAndSaveToFile(url, path)

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content)


print(r.text)

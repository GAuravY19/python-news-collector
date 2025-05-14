import requests

url = 'https://www.business-standard.com/search?q=hdfc%20ergo%20general%20insurance%20company'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com'
}
r = requests.get(url, headers=headers)

print(r.text)

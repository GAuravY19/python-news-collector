import requests

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

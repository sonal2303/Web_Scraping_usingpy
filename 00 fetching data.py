import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

def fetchAndSaveToFile(url, path):
    r = requests.get(url, proxies=proxies)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/"

fetchAndSaveToFile(url, "data/times.html")
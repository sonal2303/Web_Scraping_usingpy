import requests
from bs4 import BeautifulSoup
import pandas as pd
proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

data = {"Title": [], "Price": []}


url = "https://www.amazon.in/s?k=iphone&crid=OADRDQV2ZWBT&sprefix=iphone%2Caps%2C384&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
titles = soup.select("h2 span")
Prices = soup.select("span.a-price")
for title in titles:
    text = title.get_text(strip=True)
    print(text)
    data["Title"].append(text)
    
for Price in Prices:
    if not("a-text-Price" in Price.get("class")):
        print(Price.find("span").get_text())
        data["Price"].append(Price.find("span").get_text())
        if len(data["Price"]) == len(data["Title"]):
            break
        
min_len = min(len(data["Title"]), len(data["Price"]))

data["Title"] = data["Title"][:min_len]
data["Price"] = data["Price"][:min_len]

df = pd.DataFrame(data)
        
df = pd.DataFrame.from_dict(data)  
df.to_csv("data.csv", index=False)    
print("Titles:", len(data["Title"]))
print("Prices:", len(data["Price"]))
        

        



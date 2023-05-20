import requests
from bs4 import BeautifulSoup

url = "https://sahan-dev.me/"
web = requests.get(url)

soup = BeautifulSoup(web.text, "html.parser")
result = soup.find("h1")

print(result.text)

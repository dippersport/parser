import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.techtarget.com/whatis/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")

definition_hrefs = []


for link in links:
  href = link.get("href")
  if href and "/definition" in href and "/definition" not in href:
    definition_hrefs.append(href)

for url in definition_hrefs:
  print(url)

df = pd.DataFrame(definition_hrefs, columns=["URL"])

df.to_csv("output.csv", index=False)
    
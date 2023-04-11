from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

result = doc.find("option")
print(result)
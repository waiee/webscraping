from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tag = doc.find("option")
# tag['value'] = 'false'
# tag['color'] = "blue"
# print(tag.attrs) #print in dict

# tag = doc.find_all(["p", "div", "li"]) #search multiple tags
tag = doc.find_all(["option"], text="Undergraduate", value="undergraduate")
print(tag)
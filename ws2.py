from bs4 import BeautifulSoup
import requests
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tag = doc.find("option")
# tag['value'] = 'false'
# tag['color'] = "blue"
# print(tag.attrs) #print in dict

# tag = doc.find_all(["p", "div", "li"]) #search multiple tags
# tag = doc.find_all(["option"], text="Undergraduate", value="undergraduate")
# tag = doc.find_all(class_="btn-item")

# tag = doc.find_all(text=re.compile("\$.*"), limit=1) #read dollar sign and its content
tag = doc.find_all("input", type="text")
for tag in tag:
    tag['placeholder'] = "i changed you mf" #change placeholder

#save new html file
with open("changed.html", "w") as file:
    file.write(str(doc))


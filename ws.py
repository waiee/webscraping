#Read HTML File
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#print doc with indentation
#print(doc.prettify())

#Print tag and modify title
# tag = doc.title
# tag.string = "hello"

#find all tag, accesss first tag
# tags = doc.find_all("p")[0]
# print(tags.find_all("b")) 
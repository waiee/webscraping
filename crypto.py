from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody #read whole body
trs = tbody.contents #table row

# print(trs[1].previous_sibling) #prev sibling
# print(list(trs[0].next_siblings)) #next sibling

# print(trs[0].parent.name) #parent name
# print(list(trs[0].descendants)) #everything inside tag

prices = {}
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

print(prices)
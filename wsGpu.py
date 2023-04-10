from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/biostar-geforce-rtx-3080/p/1FT-003G-00012?Item=9SIBGVBJG73546&Description=gpu&cm_re=gpu-_-9SIBGVBJG73546-_-Product&cm_sp=SP-_-1728307-_-0-_-2-_-9SIBGVBJG73546-_-gpu-_-gpu-_-1"
result = requests.get(url)
# print(result.text)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify)

prices = doc.find_all(text="$")
# print(prices)


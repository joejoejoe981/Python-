import requests
from bs4 import BeautifulSoup
import re

response = requests.get(url = 'https://pokemondb.net/pokedex/national')
html = response.text
soup = BeautifulSoup(html, "html.parser")

with open('001.pdf','wb') as f:
    f.write(response.content)
print('網站回應結果')
print('狀態碼', response.status_code)
print('資料類型',response.headers['content-type'])
print('資料編碼',response.encoding)



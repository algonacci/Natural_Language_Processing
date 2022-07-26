from urllib import response
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_House_of_Representatives'
table_id = 'votingmembers'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', id=table_id)

df = pd.read_html(str(table))
print(df[0])
df = df[0].to_excel('data.xlsx', index=False)
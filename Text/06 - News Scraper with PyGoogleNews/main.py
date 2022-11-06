from pygooglenews import GoogleNews
import re
import pandas as pd

def search_news_headlines(query):
    gn = GoogleNews(lang='id', country='id')
    search = gn.search(query)
    news_item = search['entries']

    for i in news_item:
        i['title'] = re.sub('-.*', '', i['title'])
        i['title'] = re.sub('[^a-zA-Z0-9 ]', '', i['title'])
        i['title'] = re.sub('com', '', i['title'])
        print(i['title'])
        print(i['link'])
        print('\n')
    
    df = pd.DataFrame({
        'title': [i['title'] for i in news_item],
        'link': [i['link'] for i in news_item]
    })

    df.to_csv('news_headlines.csv', index=False)

search_news_headlines('kampus merdeka')
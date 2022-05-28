from newsapi import NewsApiClient


import requests
import json

# Init
Api_key='0bf80e3a6a5d4fefb6b80ceeaccb9560'

Query= 'islam'

# Init
newsapi = NewsApiClient(api_key=Api_key)


# if top_headlines:
#     print(top_headlines)


 # /v2/top-headlines
def get_top_headlines(Api_key, Query):
    raw_response = requests.get(f'https://newsapi.org/v2/top-headlines?q={Query}&apiKey={Api_key}').text
    return raw_response
    

def top_headlines():
    response = get_top_headlines(Api_key, Query) 
    headlines =  json.loads(response)
    print(headlines)
    return headlines['articles']


# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2022-05-01',
                                      to='2017-05-12',
                                      language='en',
                                      sort_by='relevancy',
                                      #pageSize=20,
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()
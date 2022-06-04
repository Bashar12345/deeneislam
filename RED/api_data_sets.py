from newsapi import NewsApiClient
from datetime import datetime, timedelta, date

import requests
import json


# Init
newsapi_Api_key='0bf80e3a6a5d4fefb6b80ceeaccb9560'

newsdata_api_key='pub_780974afbcc3e79f25bab0e3992a50ffc4e2'

Query= 'muslims' #'islam,God,Allah','Religion'

# Init
newsapi = NewsApiClient(api_key=newsapi_Api_key)


date_form = date.today()
#print(date_form)
date_to = date_form - timedelta(days=10)
#print(date_form)
#print(date_to)

parameters = {
    'q': Query, # query phrase
    'pageSize': 28,  # maximum is 100
    'from':date_form,
    'to':date_to,
    'sortBy':'popularity',
    'apiKey': newsapi_Api_key # your own API key
}


def get_quran_translation_list():
    raw_response='https://quranenc.com/api/v1/translations/list'


def get_the_selected_sura(translation_auther,sura_no):
    raw_response=requests.get(f'https://quranenc.com/api/v1/translation/sura/english_saheeh/{sura_no}')



def get_selected_quran_surah_with_translation(translation_auther,sura_no,ayat):
    raw_response = requests.get(f'https://quranenc.com/api/v1/translation/aya/english_saheeh/{sura_no}/{ayat}') 
   

def qurans_bangla():
    raw_responsce='http://api.alquran.cloud/v1/quran'

#https://www.hadithapi.com/api/sahih-bukhari/chapters?apiKey=$2y$10$kjKW8PvRxeTN5TKbRSuaug8HbfPKgr3Qe6Fin6A9UiO4FwsIVfNu
#https://api.hadith.sutanlab.id/books/bukhari?range=1-150
def haddit():
    raw_responsce='https://api.hadith.sutanlab.id/books/bukhari?range=1-150'
    return 0



 # /v2/top-headlines
def get_top_headlines():
    #raw_response = requests.get(f'https://newsapi.org/v2/top-headlines?q={Query}&apiKey={Api_key}').text
    #raw_response = requests.get(f'https://newsapi.org/v2/top-headlines?q={Query}&apiKey={Api_key}')
    newsapi_raw_response = requests.get(f'https://newsapi.org/v2/everything?',parameters)
    '''https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2022-05-30&'
       'sortBy=popularity&'
       'apiKey=API_KEY'''
    #newsapi_raw_response = requests.get(f'https://newsapi.org/v2/everything?q={Query}&domains=bdnews24.com,propthomalo.com,somokal.com&apiKey={Api_key}')
    newsdata_raw_response = requests.get(f'https://newsdata.io/api/1/news?apikey={newsdata_api_key}&q=muslim')
    
    return newsapi_raw_response, newsdata_raw_response
    

def top_headlines():
    newsapi_raw_response, newsdata_raw_response = get_top_headlines() 
    #headlines =  json.loads(response)
    headlines =  newsapi_raw_response.json()
    #print(headlines)
    return headlines['articles']
# if top_headlines:
#     print(top_headlines)





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
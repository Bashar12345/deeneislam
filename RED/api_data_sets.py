from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='0bf80e3a6a5d4fefb6b80ceeaccb9560')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='islam',
                                          #sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

#print(top_headlines)


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
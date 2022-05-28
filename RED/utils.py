from datetime import datetime, timedelta, date
from RED import nasa_api
from RED.api_data_sets import top_headlines, sources, all_articles 
import json
import itertools  
from .models import articles


NasaApI_KEY='KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0'


def utils_of_index_page():
    # KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0
    res_dic =dict()
    today = date.today()
    today = today - timedelta(days=1)
    previous_date = today - timedelta(days=2)
    print(today)
    print(previous_date)

    nasa_api_response = nasa_api.get_data(NasaApI_KEY, today)
    #print("todays --",type(nasa_api_response))

    previous_nasa_api_response = nasa_api.get_data(NasaApI_KEY, previous_date)
    #print("\nprevious days --",previous_nasa_api_response['url'])
    
    #todays
    hd_photo = nasa_api.get_hdurl(nasa_api_response)    
    thumbnail_photo = nasa_api.get_url(nasa_api_response)   

    day = nasa_api.get_date(nasa_api_response)

    title = nasa_api.get_title(nasa_api_response)

    desc = nasa_api.get_explaination(nasa_api_response)

    todays_res_dic = {'hd_photo':hd_photo,'thumbnail_photo':thumbnail_photo,'date':day,'title':title,'desc':desc} 
    #print(todays_res_dic)

    #prevoius
    pre_hd_photo = nasa_api.get_hdurl(previous_nasa_api_response)    
    pre_thumbnail_photo = nasa_api.get_url(previous_nasa_api_response)   
    previous_day = nasa_api.get_date(previous_nasa_api_response)

    previous_title = nasa_api.get_title(previous_nasa_api_response)

    previous_desc = nasa_api.get_explaination(previous_nasa_api_response)

    previous_res_dic = {'hd_photo':pre_hd_photo,'thumbnail_photo':pre_thumbnail_photo,'date':previous_day,'title':previous_title,'desc':previous_desc} 
    #print(previous_res_dic)

    im_url = nasa_api.get_url(nasa_api_response)
    im_url_previous = nasa_api.get_url(previous_nasa_api_response)

    present_date = nasa_api.get_date(nasa_api_response)
    yesterday = nasa_api.get_date(previous_nasa_api_response)

    nasa_api.download_image(im_url, present_date)
    nasa_api.download_image(im_url_previous, yesterday)
    return todays_res_dic,previous_res_dic


def articles_objects_view_utils():
    #article_data = articles.objects.all()
    article_title_list={}
    for article_data in articles.objects.all() :
        print(article_data.title + '\n')
        article_title_list.append(article_data.title)
    print(article_title_list)
    return article_data

#  "articles": [
#         {
#             "source": {
#                 "id": "la-nacion",
#                 "name": "La Nacion"
#             },
#             "author": null,
#             "title": "La China Suárez denunció a Ángel de Brito por hostigamiento y recibió una tajante respuesta al aire - LA NACION",
#             "description": "La actriz denunció malos tratos por parte de la prensa del espectáculo; Yanina Latorre se sumó a las críticas y la desafió",
#             "url": "https://www.lanacion.com.ar/espectaculos/television/la-china-suarez-acuso-a-angel-de-brito-de-hostigamiento-y-recibio-una-tajante-respuesta-al-aire-nid25052022/",
#             "urlToImage": "https://resizer.glanacion.com/resizer/u-kJqonM5IvlrnVOsdffPxRhPZc=/768x0/filters:format(webp):quality(80)/cloudfront-us-east-1.images.arcpublishing.com/lanacionar/JWI2FMV2TRBKVDBCFFV7G4F7IY.jpg",
#             "publishedAt": "2022-05-25T04:36:00Z",
#             "content": "No es la primera vez que María Eugenia La China Suárez hace referencia al hostigamiento que siente por un sector de la prensa de espectáculos. En reiteradas oportunidades, la actriz destacó el ensaña… [+3579 chars]"
#         },




def news_page():
    articles = top_headlines()
    #articles = top_headlines['articles']

    source = []
    title =[] 
    description =[]
    url =[]
    urlToImage =[]
    publishedAt =[]
    content =[]

    #print(articles)

    for i in range(len(articles)):
        article = articles[i]
        source.append(article['source'])
        title.append(article['title']) 
        description.append(article['description']) 
        url.append(article['url']) 
        urlToImage.append(article['urlToImage']) 
        publishedAt.append(article['publishedAt']) 
    
    # for t in title:
    #     print(t)

    article_list = itertools.zip_longest(source, title, description, url, urlToImage, publishedAt, content)

    context ={'article_list':article_list}

    return context
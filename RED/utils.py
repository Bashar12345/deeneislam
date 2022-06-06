from datetime import datetime, timedelta, date
from RED import nasa_api
from RED.api_data_sets import top_headlines, sources, all_articles ,get_selected_quran_surah_with_translation
import json
import itertools  
from .models import articles


NasaApI_KEY='KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0'


def utils_of_index_page():
    # KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0
    res_dic =dict()
    ajker_din = date.today()
    today = ajker_din - timedelta(days=1)
    previous_date = ajker_din - timedelta(days=3)
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

    #todays_res_dic = {'thumbnail_photo':thumbnail_photo,'date':day,'title':title,'desc':desc} 
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

<<<<<<< HEAD
=======



sample_dict =  [
    
    { 'chapter_id': 1,
      'chapter_name': 'Macarena',
    #   'sura_no': 2,
    #   'chapter_name': 'Macarena',
      'fecha': datetime.date(2021, 3, 11),
      'debe': 500.0},
     {'sale_id': 14,
      'name': 'Macarena',
      'fecha': datetime.date(2021, 4, 11),
      'debe': 500.0},
     {'sale_id': 15,
      'name': 'Yamila',
      'fecha': datetime.date(2021, 4, 14),
      'debe': 2000.0}
    
    ]
encoded_json = json.dumps(sample_dict)
credit = Creditos1.objects.create(dict_info=encoded_json)

decoded_data = json.loads(credit.dict_info)
print(decoded_data[0]["name"])






def get_qurans_chapters():
    
    get_selected_quran_surah_with_translation()


>>>>>>> 41f7841baa0cddfd220c13ed03db6d6a9a2d7526
def news_page():
    #newsapi_articles,newsdata_articles = top_headlines()
    newsapi_articles = top_headlines()
    #articles = top_headlines['articles']

    source = []
    title =[] 
    description =[]
    url =[]
    urlToImage =[]
    publishedAt =[]
    content =[]

    #print(articles)

    for i in range(len(newsapi_articles)):
        article = newsapi_articles[i]
        source.append(article['source'])
        title.append(article['title']) 
        description.append(article['description']) 
        url.append(article['url']) 
        urlToImage.append(article['urlToImage']) 
        publishedAt.append(article['publishedAt']) 
    
    article_list = itertools.zip_longest(source, title, description, url, urlToImage, publishedAt, content)
    context = {'article_list':article_list}
    # for t in title:
    #     print(t)
<<<<<<< HEAD

    article_list = itertools.zip_longest(source, title, description, url, urlToImage, publishedAt, content)

    context ={'article_list':article_list}

    return context
=======
    return context
>>>>>>> 41f7841baa0cddfd220c13ed03db6d6a9a2d7526

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




sample_dict =  [
    
    {'sale_id': 14,
      'name': 'Macarena',
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
    get_selected_quran_surah_with_translation


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
    
    # for t in title:
    #     print(t)
    article_list = itertools.zip_longest(source, title, description, url, urlToImage, publishedAt, content)
    context = {'article_list':article_list}

    return context







# "results": [
    #     {
    #         "title": "Gyanvapi case: Muslim side to continue arguments today",
    #         "link": "https://www.orissapost.com/gyanvapi-case-muslim-side-to-continue-arguments-today/",
    #         "keywords": [
    #             "National",
    #             "Prime News",
    #             "Gyanvapi",
    #             "Gyanvapi mosque",
    #             "Muslims"
    #         ],
    #         "creator": [
    #             "Post News Network"
    #         ],
    #         "video_url": null,
    #         "description": "Varanasi: Advocates for the Anjuman Intezamia Masjid (AIM), the Muslim side in the Gyanvapi mosque dispute, will continue their arguments on Monday challenging the maintainability of case. “In the May 26 hearing, our team had explained how the claims and demands of the women plaintiffs cannot be allowed as they had not produced any evidence […]",
    #         "content": "Varanasi: Advocates for the Anjuman Intezamia Masjid (AIM), the Muslim side in the Gyanvapi mosque dispute, will continue their arguments on Monday challenging the maintainability of case. “In the May 26 hearing, our team had explained how the claims and demands of the women plaintiffs cannot be allowed as they had not produced any evidence in support of their petition while their averments in several paragraphs of their petition are contradictory,” AIM advocate Abhay Nath Yadav said. On May 26, the district judge had started hearing the case on the issue of its maintainability in compliance with the order of the Supreme Court. The plaintiffs’ lawyer Hari Shankar Jain said his team will be in court on Monday though he is not sure whether the arguments of AIM advocates would conclude, and they would get an opportunity to counter them. AIM advocates are also likely to mention how the Gyanvapi mosque is covered under the Protection of Places of Worship Act, 1991, besides other laws and orders of the Supreme Court. Plaintiffs Rakhi Singh of Delhi and Laxmi Devi, Sita Sahu, Manju Vyas and Rekha Pathak had filed the petition in the court of civil judge on August 18, 2021. On April 8, the court appointed an advocate commissioner for the survey and videography of the Gyanvapi mosque.",
    #         "pubDate": "2022-05-30 04:46:56",
    #         "image_url": "https://www.orissapost.com/wp-content/uploads/2022/05/Gyanvapi-287x300.jpg",
    #         "source_id": "orissapost",
    #         "country": [
    #             "india"
    #         ],
    #         "category": [
    #             "top"
    #         ],
    #         "language": "english"
    #     },


# news_api


# "articles": [
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
# ]
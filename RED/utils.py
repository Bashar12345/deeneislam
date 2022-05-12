from datetime import datetime, timedelta, date
from RED import nasa_api
import json

NasaApI_KEY='KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0'


def utils_of_index_page():
    # KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0
    res_dic =dict()
    today = date.today()
    #today = today - timedelta(days=1)
    previous_date = today - timedelta(days=1)
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

#import urllib.request
#from RED import app
from django.conf import settings
import requests
import json
import os
from PIL import Image
#import datetime

print(settings.BASE_DIR)


def get_data(api_key, d_date):
    # raw_response = requests.get(
    #     f'https://api.nasa.gov/planetary/apod?api_key={api_key}').text
    # response = json.loads(raw_response)

    raw_response = requests.get(
        f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={d_date}').text
    response = json.loads(raw_response)
    #print(raw_response)
    
    return response


def get_date(response):
    date = response['date']
    return date


def get_explaination(response):
    explaination = response['explanation']
    return explaination


def get_hdurl(response):
    hdurl = response['hdurl']
    return hdurl


def get_media_type(response):
    media_type = response['media_type']
    return media_type


def get_service_version(response):
    service_version = response['service_version']
    return service_version


def get_title(response):
    service_version = response['title']
    return service_version


def get_url(response):
    url = response['url']
    return url


def download_image(url, date):
    #print(app.root_path)
    if os.path.isfile(f'{settings.BASE_DIR}/static/temp/{date}.jpg') == False:
        raw_image = requests.get(url).content
        with open(f'{settings.BASE_DIR}/static/temp/{date}.jpg', 'wb') as file:
            file.write(raw_image)

    else:
        return FileExistsError


def convert_image(image_path):
    path_to_image = os.path.normpath(image_path)

    basename = os.path.basename(path_to_image)

    filename_no_extension = basename.split(".")[0]

    base_directory = os.path.dirname(path_to_image)

    image = Image.open(path_to_image)
    # image.save(f"{base_directory}/{filename_no_extension}.png")
    image.save(f"{settings.BASE_DIR}/static/image/{filename_no_extension}.png")


# #import pandas as pd
# #from IPython.display import Image, display

# #Initialize Nasa class by creating an object:
# k = "523p5hPYHGzafYGLCkqa54kKMTV2vbP0XcPxkcLm"
# nasa = nasapy.Nasa(key=k)

# #Get a list of dates:
# dates = pd.date_range(end='2020-08-15', periods=5)

# #Empty list to store dictionary keys and values:
# data = []

# #Getting all the data:
# for d in dates:
#     apod = nasa.picture_of_the_day(d, hd=True)

#     if apod['media_type'] == 'image':
#         if 'hdurl' in apod.keys():
#             data.append(
#                 {'date': apod['date'], 'title': apod['title'], 'hdurl': apod['hdurl']})


# #Path of the directory:
# image_dir = "AAA_Images_1"

# #Checking if the directory already exists?
# dir_res = os.path.exists(image_dir)

# #If it doesn't exist then make a new directory:
# if (dir_res == False):
#     os.makedirs(image_dir)

# #If it exist then print a statement:
# else:
#     print("Directory already exists!\n")


# #Retrieving the image:
# for img in data:

#     #Creating title for image:
#     title = img["date"]+"_" + \
#         img["title"].replace(" ", "_").replace(":", "_")+".jpg"

#     #Downloading the image:
#     urllib.request.urlretrieve(img['hdurl'], os.path.join(image_dir, title))

# #Get list of images:
# astro_images = os.listdir(image_dir)

# #Displaying an image:
# Image(os.path.join(image_dir, astro_images[0]))

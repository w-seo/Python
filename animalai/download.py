from setting import *
from pprint import pprint
from datetime import datetime
from flickrapi import FlickrAPI
from urllib.request import urlretrieve

import os
import sys
import time

if __name__== "__main__":

    # API
    key = API_ACCESS_KEY
    secret = API_SECRET_KEY

    wait_time = 1

    animal_name = sys.argv[1]
    savedir = IMAGE_SAVE_DIR + animal_name

    try :
        if not os.path.exists(savedir):
            os.mkdir(savedir)

        flickr = FlickrAPI(key, secret, format = 'parsed-json')

        result = flickr.photos.search(
            text = animal_name,
            per_page = 400,
            media = 'photos',
            sort = 'relevance',
            safe_search = 1,
            extras = 'url_q, licence'
        )

        photos = result['photos']

        for i, photo in enumerate(photos['photo']):

            #create timestamp
            savetimestamp = int(datetime.utcnow().timestamp() * 1000)

            url_q = photo['url_q']
            filepath = savedir + "/" + animal_name + "_"  + str(savetimestamp) + ".jpg"

            if os.path.exists(filepath):
                continue

            urlretrieve(url_q, filepath)
            time.sleep(wait_time)

    except Exception as e:
        print(e)

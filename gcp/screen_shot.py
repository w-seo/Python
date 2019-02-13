import argparse
import os, sys, glob, time
import requests
import subprocess
import logging

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from setting import *
from storage_test import *
from logging import getLogger, FileHandler, StreamHandler, Formatter

# Log file name initialize
logger = getLogger('Logging Test')

# Setting th log level
logger.setLevel(logging.DEBUG)

# Log file save path
file_handler = FileHandler(LOG_FILE_SAVE_PATH + 'exe_log_message.log')
file_handler.setLevel(logging.DEBUG)

# Log console output
stream_handler = StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# Log output format setting
handler_format = Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')

stream_handler.setFormatter(handler_format)
file_handler.setFormatter(handler_format)

# Logger handler set
#logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# Log output test
#logger.debug("Logging Test")

def url_exits_check(check_response):

   # Input url exits check
   try:
       if "text/html" in check_response.headers["content-type"]:
           logger.info(URL_EXIST_MESSAGE)
           return True

   except Exception as ex:
       logger.error(URL_EXIST_ERROR_MESSAGE)

   return False

def network_check():

   # Network check test url
   network_check_url = "https://www.google.co.jp"

   # Connection waiting time
   timeout = 2

   try:
       _ = requests.get(network_check_url, timeout=timeout)

       logger.info(NETWORK_CONNECT_MESSAGE)
       return True

   except requests.ConnectionError:
      logger.error(NETWORK_CONNECT_ERROR_MESSAGE)

   return False

def exist_mkdir_check(folder_path):

   #if the folder does not exist, it create a folder
   try:
       if os.path.isdir(folder_path) == False:
           logger.info(FILDER_EXIST_ERROR_MESSAGE)
           subprocess.call(['mkdir', folder_path])
           logger.info(FOLDER_CREATE_MESSAGE)

       logger.info(FOLDER_EXIST_MESSAGE)

   except Exception as ex:
       logger.error(FOLDER_CREATE_ERROR_MESSAGE)

def screen_shot(site_url):

   try:
       # Create timestamp
       savetimestamp = int(datetime.utcnow().timestamp() * 1000)

       options = Options()
       options.binary_location = '/usr/bin/google-chrome'
       # Display size free
       options.add_argument('--headless')
       # Chrome secret mode
       options.add_argument('--incognito')
       # Web site dialog skip
       options.add_argument('user-agent=Mozilla/5.0 (X11, Linux x86_64) AppleWebKit/537.21 (KHTML, like Gecko) scripts.py Safari/537.21')

       driver = webdriver.Chrome(chrome_options=options)
       driver.get(site_url)

       # Site loading waiting
       time.sleep(5)

       # Display full size
       #page_width = driver.execute_script('return document.body.scrollWidth')
       # Display full size
       #page_height = driver.execute_script('return document.body.scrollHeight')

       # Capture image size
       driver.set_window_size(WINDOW_WIDTH_SIZE, WINDOW_HEIGHT_SIZE)

       # Save path exist check
       exist_mkdir_check(folder_path=SAVE_IMG_PATH)

       # Image save path
       driver.save_screenshot(SAVE_IMG_PATH + str(savetimestamp) + '.png')

       logger.info(SCREEN_SHOT_SUCCESS_MESSAGE)

       # Web driver close
       driver.quit()

   except Exception as ex:
       logger.error(SCREEN_SHOT_FAIL_MESSAGE)

def storage_upload():

   try:
       # GCP Client exits check
       #if client_check() == True:
       client = storage_client_check()
       #print("Exist client")

       # Search image file and storage upload
       #img = "/home/so_p04323/test/image_shot/screenshot.png"

       # File exits check
       if os.path.exists(SAVE_IMG_PATH):
           for img in glob.glob(SAVE_IMG_PATH+'*.png'):
               storage_img_upload(storage_client=client, file_path=img, bucket_name=BUCKET_NAME)

   except Exception as ex:
       logger.error(ex)

if __name__=="__main__":

        parser = argparse.ArgumentParser(description="website screenshot")

        # Input web site url
        parser.add_argument('site_url', help='url')
        args = parser.parse_args()

        url = args.site_url

        try:
           # Call network_check method
           if network_check() == True:
               response = requests.get(url)

           # Call url_exits_check method
           if url_exits_check(check_response=response) == True:
               # Call screen_shot method
                screen_shot(site_url=url)

           # Blob upload image
           storage_upload()

        except Exception as ex:
           logger.error(ex)

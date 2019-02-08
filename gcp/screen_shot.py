import argparse
import os, sys, glob
import requests

#from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from setting import *
from storage_test import *

def url_exits_check(check_response):
   # Input url exits check
   try:
       if "text/html" in check_response.headers["content-type"]:
           return True
   except Exception as ex:
       print(ex)

   return False

def network_check():

   # Network check test url
   network_check_url = "https://www.google.co.jp"

   # Connection waiting time
   timeout = 2

   try:
       _ = requests.get(network_check_url, timeout=timeout)
       return True

   except requests.ConnectionError:
      print("Network do not Connection")

   return False

def screen_shot(site_url):

   try:
       #Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36

       options = Options()
       options.binary_location = '/usr/bin/google-chrome'
       options.add_argument('--headless')
       # Chrome secret mode
       options.add_argument('--incognito')
       # Locale setting = Japan
       options.add_experimental_option('prefs', {'intl.accept_languages': 'jp_JP'})

       driver = webdriver.Chrome(chrome_options=options)
       driver.get(site_url)

       # Display full size
       page_width = driver.execute_script('return document.body.scrollWidth')
       # Display full size
       page_height = driver.execute_script('return document.body.scrollHeight')

       # capture image size
       driver.set_window_size(page_width, page_height)
       # image save path
       driver.save_screenshot(SAVE_IMG_PATH + 'screenshot.png')

       # Web driver close
       driver.quit()
   except Exception as ex:
       print(ex)

def storage_upload():

   try:
       # GCP Client exits check
       #if client_check() == True:
       client = client_check()
       #print("Exist client")

       # Search image file and storage upload
       #img = "/home/so_p04323/test/image_shot/screenshot.png"
       for img in glob.glob(SAVE_IMG_PATH+'*.png'):
          #print(img)
          blob_upload(client=client, file_path=img, bucket_name=BUCKET_NAME)

   except Exception as ex:
       print(ex)

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
           print(ex)

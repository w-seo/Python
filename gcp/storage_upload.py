import os, sys
import logging

from google.cloud import storage, datastore, exceptions
from message import *
from logging import getLogger, FileHandler, StreamHandler, Formatter

# Log initialize
logger = getLogger("Logging Test")

def storage_client_check():

   try:
       # Storage check
       client = storage.Client()

       if client is not None:
           logger.info(STORAGE_CLIENT_EXIST_MESSAGE)
           return client

   except exceptions.NotFound:
       logger.error(STORAGE_CLIENT_EXIST_ERROR_MESSAGE)

   return False

def datastore_client_check():

   try:
       # Datastore check
       ds_client = datastore.Client()

       if ds_client is not None():
           logger.info(DATA_STORE_CLIENT_EXIST_MESSAGE)
           return ds_client

   except exceptions.NotFound:
       logger.error(DATA_STORE_CLIENT_EXIST_ERROR_MESSAGE)

def storage_bucket_check(storage_client, bucket_name):

   try:
       bucket = storage_client.get_bucket(bucket_name)
       logger.info(BUCKET_EXIST_MESSAGE)

       return bucket

   except exceptions.NotFound:
       logger.error(BUCKET_EXIST_ERROR_MESSAGE)

   return False

def create_bucket(storage_client, bucket_name):

   try:
       bucket = storage_client.create_bucket(bucket_name)
       logger.info(BUCKET_CREATE_MESSAGE)

       return bucket

   except exceptions.NotFound:
       logger.error(BUCKET_CREATE_ERROR_MESSAGE)

def storage_img_upload(storage_client, file_path, bucket_name):

   upload_file_name = []

   try:
       # Bucket check
       bucket = storage_bucket_check(storage_client, bucket_name)

       # if dose not eixst bucket, create bucket
       if bucket == False:
           bucket = create_bucket(storage_client, bucket_name)

       # From path filename get
       if file_path is not None:
           for name in file_path.split("/"):
              upload_file_name.append(name)

       # upload file name
       blob = bucket.blob(upload_file_name[5])

       # Upload file path
       blob.upload_from_filename(file_path)

       logger.info(BUCKET_UPLOAD_MESSAGE)
       logger.info("-----------------------------------------")

       os.remove(file_path)

   except exceptions.NotFound:
       logger.error(BUCKET_UPLOAD_ERROR_MESSAGE)

#if __name__=="__main__":

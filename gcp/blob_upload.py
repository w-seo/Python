import os, sys

from google.cloud import storage

def client_check():

   try:
       # Storage check
       client = storage.Client()

       if client is not None:
           return client
   except Exception as ex:
       print(ex)

   return False

def blob_upload(client, file_path, bucket_name):

   upload_file_name = []

   try:
       # GCP storage(Bucket) name
       bucket = client.get_bucket(bucket_name)

       # From path filename get
       if file_path is not None:
           for name in file_path.split("/"):
              upload_file_name.append(name)

       # upload file name
       blob = bucket.blob(upload_file_name[5])

       # Upload file path
       blob.upload_from_filename(file_path)

       os.remove(file_path)

   except gcloud.exceptions.GCloudError as e:
       print(e)

#if __name__=="__main__":

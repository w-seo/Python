# coding:utf-8
import os
import glob
import zipfile

def create_zip(FILE_NAME="sample01", IMAGE_FILE_PATH="./sample", IMAGE_ZIP_PATH="/images_zip"):
	try:
		with zipfile.ZipFile(IMAGE_ZIP_PATH + FILE_NAME + ".zip", "w", compression=zipfile.ZIP_DEFLATED) as new_zip:
			for dirname, subdirs, files in os.walk(IMAGE_FILE_PATH):
				for filename in files:
					new_zip.write(os.path.join(dirname, filename), arcname = filename)
	except Exception as e:
		print(e)

def image_unzip(FILE_NAME="sample01", IMAGE_ZIP_PATH="/images_zip", IMAGE_UNZIP_PATH="/images_unzip"):
	try :
		for item in glob.glob(IMAGE_ZIP_PATH + "\\" + FILE_NAME + "*.zip"):
			with zipfile.ZipFile(item) as existing_zip:
				existing_zip.extractall(IMAGE_UNZIP_PATH)

			return IMAGE_ZIP_PATH
	except Exception as e:
		print(e)

def image_unzip_file_check(FILE_NAME="sample01", IMAGE_UNZIP_PATH="/images_unzip"):
	try:
		image_list = []
		for item in glob.glob(IMAGE_UNZIP_PATH + "\\*.png"):
			image_list.append(item)
		image_list.sort()

		return image_list
	except Exception as e:
		print(e)

def image_delete(IMAGE_UNZIP_PATH="/images_unzip"):
	try:
		os.remove(IMAGE_UNZIP_PATH)
	except Exception as e:
		print(e)
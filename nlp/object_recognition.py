# coding : utf-8
import cv2
import argparse
import numpy as np

from PIL import Image
from setting import *
from utils import pdf_to_image, utils_zip, create_config

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='PDF To Images Test')
	parser.add_argument("pdf_file_path", default=PDF_FILE_PATH+FILE_NAME, nargs='?', help='Input the images')

	args = parser.parse_args()

	try:
		file_name = FILE_NAME.split(".")
		file_name = file_name[0]

		# 対象のPDFファイルを画像に変換
		pdf_to_image.pdf2images(FILE_NAME=file_name, PDF_FILE_PATH=args.pdf_file_path, IMG_FILE_PATH=IMAGE_FILE_PATH)

		# IMGで変換されたファイルをZIPファイルとして保存
		utils_zip.create_zip(FILE_NAME=file_name, IMAGE_FILE_PATH=IMAGE_FILE_PATH, IMAGE_ZIP_PATH=IMG_ZIP_PATH)

		# ファイルの情報をCONFIGファイルとして保存
		create_config.create_json(FILE_NAME=file_name, JSON_CONFIG_PATH=JSON_CONFIG_FILE_PATH, IMAGE_ZIP_PATH=IMG_ZIP_PATH, IMAGE_UNZIP_PATH=IMG_UNZIP_PATH)

	except Exception as e:
		print(e)
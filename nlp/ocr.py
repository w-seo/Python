# coding:UTF-8
import sys
import cv2
import json
import argparse
import sys
import csv
import pyocr
import pyocr.builders
import pandas as pd

from PIL import Image
from setting import *
from utils import utils_zip

if __name__ == "__main__":
	# setting OCR Parameter
	parser = argparse.ArgumentParser(description='tesseract oct test')
	parser.add_argument("image_json_config", default=JSON_CONFIG_FILE_PATH +JSON_CONFIG_FILE_NAME,
		nargs='?', help='read image json config file')
	
	args = parser.parse_args()
	tools = pyocr.get_available_tools()

	try : 
		# jsonファイルから物体認識された結果のデータを読み込み
		with(open(args.image_json_config, 'r')) as json_config:
			json_data = json.load(json_config)

		# 処理の対象のファイル名
		FILE_NAME = json_data["file_info"].get("file_name", "sample")
		# ファイルをイメージ化してzip形式に変換したデータ
		IMAGE_ZIP_PATH = json_data["read_data"].get("image_zip_path", "sample")
		IMAGE_UNZIP_PATH = json_data["read_data"].get("image_unzip_path", "sample")

		image_zip_array = []
		# イメージのzipファイルを解凍
		image_zip_array.append(utils_zip.image_unzip(FILE_NAME=FILE_NAME, IMAGE_ZIP_PATH=IMAGE_ZIP_PATH, IMAGE_UNZIP_PATH=IMAGE_UNZIP_PATH))
		# zipファイルが存在しないまま既に画像ファイルが存在する時
		# image_unzip_array = ["1"]

		if len(image_zip_array) >= 1:
			# unzipファイルの中身を確認
			image_file_array = utils_zip.image_unzip_file_check(FILE_NAME=FILE_NAME, IMAGE_UNZIP_PATH=IMAGE_UNZIP_PATH)

		for item in image_file_array:
			if len(tools) == 0:
				print("no OCR tool found")
				sys.exit(1)

			tool = tools[0]
			print("Will use tool '%s'" % (tool.get_name()))

			langs = tool.get_available_languages()
			print("Available languages: %s" % ", ".join(langs))
			lang = langs[2]
			print("Will use lang '%s'" % (lang))

			txt = tool.image_to_string(
				Image.open(item),
				lang="jpn",
				builder=pyocr.builders.TextBuilder(tesseract_layout=6)
			)

			df = pd.DataFrame([[txt]], columns = ["word"])
			df.to_csv(OCR_CSV_FILE_PATH + FILE_NAME + ".csv", encoding="cp932", mode="a", header=False, index=False)

		# utils_zip.image_delete(IMAGE_UNZIP_PATH=IMAGE_UNZIP_PATH)

	except Exception as e:
		print(e)
# coding:UTF-8
import sys
import cv2
import glob
import json
import argparse
import csv

from setting import *
from pipeline import *

if __name__ == "__main__":
	# setting OCR Parameter
	parser = argparse.ArgumentParser(description='tesseract oct test')
	parser.add_argument("ocr_read_file_name", default=OCR_CSV_FILE_PATH, 
		nargs='?', help='read in ocr_csc_file')
	parser.add_argument("image_json_config", default=JSON_CONFIG_FILE_PATH + JSON_CONFIG_FILE_NAME,
		nargs='?', help='read image json config file')
	
	args = parser.parse_args()

	try :
		# jsonファイルから物体認識された結果のデータを読み込み
		with(open(args.image_json_config, 'r')) as json_config:
			json_data = json.load(json_config)

		# 処理の対象のファイル名
		FILE_NAME = json_data["file_info"].get("file_name", "sample")

		for item in glob.glob(args.ocr_read_file_name + "\\*.csv"):
			# csvファイルから文章を読み込み
			with(open(item, 'r')) as csv_read_file:
				OCR_CSV_FILE_READER = csv_read_file.read()

			pipeline_parse = parse(OCR_CSV_FILE_READER)
			word = pipeline_parse.sentense_parse()

			pipeline_csvfile = csvfile(NLP_RESULT_CSV_FILE_PATH + FILE_NAME + ".csv", word)
			pipeline_csvfile.create_csvfile()

			# pipeline_parts = parts_of_word(args.ocr_write_file_name, word)
			# pipeline_parts.devide_word()

	except Exception as e:
		print(e)
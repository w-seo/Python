# coding:utf-8
import os
import json

def create_json(FILE_NAME="json_sample", JSON_CONFIG_PATH="./json_config", IMAGE_ZIP_PATH="./sample", IMAGE_UNZIP_PATH="sample"):
	pdf_info = {}

	pdf_info["file_info"] = {"file_name":FILE_NAME}
	pdf_info["read_data"] = {"image_zip_path":IMAGE_ZIP_PATH, "image_unzip_path":IMAGE_UNZIP_PATH}

	fw = open(JSON_CONFIG_PATH + "json_config_" + FILE_NAME + ".json", 'w')
	# json.dump関数でファイルに書き込む
	json.dump(pdf_info, fw, indent=4)


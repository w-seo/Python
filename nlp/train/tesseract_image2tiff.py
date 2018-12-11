import os
import re
import sys

from PIL import Image
from tesseract_train_setting import *

def image_to_tiff(FILE_NAME="sample"):
	try:
		# ファイルの存在チェック
		flag = os.path.exists(FILE_NAME)

		# ファイルオープン
		img = Image.open(FILE_NAME, "r")
		img.save(TIFF_IMAGE_FILE_PATH + TRAIN_TIFF_IMAGE_FILE_NAME + ".exp0" + ".tif", 'tiff')

	except Exception as e:
		print(e)
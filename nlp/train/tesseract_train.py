import argparse

from tesseract_train_setting import *
from tesseract_image2tiff import image_to_tiff
from tesseract_tiff2box import extract_digits_and_symbols

if __name__ == "__main__":

	# setting train_image Parameter
	parser = argparse.ArgumentParser(description='Tesseract Train Test')
	parser.add_argument("train_image", default=TRAIN_IMAGE_FILE_PATH,
		nargs='?', help='Train_image Transformation')
	
	args = parser.parse_args()

	TIFF_IMAGE_FILE_NAME = args.train_image

	# image_to_tiff(FILE_NAME=TIFF_IMAGE_FILE_NAME)

	extract_digits_and_symbols(FILE_NAME=TIFF_IMAGE_FILE_PATH)
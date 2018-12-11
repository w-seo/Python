from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes

def pdf2images(FILE_NAME = "sample", PDF_FILE_PATH="./sample", IMG_FILE_PATH="./sample"):
	images = convert_from_path(PDF_FILE_PATH)

	i = 0

	for item in images:
		images[i].save(IMG_FILE_PATH + FILE_NAME + "_" + str(i) + ".png", 'png')
		i += 1
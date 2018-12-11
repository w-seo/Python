# USAGE
# python tesseract_tiff2box.py --image example_check.png --reference tesseract_tiff.tif

# import the necessary packages
import cv2
import numpy as np
import argparse
import imutils

from imutils import contours
from tesseract_train_setting import *
from skimage.segmentation import clear_border

def extract_digits_and_symbols(FILE_NAME = "sample"):

	# setting train_image Parameter
	parser = argparse.ArgumentParser(description='Tesseract Train Test')
	parser.add_argument("tiff_image", default=FILE_NAME,
		nargs='?', help='Train_image Transformation')
	
	args = parser.parse_args()

	# initialize the list of reference character names, in the same
	# order as they appear in the reference image where the digits
	# their names and:
	# T = Transit (delimit bank branch routing transit #)
	# U = On-us (delimit customer account number)
	# A = Amount (delimit transaction amount)
	# D = Dash (delimit parts of numbers, such as routing or account)
	charNames = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
		"T", "U", "A", "D"]

	# load the reference MICR image from disk, convert it to grayscale,
	# and threshold it, such that the digits appear as *white* on a
	# *black* background
	ref = cv2.imread(args.tiff_image)
	ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
	ref = imutils.resize(ref, width=3300, height=2500)
	ref = cv2.threshold(ref, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
	# ref = cv2.threshold(ref, 0, 255, cv2.THRESH_BINARY_INV / cv2.THRESH_OTSU)[1]


	# find contours in the MICR image (i.e,. the outlines of the
	# characters) and sort them from left to right
	refCnts = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	refCnts = refCnts[0] if imutils.is_cv2() else refCnts[1]
	refCnts = contours.sort_contours(refCnts, method="left-to-right")[0]

	# create a clone of the original image so we can draw on it
	clone = np.dstack([ref.copy()] * 3)

	i = 0

	box_data = []

	try:
		# loop over the (sorted) contours
		for c in refCnts:
			# compute the bounding box of the contour and draw it on our
			# image
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 255, 0), 2)

			roi = clone[y:y+h, x:x+w]

			cv2.imwrite(ROI_IMAGE_FILE_PATH + str(i) + ".jpg", roi)
			i += 1

			box_data.append([x, y, x+w, y+h])

		print("finish!!!")

		# show the output of applying the simple contour method
		cv2.imshow("Simple Method", clone)
		cv2.waitKey(0)
	except Exception as e:
		print(e)
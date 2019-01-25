# coding: utf-8

from PIL import Image
from sklearn import model_selection
from setting import *

import os, glob
import numpy as np

# classes = ["bear", "hippopotamus", "zebra"]
classes = ["cats", "lion", "bear"]
num_classes = len(classes)
image_size = 50
#num_testdata = 100

X = []
Y = []

#X_train = []
#X_test = []
#Y_train = []
#Y_test = []

for index, class_name in enumerate(classes):
    photos_dir = IMAGE_SAVE_DIR + class_name

    files = glob.glob(photos_dir + "/" + "*.jpg")

    for i, file in enumerate(files):
        if i > 400:
            break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)

        X.append(data)
        Y.append(index)

        #if i < num_testdata:
        #    X_test.append(data)
        #    Y_test.append(index)
        #else:
        #    for angle in range(-20, 20, 5):
        #        img_r = image.rotate(angle)
        #        data = np.asarray(img_r)
        #        X_train.append(data)
        #        Y_train.append(index)

        #        img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
        #        data = np.asarray(img_trans)

        #        X_train.append(data)
        #        X_train.append(index)

X = np.array(X)
Y = np.array(Y)

#X_train = np.array(X_train)
#X_test = np.array(X_test)
#y_train = np.array(Y_train)
#y_test = np.array(Y_test)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save(NPY_SAVE_DIR + "cat_lion.npy", xy)

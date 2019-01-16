from PIL import Image
from sklearn import model_selection
from setting import *

import os, glob
import numpy as np

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

# 画像の読み込み
X = []
Y = []

for index, class_name in enumerate(classes):
    photos_dir = IMAGE_SAVE_DIR + "\\" + class_name
    files = glob.glob(photos_dir + "*.jpg")

    for i, file in enumerate(files):
        if i > 400:
            break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(image)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save(IMAGE_SAVE_DIR + "animal.npy", xy)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 10:41:12 2019

@author: jaisi8631
"""

# imports
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.optimizers import SGD
import argparse
import imutils
import cv2
import os


# image constraints
img_width, img_height = 128, 128


# argument parser for path to test image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default = "test.jpg",
                help="path to test x-ray image")
args = vars(ap.parse_args())


# load and compile model
model = load_model('model.h5')
model.compile(loss = "binary_crossentropy", 
              optimizer = SGD(lr=0.001, momentum=0.9), 
              metrics=["accuracy"])


# preprocess image
image = cv2.imread(args["image"])
image = cv2.resize(image, (img_width, img_height))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis = 0)


# generate prediction
result = model.predict(image)
pred = np.argmax(result, axis=1)
prediction = "UNRECOGNIZABLE"
if(pred[0] == 0):
    prediction = "Normal"
else:
    prediction = "Pneumonia"


# return result
print("The prediction is: " + prediction)
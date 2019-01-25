#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 03:46:58 2018

@author: laiunce
"""

import cv2
import numpy as np
import pytesseract
from PIL import Image


#tesseract_cmd = '/Users/laiunce/anaconda/lib/python3.6/site-packages/'
#pytesseract.tesseract_cmd =  tesseract_cmd+'tesseract_ocr.cpython-36m-darwin.so'


# Path of working folder on Disk
src_path = '/Users/laiunce/Desktop/image_detection/images/'

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)


    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    print('a')
    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)


    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
    print('b')

    # Remove template file
    #os.remove(temp)

    return result



print (get_string(src_path + "q.png"))



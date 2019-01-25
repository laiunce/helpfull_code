#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 21:13:34 2019

@author: crilaiun
"""
#source activate retinanet

from imageai.Detection import VideoObjectDetection
import os
import cv2
import time
from imageai.Detection import ObjectDetection

#esta lina porque sino pincha a veces ver bien luego
os.environ['KMP_DUPLICATE_LIB_OK']='True'

camera = cv2.VideoCapture(0)


execution_path = os.getcwd()


camera = cv2.VideoCapture(0)


detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
custom_objects = detector.CustomObjects(person=True, car=True)

#detections = detector.detectCustomObjectsFromImage(input_image='tpm/origen0.png', output_image_path= 'tpm/opencv0.png', custom_objects=custom_objects, minimum_percentage_probability=70)


for i in range(4):
    return_value, image = camera.read()
    cv2.imwrite('tpm/origen'+str(i)+'.png', image)
    detections = detector.detectCustomObjectsFromImage(input_image='tpm/origen'+str(i)+'.png', output_image_path= 'tpm/opencv'+str(i)+'.png', custom_objects=custom_objects, minimum_percentage_probability=70)
    if len(detections)>0:
        cv2.imwrite('tpm/detect/'+str(i)+'.png', image)
    #cv2.imwrite('tpm/opencv'+str(i)+'.png', image)
    #time.sleep(1)
    
del(camera)


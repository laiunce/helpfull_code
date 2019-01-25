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
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def box_cuadrantes(box):

    x=1280
    y=720
    #le resto 1 para que no llegue al tope maximo del x o y sino quedaria fuera del cuadrante.
    point1 = Point(box[0]-1, box[1]-1)
    point2 = Point(box[2]-1, box[3]-1)
    point3 = Point(box[0]-1, box[3]-1)
    point4 = Point(box[2]-1, box[1]-1)
    
    lista_cuadrantes = []
    
    #son coordenadas x,y
    
    #abajo izquierda
    #abajo derecha
    #arriba derecha
    #arriba izquierda
    
    cuadrante1 = Polygon([(0, y/2), (x/2, y/2), (x/2, 0), (0, 0)])
    cuadrante2 = Polygon([(x/2, y/2), (x, y/2), (x, 0), (x/2, 0)])
    cuadrante3 = Polygon([(0, y), (x/2, y), (x/2, y/2), (0, y/2)])
    cuadrante4 = Polygon([(x/2, y), (x, y), (x, y/2), (x/2, y/2)])
    
    if cuadrante1.contains(point1) or cuadrante1.contains(point2) or cuadrante1.contains(point3) or cuadrante1.contains(point4):
        lista_cuadrantes.append('cuadrante1')
    if cuadrante2.contains(point1) or cuadrante2.contains(point2) or cuadrante2.contains(point3) or cuadrante2.contains(point4):
        lista_cuadrantes.append('cuadrante2')
    if cuadrante3.contains(point1) or cuadrante3.contains(point2) or cuadrante3.contains(point3) or cuadrante3.contains(point4):
        lista_cuadrantes.append('cuadrante3')
    if cuadrante4.contains(point1) or cuadrante4.contains(point2) or cuadrante4.contains(point3) or cuadrante4.contains(point4):
        lista_cuadrantes.append('cuadrante4')        
        
    return lista_cuadrantes


#esta lina porque sino pincha a veces ver bien luego
os.environ['KMP_DUPLICATE_LIB_OK']='True'

camera = cv2.VideoCapture(0)


execution_path = os.getcwd()



import os
from imageai.Detection import ObjectDetection
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()


camera = cv2.VideoCapture(0)

for i in range(10):
    return_value, image = camera.read()
    cv2.imwrite('tpm/origen'+str(i)+'.png', image)    
    detections = detector.detectObjectsFromImage(input_image='tpm/origen'+str(i)+'.png', output_image_path= 'tpm/opencv'+str(i)+'.png', minimum_percentage_probability=70)

    #cv2.imwrite('tpm/opencv'+str(i)+'.png', image)
    #time.sleep(1)
    if len(detections)>0:
        
        for eachObject in detections:
            print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
            if eachObject["name"] == 'person':
                box = eachObject["box_points"]  
                print(box_cuadrantes(box))
                
                cv2.imwrite('tpm/detect/'+str(i)+'_'.join(list(box_cuadrantes(box)))+'.png', image)        
    
del(camera)






     






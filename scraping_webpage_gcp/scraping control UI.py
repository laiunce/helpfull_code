#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:47:34 2018

@author: laiunce
"""

import time
from selenium import webdriver
import pyautogui


driver = webdriver.Chrome('/Users/laiunce/anaconda/selenium/webdriver/chromedriver')
pagina = 'http://www.bcra.gob.ar/BCRAyVos/Situacion_Crediticia.asp'
driver.get(pagina)
time.sleep(2)
pyautogui.moveTo(192, 692,2)
pyautogui.click()
element = driver.find_element_by_name("CUIT")


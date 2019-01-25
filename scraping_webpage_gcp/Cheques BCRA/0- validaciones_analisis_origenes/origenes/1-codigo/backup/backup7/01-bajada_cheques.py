# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import webbrowser
import zipfile
import pandas as pd
import os

url = 'http://www.bcra.gov.ar/cheques/actualiza.asp'
page_ext = requests.get(url)
soup_ext = BeautifulSoup(page_ext.content)
p = (soup_ext.findAll("tr"))

tmp = re.findall(r"onmousedown", str(p))

texto=[]
for i in p:
    texto.append(str(p)) 
    

tmp = re.findall(r"zips\/cheques\/\d\d\d\d\d\d\d\d.zip", str(soup_ext))

#webbrowser.open('www.bcra.gov.ar/zips/cheques/20170613.zip',autoraise=True)


path= 'C:\\Users\\LAC40641\\Downloads\\'

#establecer a google chrome como predeterminado
for i in tmp:
    webbrowser.open('www.bcra.gov.ar/'+i,autoraise=True)


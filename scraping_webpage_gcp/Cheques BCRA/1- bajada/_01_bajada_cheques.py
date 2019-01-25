# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import webbrowser
import pyodbc
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import webbrowser
import zipfile
import pandas as pd
import os
import pyodbc


#trae maxima fecha en DW
con = pyodbc.connect('DRIVER={SQL Server};SERVER=srappw021p000.terceros.banco.com.ar\HST1;DATABASE=DAM;TRUSTED_CONNECTION=yes;pwd=[windows_pass]')
cur = con.cursor()
db_cmd = "select max(anio_mes_dia) from claiun_bcra_cheques_bajada_201601_2017"
res = cur.execute(db_cmd)

max_fecha= 99999999
for r in res:
    max_fecha= (r[0])
    

print('scraping BCRA')
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

#establecer a google chrome como predeterminado
for i in tmp:
    if int(i[-12:-4]) > max_fecha:
        webbrowser.open('www.bcra.gov.ar/'+i,autoraise=True)



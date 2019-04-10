
Conversación abierta. 6 mensajes. Todos los mensajes leídos.

Ir al contenido
Uso de Gmail con lectores de pantalla
in:sent rios 

2 de unas 57
scraping deptos
Recibidos
x

Laiun Cristian Ezequiel <laiun.ce@gmail.com>
Archivos adjuntos
sáb., 9 jun. 2018 18:36
para Leandro

Peli te adjunto el excel resultado, todos los barrios te deje el link a la publicacion. Donde no hay datos es porque el usuario no puso nada.

abrazoo
Zona de los archivos adjuntos

Laiun Cristian Ezequiel <laiun.ce@gmail.com>
Archivos adjuntos
sáb., 9 jun. 2018 18:44
para Leandro

codigo

Zona de los archivos adjuntos

Leandro Martín Ríos
lun., 11 jun. 2018 23:38
Geniooo graciasMe pasas la nueva búsqueda please HugLea

Laiun Cristian Ezequiel <laiun.ce@gmail.com>
Archivos adjuntos
mar., 12 jun. 2018 0:23
para Leandro

1, 2 y 3 ambientes peli

abrazo! avisame cualquier cosa.

Zona de los archivos adjuntos

Laiun Cristian Ezequiel <laiun.ce@gmail.com>
mar., 12 jun. 2018 0:37
para Leandro

vos haceme acordar por las dudas, pero este script lo vamos a correr todos los dias para detectar gente que le esta bajando el precio a los deptos cosa de saber que se le puede pedir menos.


Leandro Martín Ríos <rios.leandromartin@gmail.com>
dom., 3 feb. 11:49
para mí

Cabezón, podremos volver a correr el script de solodueños para buscar dptos 1 2 y 3 ambientes?
Estamos con la compra del dpto de flor

Hoy voy a estudiar y acomodar mi dataset de imágenes Para la tesis 

Chiflame si querés 

Abrazo grande 
Pelli 

¡OK!Sí, dale.No creo.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:57:40 2018

@author: laiunce
"""

#http://selenium-python.readthedocs.io/locating-elements.html




from selenium import webdriver
import re
import requests
import pandas as pd
import bs4
import time


#Por cada pagina
def obtiene_datos(i,driver):
    
    driver.get(i)
    
    direccion = ''
    venta = ''
    barrio = ''
    nom_duenio = ''
    telefono = ''
    cant_ambietes = ''
    metros_cubiertos = ''
    expensas = ''
    antiguedad = ''
    dormitorios = ''
    ascensores = ''
    deptos_por_piso = ''
    impuestos_anuales = ''  
    #Precio venta
    try:
        element =driver.find_element_by_xpath('//*[@style="width:300PX; float:right; font-family:Segoe, \'Segoe UI\', \'DejaVu Sans\', \'Trebuchet MS\', Verdana, sans-serif; font-size:13px; font-weight:bold; margin-top:5px; margin-right:10px"]')
        patt = re.compile(r'[^\d]')
        venta = patt.sub('', element.text)
    except:
        pass
    
    try:    
        #Direccion
        element =driver.find_element_by_xpath('//*[@style="float:left; font-family:Segoe, \'Segoe UI\', \'DejaVu Sans\', \'Trebuchet MS\', Verdana, sans-serif; font-size:13px; font-weight:bold; line-height:2.2; overflow:hidden; height:inherit; width:500px"]')
        direccion= element.text
    except:
      pass
        
    try:       
        #Barrio
        element =driver.find_element_by_xpath('//*[@style="float:left; width:240PX; font-family:Segoe, \'Segoe UI\', \'DejaVu Sans\', \'Trebuchet MS\', Verdana, sans-serif; font-size:13px; font-weight:bold; margin-top:5px; color:#AE000D"]')
        barrio= element.text
    except:
      pass
        
    try:      
        #NombreDueño
        element =driver.find_element_by_xpath('//*[@style="font-family:Segoe, \'Segoe UI\', \'DejaVu Sans\', \'Trebuchet MS\', Verdana, sans-serif; font-weight:bold; font-size:13px; color:#AE000D; padding:5px; overflow:hidden"]')
        nom_duenio= element.text
    except:
      pass
        
    try:  
        #Telefono
        element =driver.find_element_by_xpath('//*[@style="font-family:Segoe, \'Segoe UI\', \'DejaVu Sans\', \'Trebuchet MS\', Verdana, sans-serif; font-weight:bold; font-size:12px; padding-left:5px; padding-right:5px; overflow:hidden; -webkit-text-fill-color: #000000; color:#000000"]')
        telefono= element.text
    except:
      pass
        
    try:  
        #Obtiene otros datos
        element =driver.find_element_by_xpath('//*[@name="datos-ficha"]')
        texto=element.text
    except:
      pass
        
    try:  
        #cantidad_ambientes
        patt = re.compile(r'(?<=Ambientes: )(.*)(?= Ba)')
        cant_ambietes = patt.search(texto).group(1)
    except:
      pass
        
    try:  
        #metros_cubiertos
        patt = re.compile(r'(?<=Sup. cubierta total: )(.*)(?= m2)')
        metros_cubiertos = patt.search(texto).group(1)
    except:
      pass
        
    try:  
        #Expensas
        patt = re.compile(r'(?<=Expensas: \$ )(.*)')
        expensas = patt.search(texto).group(1)
    except:
      pass
        
    try:  
        #Antiguedad
        patt = re.compile(r'(?<=Antigüedad: )(.*)(?= Ubicación)')
        antiguedad = patt.search(texto).group(1)
    except:
      pass
        
    try:  
        #Dormitorios
        patt = re.compile(r'(?<=Dormitorios: )(.*)(?= Cantidad de ascensores:)')
        dormitorios = patt.search(texto).group(1)
    except:
      pass
        
    try:  
        #Ascensores
        patt = re.compile(r'(?<=Cantidad de ascensores: )(.*)')
        ascensores = patt.search(texto).group(1)
    except:
      pass
        
    try:  
        #Deptos por piso
        patt = re.compile(r'(?<=Deptos. por piso: )(.*)')
        deptos_por_piso = patt.search(texto).group(1)
    except:
      pass
        
    try:  
        #Impuestos Anuales
        patt = re.compile(r'(?<=Impuestos Anuales: \$ )(.*)')
        impuestos_anuales = patt.search(texto).group(1)
    except:
      pass  
      
    
    row = {
           'link':i,
           'direccion':direccion,
           'precio_venta':venta,
         'barrio' : barrio,
         'nom_duenio' : nom_duenio,
         'telefono' : telefono,
         'cant_ambietes' : cant_ambietes,
         'metros_cubiertos' : metros_cubiertos,
         'expensas' : expensas,
         'antiguedad' : antiguedad,
         'dormitorios' : dormitorios,
         'ascensores' : ascensores,
         'deptos_por_piso' : deptos_por_piso,
         'impuestos_anuales' : impuestos_anuales
           }
        
    return(row)
      
      




driver = webdriver.Chrome('/Users/laiunce/anaconda/selenium/webdriver/chromedriver')



lista_datos=[]


########### PAGINA 1
pagina = 'https://soloduenos.com/buscar.asp'
driver.get(pagina)

#pagina principal
element =driver.find_element_by_xpath('//*[@id="image3"]')
element.click()
      
print('1')    
########### PAGINA 2  
#Depto
element =driver.find_element_by_xpath('//*[@type="checkbox" and @value="2"]')
element.click()

#Compra
element =driver.find_element_by_xpath('//*[@type="checkbox" and @name="ChkCompra" and @value="ON"]')
element.click()

print('2')  

#Barrio selector
#este selector de barrio no anda bien, pero como queremos todos, que traiga todos y listo
#element =driver.find_element_by_xpath('//*[@name="CmbBarrio1"]')    
#Select(element).select_by_value('4')


#SUBMIT
element =driver.find_element_by_xpath('//*[@type="submit"]')
element.click()


########### PAGINA 3

element =driver.find_element_by_xpath('//*[@type="radio" and @name="optAmbientes2" and @value="2"]')
element.click()

element =driver.find_element_by_xpath('//*[@type="radio" and @name="optAmbientesx2" and @value="2"]')
element.click()


#SUBMIT
element =driver.find_element_by_xpath('//*[@type="submit"]')
element.click()

##

#TENER EN CUENTA LA URL DE LA PAGINA CAMBIAR A QUE MUESTRE 1000 PARA MOSTRAR TODOS Y SCREAPEAR
#TENER EN CUENTA LA URL DE LA PAGINA CAMBIAR A QUE MUESTRE 1000 PARA MOSTRAR TODOS Y SCREAPEAR
#TENER EN CUENTA LA URL DE LA PAGINA CAMBIAR A QUE MUESTRE 1000 PARA MOSTRAR TODOS Y SCREAPEAR
#TENER EN CUENTA LA URL DE LA PAGINA CAMBIAR A QUE MUESTRE 1000 PARA MOSTRAR TODOS Y SCREAPEAR
#TENER EN CUENTA LA URL DE LA PAGINA CAMBIAR A QUE MUESTRE 1000 PARA MOSTRAR TODOS Y SCREAPEAR

#OBTENER LOS LINKS

pag2="https://soloduenos.com/ResultadoBusqueda.asp?whichpage=1&pagesize=1000&NroZona=1&sqlQuery=~(a.CodInmueble=2%20AND%20Ambiente%3E=2%20AND%20Ambiente%3C=2)~~~~~~~~~~~~~~&SQLQueryEnvios=%27ON%27%2C%27%27%2C%27%27%2C1%2C1%2C%270%27%2C%270%27%2C%270%27%2C%270%27%2C%27%27%2C%271%27%2C+%27%27%2C%27%28a%2ECodInmueble%3D2+AND+Ambiente%3E%3D2+AND+Ambiente%3C%3D2%29%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27%2C%27%27&"
pagina = 'https://soloduenos.com/buscar.asp'
driver.get(pag2)

urls=[]
beg ='https://soloduenos.com/'

soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
links = soup.find_all('a', href=True)
for i in links:
    try:
        if str(i)[0:23] == '<a href="Ficha.asp?Tipo':
            urls.append(beg+i.get('href'))
    except:
        print('error en devolver links')
  

#Se queda con los links unicos      

url_unicos = set(urls)

for i in url_unicos:
    try:
        print (i)
        fila = obtiene_datos(i,driver)
        lista_datos.append(fila)
    except:
        pass



datf=pd.DataFrame(lista_datos)


datf.to_csv('deptos.csv', sep='\t')



bajada3.py
Mostrando bajada3.py.

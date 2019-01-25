# -*- coding: utf-8 -*-
from subprocess import Popen
import subprocess
import pyodbc


def run_batch_file(file_path):
    p=Popen(file_path,creationflags=subprocess.CREATE_NEW_CONSOLE)
    return p

#ejecuta consulta sql

con = pyodbc.connect('DRIVER={SQL Server};SERVER=srappw021p000.terceros.banco.com.ar\HST1;DATABASE=DAM;TRUSTED_CONNECTION=yes;pwd=[windows_pass]')
cur = con.cursor()

filename = 'G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/9- cheques_ultimo_mes/0- crea_tabla_rechazados_ultimo_mes.sql'
f = open(filename, 'r')
query = " ".join(f.readlines())


cur.execute(query)
con.commit()

#ejecuta cruce spss

path_bat ='G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/9- cheques_ultimo_mes/cruce_cheques_mes.bat'

p=run_batch_file(path_bat)
p_status = p.wait()


#ejecuta impresion de la alerta

path_principal = 'G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/'

#guarda alerta
subprocess.call(['python', path_principal+'9- cheques_ultimo_mes/2- imprime meses.py'])
# -*- coding: utf-8 -*-

import pyodbc
import pandas as pd

##
## 1 - Comienza ingreso de datos
##


con = pyodbc.connect('DRIVER={SQL Server};SERVER=srappw021p000.terceros.banco.com.ar\HST1;DATABASE=DAM;TRUSTED_CONNECTION=yes;pwd=[windows_pass]')
cur = con.cursor()

    
db_cmd = " select Documento, Banca_Id, Tipo_Persona_Id, DEUDA as Deuda, Calificacion_Global as Calificacion, Disponible_Global as Disponible from claiun_salida_cheques_cruce_1mes order by DEUDA desc"
res = cur.execute(db_cmd)
data = cur.fetchall()


df = pd.DataFrame(columns=['Documento','Banca_Id','Tipo_Persona_Id','Deuda','Calificacion','Disponible'])

for r in data:
    df.loc[len(df)] = [r[0],r[1],r[2],r[3],r[4],r[5]]


##
## 1 - Termina ingreso de datos
##


#Genera un excel con la salida
#\\srfspw001i005.terceros.banco.com.ar\Util_W0010S04\JCGil
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('//srfspw001i005.terceros.banco.com.ar/Util_W0010S04/JCGil/ALERTAS/cheques_rechazados.xlsx', engine='xlsxwriter')
#writer = pd.ExcelWriter('C:\\Users\\LAC40641\\Downloads\\deuda_cheques.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='cheques',index=False)
# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['cheques']


#formato numero y ancho columna
format1 = workbook.add_format({'num_format': '$ #,##0'})
worksheet.set_column('D:D', 18, format1)
format1 = workbook.add_format({'num_format': '$ #,##0'})
worksheet.set_column('E:E', 18, format1)
format1 = workbook.add_format({'num_format': '$ #,##0'})
worksheet.set_column('F:F', 18, format1)



titulo = workbook.add_format({ 'bg_color': '#E4DDDD','font_color': '#575353','font_size': 12,'text_wrap':'true'})
worksheet.write(0,0,'Documento', titulo)
worksheet.write(0,1,'Banca_Id', titulo)
worksheet.write(0,2,'Tipo_Persona_Id', titulo)
worksheet.write(0,3,'Deuda', titulo)
worksheet.write(0,4,'Calificacion', titulo)
worksheet.write(0,5,'Disponible', titulo)


# ancho columna
worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 17)
worksheet.set_column('D:D', 13)
worksheet.set_column('E:E', 15)
worksheet.set_column('F:F', 15)




worksheet.autofilter('A1:F999999')

writer.save()

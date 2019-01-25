# -*- coding: utf-8 -*-

import pyodbc
import pandas as pd

##
## 1 - Comienza ingreso de datos
##


con = pyodbc.connect('DRIVER={SQL Server};SERVER=srappw021p000.terceros.banco.com.ar\HST1;DATABASE=DAM;TRUSTED_CONNECTION=yes;pwd=[windows_pass]')
cur = con.cursor()

filename = 'G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/6-imprime_todos/imprime_todos_formato.sql'
f = open(filename, 'r')
query = " ".join(f.readlines())
cur.execute(query)
con.commit()



db_cmd = "select * from claiun_tmp_formato_nosis_cheques_fechas"
res = cur.execute(db_cmd)
data = cur.fetchall()


df = pd.DataFrame(columns=['cuil','nro_cheque','fecha_rechazo','monto','fecha_pago','causal','pago_multa','persona_juridica_relacionada','dias_pago_cheque','dias_pago_multa'])

for r in data:
    df.loc[len(df)] = [r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[8]]


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




titulo = workbook.add_format({ 'bg_color': '#E4DDDD','font_color': '#575353','font_size': 12,'text_wrap':'true'})
worksheet.write(0,0,'cuil', titulo)
worksheet.write(0,1,'Cheque Nº', titulo)
worksheet.write(0,2,'Fecha rechazo', titulo)
worksheet.write(0,3,'Monto', titulo)
worksheet.write(0,4,'Fecha pago', titulo)
worksheet.write(0,5,'causal', titulo)
worksheet.write(0,6,'Pago multa', titulo)
worksheet.write(0,7,'Persona Jurídica Relacionada', titulo)
worksheet.write(0,8,'Dias pago cheque', titulo)
worksheet.write(0,9,'Dias pago multa', titulo)


# ancho columna
worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 17)
worksheet.set_column('D:D', 13)
worksheet.set_column('E:E', 15)
worksheet.set_column('F:F', 15)
worksheet.set_column('G:G', 15)
worksheet.set_column('H:H', 15)
worksheet.set_column('I:I', 15)
worksheet.set_column('J:J', 15)

#formato condicion Impago
format_impaga = workbook.add_format({'bg_color': '#ECE7E7','font_color': '#9C0006'})
worksheet.conditional_format('G2:G999999', {'type': 'text',
                                         'criteria': 'containing',
                                         'value': 'IMPAGA',
                                         'format': format_impaga})




worksheet.autofilter('A1:J999999')

writer.save()

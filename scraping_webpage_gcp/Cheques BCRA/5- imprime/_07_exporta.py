# -*- coding: utf-8 -*-

import pyodbc
import pandas as pd

con = pyodbc.connect('DRIVER={SQL Server};SERVER=srappw021p000.terceros.banco.com.ar\HST1;DATABASE=DAM;TRUSTED_CONNECTION=yes;pwd=[windows_pass]')
cur = con.cursor()
db_cmd = "select Nro_Documento_Persona,Monto_cheques_SF,Cliente_Nombre,Deuda_Total_BP,Estado,Banca_Desc,Mes_Situacion_BCRA,Situacion_BCRA,Inhabilitado_Multa from claiun_salida_cheques_bcra"
res = cur.execute(db_cmd)
data = cur.fetchall()

df = pd.DataFrame(columns=['Nro_Documento_Persona','Monto_cheques_SF','Cliente_Nombre','Deuda_Total_BP','Estado','Banca_Desc','Mes_Situacion_BCRA','Situacion_BCRA','Inhabilitado_Multa'])


for r in data:
    df.loc[len(df)] = [r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]]


#Genera un excel con la salida
#\\srfspw001i005.terceros.banco.com.ar\Util_W0010S04\JCGil
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('//srfspw001i005.terceros.banco.com.ar/Util_W0010S04/JCGil/ALERTAS/deuda_cheques.xlsx', engine='xlsxwriter')
#writer = pd.ExcelWriter('C:\\Users\\LAC40641\\Downloads\\deuda_cheques.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Por deuda',index=False)
# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Por deuda']

#formato numero y ancho columna
format1 = workbook.add_format({'num_format': '$ #,##0'})
worksheet.set_column('D:D', 18, format1)
worksheet.set_column('B:B', 18, format1)


titulo = workbook.add_format({ 'bg_color': '#5081BB','font_color': '#FFFFFF','font_size': 12,'text_wrap':'true'})
worksheet.write(0,0,'Nro_Documento', titulo)
worksheet.write(0,1,'Monto_cheques_SF', titulo)
worksheet.write(0,2,'Cliente_Nombre', titulo)
worksheet.write(0,3,'Deuda_Total_BP', titulo)
worksheet.write(0,4,'Estado', titulo)
worksheet.write(0,5,'Banca_Desc', titulo)
worksheet.write(0,6,'Mes_Situacion_BCRA', titulo)
worksheet.write(0,7,'Situacion_BCRA', titulo)
worksheet.write(0,8,'Inhabilitado_Multa', titulo)


# ancho columna
worksheet.set_column('A:A', 17)
worksheet.set_column('B:B', 21)
worksheet.set_column('C:C', 25)
worksheet.set_column('D:D', 18)
worksheet.set_column('E:E', 18)
worksheet.set_column('F:F', 22)
worksheet.set_column('G:G', 22)
worksheet.set_column('H:H', 18)
worksheet.set_column('I:I', 20)


#formato condicion BCRA 4 o 5
format_4 = workbook.add_format({'bg_color': '#F3B25C','font_color': '#7F4801'})
worksheet.conditional_format('H2:H10000', {'type': 'text',
                                         'criteria': 'containing',
                                         'value': '4',
                                         'format': format_4})
format_5 = workbook.add_format({'bg_color': '#FFC7CE','font_color': '#9C0006'})
worksheet.conditional_format('H2:H10000', {'type': 'text',
                                         'criteria': 'containing',
                                         'value': '5',
                                         'format': format_5})

#formato condicion inhabilitado_multa si
format_multa = workbook.add_format({'bg_color': '#FFC7CE','font_color': '#9C0006'})

worksheet.conditional_format('I2:I10000', {'type': 'text',
                                         'criteria': 'containing',
                                         'value': 'Si',
                                         'format': format_multa})
#formato condicion estado cartera
format_cartera_mora = workbook.add_format({'bg_color': '#FFC7CE','font_color': '#9C0006'})
worksheet.conditional_format('E2:E10000', {'type': 'text',
                                         'criteria': 'containing',
                                         'value': 'Mora más de 90 Días',
                                         'format': format_cartera_mora})
    
format_cartera_31_90_dias = workbook.add_format({'bg_color': '#F3B25C','font_color': '#7F4801'})
worksheet.conditional_format('E2:E10000', {'type': 'text',
                                         'criteria': 'containing',
                                         'value': 'Atraso 31 a 90 Días',
                                         'format': format_cartera_31_90_dias})
    
format_cartera_7_30_dias = workbook.add_format({'bg_color': '#F2E463','font_color': '#766B03'})
worksheet.conditional_format('E2:E10000', {'type': 'text',
                                         'criteria': 'containing',
                                         'value': 'Atraso 7 a 30 Días',
                                         'format': format_cartera_7_30_dias})

worksheet.autofilter('A1:I99999')

writer.save()

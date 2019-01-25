# -*- coding: utf-8 -*-
from subprocess import Popen
import subprocess
import pyodbc

con = pyodbc.connect('DRIVER={SQL Server};SERVER=srappw021p000.terceros.banco.com.ar\HST1;DATABASE=DAM;TRUSTED_CONNECTION=yes;pwd=[windows_pass]')
cur = con.cursor()

#path_bat = '//srappw001v011.terceros.banco.com.ar/Disco D/COBRANZAS/prueba_claiun/cheques_scraping/Track manual/2- subida/batch_carga_cheques.bat'


def run_batch_file(file_path):
    p=Popen(file_path,creationflags=subprocess.CREATE_NEW_CONSOLE)
    return p


filename = 'G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/2- subida/0-borra_meses_anteriores.sql'
f = open(filename, 'r')
query = " ".join(f.readlines())
cur.execute(query)
con.commit()



p=run_batch_file('G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/2- subida/0-inserta_meses_a_borrar.bat')
p_status = p.wait()



filename = 'G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/2- subida/1-borra_registro_meses.sql'
f = open(filename, 'r')
query = " ".join(f.readlines())
cur.execute(query)
con.commit()



p=run_batch_file('G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/2- subida/2-inserta_registros.bat')
p_status = p.wait()

# import pyodbc
# con = pyodbc.connect('DRIVER={SQL Server};SERVER=srappw021p000.terceros.banco.com.ar\HST1;DATABASE=DAM;TRUSTED_CONNECTION=yes;pwd=[windows_pass]')
# cur = con.cursor()

# #cur.execute("drop table claiun_bcra_tmp")
# #con.commit()

# CREATE TABLE [dbo].[claiun_bcra_cheques_al_format](
# 	[cuil] [bigint] NULL,
# 	[nro_cheque] [bigint] NULL,
# 	[fecha_rechazo] [bigint] NULL,
# 	[monto] [float] NULL,
# 	[fecha_pago] [bigint] NULL,
# 	[causal] [nvarchar](255) NULL,
# 	[pago_multa] [nvarchar](255) NULL,
# 	[persona_juridica_relacionada] [nvarchar](255) NULL,
# 	[mes] [bigint] NULL
# ) ON [PRIMARY]


# insert into [dbo].[claiun_bcra_cheques_al_format_tmp] ([cuil],[nro_cheque],[fecha_rechazo],[monto],[fecha_pago],[causal],[pago_multa],[persona_juridica_relacionada],[mes])
# values
# ()


# cur.execute("CREATE TABLE claiun_bcra_cheques_al_format_tmp (cuil integer, nombre varchar(30), mes integer)")
# con.commit() 

# cur.execute("INSERT INTO claiun_bcra_tmp values (35560145, 'nombre', 4)")
# con.commit() 



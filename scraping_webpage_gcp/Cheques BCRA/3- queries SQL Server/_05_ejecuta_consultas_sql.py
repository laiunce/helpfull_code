import pyodbc
con = pyodbc.connect('DRIVER={SQL Server};SERVER=srappw021p000.terceros.banco.com.ar\HST1;DATABASE=DAM;TRUSTED_CONNECTION=yes;pwd=[windows_pass]')
cur = con.cursor()

#ejecuta 1- cheques_rechazados.sql

filename = 'G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/3- queries SQL Server/1- cheques_rechazados.sql'
f = open(filename, 'r')
query = " ".join(f.readlines())


cur.execute(query)
con.commit()


#ejecuta 2- inhabilitados_multas.sql

#filename2 = 'G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/3- queries SQL Server/2- inhabilitados_multas.sql'
#f2 = open(filename2, 'r')
#query2 = " ".join(f2.readlines())
#cur.execute(query2)
#con.commit()


#ejecuta 3- registros unicos estados.sql

filename3 = 'G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/3- queries SQL Server/3- registros unicos estados.sql'
f3 = open(filename3, 'r')
query3 = " ".join(f3.readlines())


cur.execute(query3)
con.commit()


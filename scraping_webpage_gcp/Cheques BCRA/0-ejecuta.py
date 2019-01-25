
import subprocess

path_principal = 'G://COBRANZAS/prueba_claiun/cheques_scraping/Track manual/'


#bajada y transformacion
subprocess.call(['python', path_principal+'1- bajada/_01_bajada_cheques.py'])
subprocess.call(['python', path_principal+'1- bajada/_02_transforma_datos.py'])
subprocess.call(['python', path_principal+'1- bajada/_03_une_datasets.py'])

#subida a SQL Server

#no anda G:\COBRANZAS\prueba_claiun\cheques_scraping\Track manual\2- subida\0-inserta_meses_a_borrar.str
subprocess.call(['python', path_principal+'2- subida/_04_crea_tabla_carga.py'])

#Consultas de tranformacion y creacion de metricas
#subprocess.call(['python', path_principal+'3- queries SQL Server/_05_ejecuta_consultas_sql.py'])

#cruce con clientes con deuda
#subprocess.call(['python', path_principal+'4- Salida/_06_cruce_comparacion.py'])

#imprime archivo en servidor
#subprocess.call(['python', path_principal+'5- imprime/_07_exporta.py'])

#imprime todos los cheques en servidor
#subprocess.call(['python', path_principal+'6-imprime_todos/_08_exporta_todos.py'])

#imprime cruce de cheques ultimo mes
subprocess.call(['python', path_principal+'9- cheques_ultimo_mes/ejecuta_cruce.py'])
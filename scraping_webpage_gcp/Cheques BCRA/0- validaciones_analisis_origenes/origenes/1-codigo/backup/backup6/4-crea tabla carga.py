# -*- coding: utf-8 -*-
import pyodbc
import pandas as pd
from pandas import DataFrame
from pandas.tools import plotting
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

####
####
####
####
#### NO TENEMOS PERMISOS !!!!
####
####
####

import pyodbc
con = pyodbc.connect('DRIVER={SQL Server};SERVER=srappw021p000.terceros.banco.com.ar\HST1;DATABASE=DAM;TRUSTED_CONNECTION=yes')
cur = con.cursor()
cur.execute("drop table claiun_bcra_cheques_pa")
con.commit() #I've also tried cur.commit()

cur.execute("CREATE TABLE claiun_bcra_cheques_pa (cuil integer, nombre varchar(30), mes integer)")
con.commit() 
# Given 10000 logs
# Group logs by employee
# Number of each category `enter_for` a employee has entered
# i.e. employee 1002 meeting - 52, call - 80
# Show hot hours for enter to the facilities

# import librerias

import csv
import pandas as pd
import numpy as np
from datetime import datetime
# Definimos constante del archivo
FILENAME = 'writing_csv.csv'

#asignamos a data frame los datos del csv
df = pd.read_csv(FILENAME)
#agregamos columna al dataframe de fecha para convertir el timestamp y lo calculamos con segundos
df["Hora"]=pd.to_datetime(df["entered_at"],unit="s").dt.hour
#agrupamos por fechas y contamos los registros
df_agrupado=df.groupby(['Hora']).size().reset_index(name="count")
#ordenamos por los mas altos
df_ordenado=df_agrupado.sort_values(['count'],ascending=[False])
#iteramos el df_ordenado
i=0
for index, row in df_ordenado.iloc[:5].iterrows():
    i=i+1
   # Hora=.datetime.utcfromtimestamp(row["Fecha"])
    print (f'The hot hour number {i} is at {row["Hora"]} hrs. with {row["count"]} enter to the facilities')



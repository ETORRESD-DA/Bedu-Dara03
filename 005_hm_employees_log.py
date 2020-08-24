  
# Given 10000 logs
# Group logs by employee
# Number of each category `enter_for` a employee has entered
# i.e. employee 1002 meeting - 52, call - 80
# Show hot hours for enter to the facilities


import csv
# import pandas
import pandas as pd
from datetime import datetime
# CONSTANT
FILENAME = 'writing_csv.csv'
#asignamos a data frame los datos delcsv
df = pd.read_csv(FILENAME)

#agrupamos
#print(df.groupby(['employee_id','enter_for']).agg(['count']))
df_agrupado=df.groupby(['employee_id','enter_for']).size().reset_index(name="count")
df_ordenado=df_agrupado.sort_values(['employee_id','count'],ascending=[True,False])
print(df_ordenado)






 


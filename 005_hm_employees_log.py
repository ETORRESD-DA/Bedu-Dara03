  
# Given 10000 logs
# Group logs by employee
# Number of each category `enter_for` a employee has entered
# i.e. employee 1002 meeting - 52, call - 80
# Show hot hours for enter to the facilities

#Importamos librerias
import csv
import pandas as pd
# CONSTANT
FILENAME = 'writing_csv.csv'
#asignamos a data frame los datos delcsv
df = pd.read_csv(FILENAME)
#agrupamos
df_agrupado=df.groupby(['employee_id','enter_for']).size().reset_index(name="count")
#ordenamos
df_ordenado=df_agrupado.sort_values(['employee_id','count'],ascending=[True,False])
#print(df_ordenado)

#convertimos de lista larga a lista ancha, funcion interesante
#df_ordenado=df_ordenado.pivot(index='employee_id', columns='enter_for', values='count').reset_index()
#print(df_ordenado)

#extraemos los valores unicos de empleados
Lista_employees = list(df_ordenado["employee_id"].unique())
#print(Lista_employees)

#Lista_categorias = list(df_ordenado.columns)
#print(Lista_categorias)

#recorremos la lista de empleados
for i in Lista_employees:
   #asignamos el valor de empleado a variable Empleado
   Empleado=i
   #Inicializamos la variable cadenaInter que me guarda la construccion de la cadena
   cadenaInter=""
   #recorremos la tuplas
   for row in df_ordenado.itertuples():
      #print(row.employee_id)
      #print(Empleado)
      #construimos la cadena paralaparte del empleado
      Cadena_Empleado=f'for employee {Empleado}'
      #comparamos el empleado con la tupla 1 a 1
      if row.employee_id == Empleado:
         #armamos la cadena final
         cadenaInter=(f'{cadenaInter} {row.enter_for}-{row.count}')
   #imprimimos
   print(Cadena_Empleado,cadenaInter)
   #creo que el algoritmo no es optimo, tendriamos que agregar una funcion que me ayude a filtrar
   #antes de usar


    



# for employee_id, row in df_ordenado.iterrows():
#   for enter_for, column in row.iteritems():
#      print(row)

     #df_ordenado=df_ordenado.pivot(index='employee_id', columns='enter_for', values='count').reset_index()





 


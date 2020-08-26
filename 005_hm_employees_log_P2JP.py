{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import librerias\n",
    "\n",
    "import csv\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Definimos constante del archivo\n",
    "FILENAME = 'writing_csv.csv'\n",
    "\n",
    "#asignamos a data frame los datos del csv\n",
    "df = pd.read_csv(FILENAME)\n",
    "#agregamos columna al dataframe de fecha para convertir el timestamp y lo calculamos con segundos\n",
    "df[\"Hora\"]=pd.to_datetime(df[\"entered_at\"],unit=\"s\").dt.hour"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#agrupamos por fechas y contamos los registros\n",
    "df_agrupado=df.groupby(['Hora']).size().reset_index(name=\"count\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#ordenamos por los mas altos\n",
    "df_ordenado=df_agrupado.sort_values(['count'],ascending=[False])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The hot hour number 1 is at 23 hrs. with 870 enter to the facilities\n",
      "The hot hour number 2 is at 18 hrs. with 850 enter to the facilities\n",
      "The hot hour number 3 is at 17 hrs. with 849 enter to the facilities\n",
      "The hot hour number 4 is at 20 hrs. with 848 enter to the facilities\n",
      "The hot hour number 5 is at 22 hrs. with 848 enter to the facilities\n"
     ]
    }
   ],
   "source": [
    "#iteramos el df_ordenado\n",
    "i=0\n",
    "for index, row in df_ordenado.iloc[:5].iterrows():\n",
    "    i=i+1\n",
    "   # Hora=.datetime.utcfromtimestamp(row[\"Fecha\"])\n",
    "    print (f'The hot hour number {i} is at {row[\"Hora\"]} hrs. with {row[\"count\"]} enter to the facilities')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

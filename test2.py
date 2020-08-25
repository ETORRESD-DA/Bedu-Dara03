import csv
import random
from datetime import datetime
ahora=datetime.now()
print(ahora)
ahora = ahora.replace(hour=random.randint(7, 18), minute=random.randint(0, 59))
print(ahora)
ts = datetime.timestamp(ahora)
print(ts)
tsreturn = datetime.fromtimestamp(1598312168)
print(tsreturn)
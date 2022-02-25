from dataclasses import dataclass
import datetime

my_time = datetime.datetime.now()
my_day = datetime.date.today()

#Formato
my_str = my_time.strftime('%d/%m/%y')
my_str = my_time.strftime('El ano es: %y')

print(my_str)

# Zonas horarias.

import pytz

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

bogota = pytz.timezone('America/Bogota')
bogota_date = datetime.datetime.now(bogota)
print(f'Bogota: {bogota_date}')

mexico = pytz.timezone('America/Mexico_City')
mexico_date = datetime.datetime.now(mexico)
print(f'Mexico: {mexico_date}')


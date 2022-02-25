from dataclasses import dataclass
import datetime

my_time = datetime.datetime.now()
my_day = datetime.date.today()

#Formato
my_str = my_time.strftime('%d/%m/%y')
my_str = my_time.strftime('El ano es: %y')

print(my_str)
from datetime import datetime, date
import pytz
import os

# Fecha/Hora actual del equipo
now = datetime.now()
print(now)

my_day = date.today()
print(my_day)

print(f"Year: {my_day.year}")
print(f"Day: {my_day.day}")
print(f"Month: {my_day.month}")

# Formateo de fechas
# %Y => Year
# %m => Month
# %d => Day
# %H => Hour
# %M => Minute
# %S => Second

my_str = now.strftime("%d/%m/%Y")
print(f"Formato LATAM: {my_str}")

my_str = now.strftime("%m/%d/%Y")
print(f"Formato USA: {my_str}")

my_str = now.strftime("Estamos en el año %Y")
print(f"Formato Random: {my_str}")


os.system("clear")
# Zonas Horarias (Time Zones)
# Modulo pytz
# Lista de Time Zones https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print(f"Bogota: {bogota_date.strftime('%d/%m/%Y, %H:%M:%S')}")

santiago_timezone = pytz.timezone("America/Santiago")
santiago_date = datetime.now(santiago_timezone)
print(f"Santiago: {santiago_date.strftime('%d/%m/%Y, %H:%M:%S')}")

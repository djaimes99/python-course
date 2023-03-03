# import datetime

# print(datetime.date.today())
# # 2023-02-01

# #convertir minutos a horas 
# print(datetime.timedelta(minutes=70))
# #1:10:00 equivalente en horas de 70 minutos

#################################################

#Otra forma de importar un módulo o libreria
# from datetime import timedelta,date
# import fmath

# print (date.today())
# fmath.add(5, 30)
# fmath.substract(30, 5)

#usando modulos creados por otros,una vez instalado...
#cambiar el color de las letras en la consola 
from colorama import Fore, Style, init 
init(autoreset=True) #ó init(convert=True), para que funcione en consola de windows
print(Fore.RED + "Hello World")


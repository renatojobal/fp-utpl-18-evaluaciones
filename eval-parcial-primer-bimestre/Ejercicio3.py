'''
Ejercicio 3.- Realizar un programa que permita ingresar un valor en segundos, luego realizar un proceso que
permita presentar el valor en minutos y segundos del valor dado. Ejemplo:
100 segundos es igual a 1 minuto y 40 segundos


@author Renato
'''

# INGRESO DE DATOS
segundos = 0
minutos = 0
horas = 0
dias = 0
seconds = float(input("Ingrese los segundos: ")) # La variable "seconds" sirve para poder presentar el original al final
segundos = seconds

# CALCULO
while(segundos > 60):
    minutos = minutos + 1
    segundos = segundos - 60

while(minutos > 60):
    horas = horas + 1
    minutos = minutos - 60

while(horas > 24):
    dias = dias + 1
    horas = horas - 24


# SALIDA
print("{} segundos es igual a {} dias, {} horas, {} minutos y {} segundos\n".format(seconds, dias, horas, minutos, segundos))

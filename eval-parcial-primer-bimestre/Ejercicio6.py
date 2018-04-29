'''
Ejercicio 6.- Realizar un programa que permita ingresar el número de mes de un 
año (1,…,12), en base al valor ingresado presenta el número de días que tiene ese mes.

@author Renato
'''

# INGRESO DE DATOS

nroMes = int(input("Ingrese el número del mes: "))

# CALCULO
if(nroMes == 2):
    dias = 28
elif(nroMes == 4 and nroMes == 6 and nroMes == 9 and nroMes == 11):
    dias = 30
else:
    dias = 31

# SALIDA
print("El mes {} tiene {} dias\n".format(nroMes, dias))

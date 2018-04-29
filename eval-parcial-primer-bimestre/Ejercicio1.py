

'''
Ejercicio 1.- Realizar un programa en Java que permita ingresar por teclado la 
longitud y la anchura de una habitación, realizar los procesos respectivos que 
permita obtener la superficie de la misma, además
se debe presentar en pantalla el valor de la superficie, finalmente tomar en 
consideración que se debe presentar el valor con 3 decimales. 

@author Renato
'''



# INGRESO DE DATOS

largo = float(input("Ingrese el largo de la habitación en metros: "))

ancho = float(input("Ingrese el ancho de la habitación en metro: "))

# CALCULO
superficie = largo*ancho

# SALIDA
print("La superficie de la habitación es {} metros cuadrados.".format(superficie))



'''
Ejercicio 2.- Ingresar por teclado la variables: x,y,z.
En base a las mismas realizar la siguiente operación:
m = (x+(y/z))/(x-(y/z))
y finalmente presentar en pantalla el siguiente reporte:

El valor de m, en base a las variables:
x = 10.2
 y = 9.2
  z = 8.2
da como resultado:
     m = ?

@author Renato
'''

# INGRESO DE DATOS
x = float(input("Ingrese el valor para la variable x: "))
y = float(input("Ingrese el valor para la variable y: "))
z = float(input("Ingrese el valor para la variable z: "))


# CALCULO
m = (x+(y/z))/(x-(y/z))

# SALIDA
print("Se ha calculado el valor de m a partir de m = (x+(y/z))/(x-(y/z))")

print("El valor de m, en base a las variables:\nx = {}\n y = {}\n  z = {}\nda como resultado:\n     m = {}".format(x, y, z, round(m, 2)))



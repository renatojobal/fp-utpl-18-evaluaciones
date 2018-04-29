'''
Ejercicio 4.- Dado el siguiente sistema de ecuaciones:
ax + by = c
dx + ey = f
resolverlo aplicando las siguientes formulas:

x = (c*e-b*f)/(a*e-b*d)
y = (c*e-b*f)/(a*e-b*d)

Presentar en pantalla los valores de x y y

@author Renato
'''

# INGRESO DE DATOS

a = float(input("Igrese el valor de a: "))
b = float(input("Igrese el valor de b: "))
c = float(input("Igrese el valor de c: "))
d = float(input("Igrese el valor de d: "))
e = float(input("Igrese el valor de e: "))
f = float(input("Igrese el valor de f: "))


# CALCULO
x = (c*e-b*f)/(a*e-b*d)
y = (c*e-b*f)/(a*e-b*d)

# SALIDA
print("RESPUESTA: \n x = {}f\n y = {}\n".format(round(x, 3), round(y, 3)))

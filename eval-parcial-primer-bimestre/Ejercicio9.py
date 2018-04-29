'''
Ejercicio 9.- Dos triángulos son congruentes si tienen la misma forma y tamaño, es decir, su ángulos y lados
correspondientes son iguales. Elaborar un algoritmo que lea los tres ángulos y tres lados de dos
triángulos e imprima si son congruentes, caso contrario que imprima que no son congruentes.
@author Renato
'''




'''
  Se obtiene el varlo de cada angulo y lado de ambos triangulos
'''

# INGRESO DE DATOS
print("PRIMER TRIANGULO")

# Angulos
print("\t--Angulos--")
anguloA1 = float(input("\t\tIngrese el valor del ángulo A: "))
anguloB1 = float(input("\t\tIngrese el valor del ángulo B: "))
anguloC1 = float(input("\t\tIngrese el valor del ángulo C: "))

# Lados
print("--Lados--")
ladoa1 = float(input("\t\tIngrese el valor del lado a: "))
ladob1 = float(input("\t\tIngrese el valor del lado b: "))
ladoc1 = float(input("\t\tIngrese el valor del lado c: "))
print("SEGUNDO TRIANGULO")

# Angulos
print("\t--Angulos--")
anguloA2 = float(input("\t\tIngrese el valor del ángulo A: "))
anguloB2 = float(input("\t\tIngrese el valor del ángulo B: "))
anguloC2 = float(input("\t\tIngrese el valor del ángulo C: "))

# Lados
print("\t--Lados--")

ladoa2 = float(input("\t\tIngrese el valor del lado a: "))
ladob2 = float(input("\t\tIngrese el valor del lado b: "))
ladoc2 = float(input("\t\tIngrese el valor del lado c: "))


# CALCULO y SALIDA

if((anguloA1 == anguloA2) and (anguloB1 == anguloB2) and (anguloC1 == anguloC2) and (ladoa1 == ladoa2) and (ladob1 == ladob2) and (ladoc1 == ladoc2)):
    print("Si son congruentes")
else:
    print("No son congruentes")







'''
Ejercicio 8.- Ingresar por teclado tres variables, dichas variables siempre tendrán como valores letras
mayúsculas de abecedario. 
Sabiendo que por ejemplo la letra “E” es menor que la letra “P”; establezca una solución que
permita determinar ¿Cuál de las tres letras ingresadas, aparece primero en el abecedario ?
Ejemplo: Si el usuario ingresa:
v1 = “Z”
v2 = “B”
v3 = “C”
La primera letra que aparece en el abecedario es B
 * @author Renato
 '''

# INGRESO DE DATOS


nombre1 = str(input("Ingrese una letra: "))
nombre1 = nombre1.upper()        # Se lo convierte en mayusculas
v1 = nombre1[0]              # Se obtiene la primera letra

nombre2 = str(input("Ingrese una letra: "))
nombre2 = nombre2.upper()         # Se lo convierte en mayusculas
v2 = nombre2[0]              # Se obtiene la primera letra

nombre3 = str(input("Ingrese una letra: "))
nombre3 = nombre3.upper()         # Se lo convierte en mayusculas
v3 = nombre3[0]              # Se obtiene la primera letra

# CALCULO y SALIDA
if(v1 < v2 and v1 < v3):
    print("La primera letra que aparece en el abecedario es {}".format(v1))
else:
    if(v2 < v1 and v2 < v3):
        print("La primera letra que aparece en el abecedario es {}".format(v2))
    else:
        print("La primera letra que aparece en el abecedario es {}".format(v3))

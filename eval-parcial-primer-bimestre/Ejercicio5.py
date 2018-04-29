'''
Ejercicio 5.- Ingresar por teclados 4 calificaciones de un estudiante, encontrar el promedio de las
calificaciones ingresadas. Presentar la puntuación del estudiante en base a la siguiente información:
Media Puntuación
90-100 A
80-89 B
70-79 C
0-69 D
El reporte sería por ejemplo así:
El estudiante con el promedio de calificaciones 70, tiene una puntuación de C
 
 
 * @author Renato
'''

# INGRESO DE DATOS
contador = 1
n = 4
suma = 0
puntuacion = "Sin especificar"
while (contador <= n):
    calificacion = float(input("Ingrese la calificacion {}: ".format(contador)))
    suma = suma + calificacion  # Las calificaciones se van agregando a la variable suma
    contador = contador + 1


# CALCULO
promedio = (suma)/n

if(promedio >= 90 and promedio <= 100):
    puntuacion = "A"
elif(promedio >= 80 and promedio < 90):
    puntuacion = "B"
elif(promedio >= 70 and promedio < 80):
    puntuacion = "C"
elif(promedio < 70):
    puntuacion = "D"
else:
    print("ERROR: Las calificaciones están fuera del rango de 1 a 100.") # En caso de haber ingresado calificaciones incorrectas


# SALIDA
if promedio >= 1 and promedio <= 100:
	print("El estudiante con el promedio de calificaciones {}, tiene una puntuación de {}\n".format(promedio, puntuacion))
else:
	print("ERROR: Las calificaciones están fuera del rango de 1 a 100.") # En caso de haber ingresado calificaciones incorrectas

'''
Ejercicio 7.- Un empresa paga a sus vendedores de la siguiente manera:
Sueldo fijo $ 360.40 más un porcentaje de las ventas realizadas en el mes.
Si las ventas fueron menores o iguales a $ 500, el porcentaje es de 5%
Si las ventas fueron mayores a $ 500 y menores o iguales a $1000, el porcentaje es de 8%
Si las ventas fueron mayores a $ 1000 y menores o iguales a $5000, el porcentaje es de 10%
Si las ventas fueron mayores a $ 5000, el porcentaje es de 15%
Ingresar el valor de las ventas de un empleado y calcular su sueldo en base la información dada
 * @author Renato
'''

# INGRESO DE DATOS
sueldoFijo = 360.40

ventas = float(input("Ingrese el valor de las ventas del empleado en dolares: "))


# CALCULO
if(ventas <= 500):
    aumento = ventas * 0.05
    sueldoTotal = sueldoFijo + aumento
    
else if(ventas > 500 and ventas <= 1000):
    aumento = ventas * 0.08
    sueldoTotal = sueldoFijo + aumento
    
else if(ventas > 1000 and ventas <= 5000):
    aumento = ventas * 0.10
    sueldoTotal = sueldoFijo + aumento
    
else:
    aumento = ventas * 0.15
    sueldoTotal = sueldoFijo + aumento


# SALIDA
print("El sueldo del asciende a: %.2f USD\n".format(sueldoTotal))

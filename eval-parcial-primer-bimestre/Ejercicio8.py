package examenprimerparcial;

import java.util.Scanner;

/**
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
 */
public class Ejercicio8 {
    public static void main(String[] args){
        // DECLARACION DE VARIABLES
        char v1, v2, v3;
        String nombre1, nombre2, nombre3;
        
        // INGRESO DE DATOS
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese una letra: ");
        nombre1 = entrada.nextLine();
        nombre1 = nombre1.toUpperCase(); // Se lo convierte en mayusculas
        v1 = nombre1.charAt(0);          // Se obtiene la primera letra
        
        System.out.println("Ingrese una letra: ");
        nombre2 = entrada.nextLine();
        nombre2 = nombre2.toUpperCase(); // Se lo convierte en mayusculas
        v2 = nombre2.charAt(0);          // Se obtiene la primera letra
        
        System.out.println("Ingrese una letra: ");
        nombre3 = entrada.nextLine();
        nombre3 = nombre3.toUpperCase(); // Se lo convierte en mayusculas
        v3 = nombre3.charAt(0);          // Se obtiene la primera letra
        // CALCULO y SALIDA
        if(v1 < v2 && v1 < v3){
            System.out.printf("La primera letra que aparece en el abecedario es %c\n", v1);
        }else{
            if(v2 < v1 && v2 < v3){
                System.out.printf("La primera letra que aparece en el abecedario es %c\n", v2);
            }else{
                System.out.printf("La primera letra que aparece en el abecedario es %c\n", v3);
            }
        }
    }
    
}

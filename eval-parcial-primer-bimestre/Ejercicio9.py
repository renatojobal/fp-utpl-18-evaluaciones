package examenprimerparcial;

import java.util.Scanner;

/**
Ejercicio 9.- Dos triángulos son congruentes si tienen la misma forma y tamaño, es decir, su ángulos y lados
correspondientes son iguales. Elaborar un algoritmo que lea los tres ángulos y tres lados de dos
triángulos e imprima si son congruentes, caso contrario que imprima que no son congruentes.
@author Renato
*/
public class Ejercicio9 {
    public static void main(String[] args){
        // DECLARACION DE VARIABLES
        /*Se declara una variable para cada angulo y lado de ambos triángulos*/
        double anguloA1, anguloB1, anguloC1, anguloA2, anguloB2, anguloC2;
        double ladoa1, ladob1, ladoc1, ladoa2, ladob2, ladoc2;
        
    
        // INGRESO DE DATOS
        Scanner entrada = new Scanner(System.in);
        /*
          Se obtiene el varlo de cada angulo y lado de ambos triangulos
        */
        System.out.println("PRIMER TRIANGULO");
        // Angulos
        System.out.println("\t--Angulos--");
        System.out.println("\t\tIngrese el valor del ángulo A: ");
        anguloA1 = entrada.nextDouble();
        System.out.println("\t\tIngrese el valor del ángulo B: ");
        anguloB1 = entrada.nextDouble();
        System.out.println("\t\tIngrese el valor del ángulo C: ");
        anguloC1 = entrada.nextDouble();
        // Lados
        System.out.println("--Lados--");
        System.out.println("\t\tIngrese el valor del lado a: ");
        ladoa1 = entrada.nextDouble();
        System.out.println("\t\tIngrese el valor del lado b: ");
        ladob1 = entrada.nextDouble();
        System.out.println("\t\tIngrese el valor del lado c: ");
        ladoc1 = entrada.nextDouble();
        
        System.out.println("SEGUNDO TRIANGULO");
        // Anfulos
        System.out.println("\t\tIngrese el valor del ángulo A: ");
        anguloA2 = entrada.nextDouble();
        System.out.println("\t\tIngrese el valor del ángulo B: ");
        anguloB2 = entrada.nextDouble();
        System.out.println("\t\tIngrese el valor del ángulo C: ");
        anguloC2 = entrada.nextDouble();
        // Lados
        System.out.println("\t--Lados--");
        System.out.println("\t\tIngrese el valor del lado a: ");
        ladoa2 = entrada.nextDouble();
        System.out.println("\t\tIngrese el valor del lado b: ");
        ladob2 = entrada.nextDouble();
        System.out.println("\t\tIngrese el valor del lado c: ");
        ladoc2 = entrada.nextDouble();
        
        
        // CALCULO
        
        if((anguloA1 == anguloA2) && (anguloB1 == anguloB2) && (anguloC1 == anguloC2) && (ladoa1 == ladoa2) && (ladob1 == ladob2) && (ladoc1 == ladoc2)){
            System.out.println("Si son congruentes");
        }else{
            System.out.println("No son congruentes");
        }
        
        
        // SALIDA

    
    }
}

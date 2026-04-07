/**
 * 4. Escribir un programa que cuente el número de cifras que tiene un número (por
 * ejemplo, el 8 tiene una cifra, el 221 tres y el 456789 seis).
 */

import java.util.Scanner;

public class Ejercicio_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Dime un número: ");
        int num = sc.nextInt();

        int contador = 0;

        while (num != 0){
            num = num / 10;
            contador++;
        }
        System.out.println("Ese número tiene " + contador + " cifras.");
    }
}

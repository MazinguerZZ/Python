package Ejercicio_1;

import java.io.*;
import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        File fichero;

        while (true) {
            System.out.print("Introduce el nombre del fichero: ");
            String nombre = sc.nextLine();
            fichero = new File(nombre);

            if (!fichero.exists()) {
                System.out.println("El fichero " + nombre + " no existe");
            } else {
                break;
            }
        }

        System.out.print("Introduce la palabra a buscar: ");
        String palabra = sc.nextLine();

        int numLineas = 0;
        int numApariciones = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(fichero))) {
            String linea;

            while ((linea = br.readLine()) != null) {
                numLineas++;

                int index = 0;
                while ((index = linea.indexOf(palabra, index)) != -1) {
                    numApariciones++;
                    index += palabra.length();
                }
            }

            System.out.println("El fichero tiene " + numLineas + " líneas");
            System.out.println("La palabra " + palabra + " aparece " + numApariciones + " veces");

        } catch (IOException e) {
            System.out.println("Error al leer el fichero");
            e.printStackTrace();
        }

        sc.close();
    }
}
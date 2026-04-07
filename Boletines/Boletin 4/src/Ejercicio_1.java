import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Dame un número: ");
        int num = sc.nextInt();

        int resultado = 1;

        System.out.print(num + "! = ");

        for (int i = num; i > 0; i--) {
            resultado = resultado * i;

            System.out.print(i);

            if (i > 1) {
                System.out.print("*");
            }
        }
        System.out.println(" = " + resultado);
    }
}
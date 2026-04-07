import java.util.ArrayList;
import java.util.Random;

public class Ejercicio_1 {
    public static void main(String[] args) {
        ArrayList<Integer> loteria = new ArrayList<>();
        Random rand = new Random();

        while (loteria.size() < 6) {
            int numero = rand.nextInt(49) + 1;
            if (!loteria.contains(numero)) {
                loteria.add(numero);
            }
        }

        System.out.println("Primitiva: " + loteria);
    }
}
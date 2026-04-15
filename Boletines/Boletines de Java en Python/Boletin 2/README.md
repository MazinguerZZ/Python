# Ejercicios Genéricos de Programación 2

Este boletín de ejercicios está orientado a practicar con todo lo visto en el boletín 1.

---

1. Escribir un programa que nos pida tres palabras por teclado en cualquier orden y nos las muestre en pantalla ordenadas alfabéticamente en orden ascendente.

2. Ídem al anterior pero ordenando ahora en orden descendente.

3. Escribir un programa que pida un número por teclado al usuario que simule ser el precio de un artículo y escriba el resultado de aplicarle el IVA del 21%. El resultado debe de estar redondeado a dos decimales.

4. Escribir un programa que nos pida por teclado dos calificaciones numéricas de un alumno y nos muestre la media aritmética resultante redondeada sin decimales. Las notas introducidas deben de estar entre 0 y 10 y admiten decimales. En caso de que una entrada sea errónea debería de advertirnos de ello y no hacer el cálculo.

5. Escribir un programa que nos pida las notas obtenidas en un trimestre y nos muestre la media ponderada sabiendo que:
   1. La primera nota corresponde al trabajo en clase y cuenta como un **5%** del total.
   2. La segunda corresponde a los ejercicios prácticos: **15%**.
   3. La tercera la nota del examen: **80%**.

   El resultado debería de mostrarse de dos formas: redondeado con dos decimales (nota real) y redondeado sin decimales (nota de boletín).

6. Modificar el ejercicio anterior para que la nota del boletín se redondee matemáticamente si es superior a 5, pero se trunquen los decimales si es inferior a 5.

7. Escribir un programa que pida un número por teclado y nos imprima la tabla de multiplicar de dicho número del 1 al 10. Por ejemplo, si introducimos el 74 el resultado será algo así:

   ```
   74 x 1 = 74
   74 x 2 = 148
   …
   74 x 10 = 740
   ```

8. Escribir un programa que pida un número por teclado y escriba todos sus divisores separados por comas (evitando poner una coma al final). Por ejemplo, si el número introducido es el 14 tu programa debería de mostrar lo siguiente:

   ```
   Divisores del número 14: 1, 2, 7, 14
   ```

9. Escribir un programa que pida números entre el 1 y el 100 por teclado hasta que escribamos la palabra `FIN` (con mayúsculas). Si el usuario introduce una entrada inválida (números superiores a 100, otras cadenas de caracteres que no sean `FIN`, etc.) no se tendrá en cuenta pero se mostrará un mensaje de error y el programa seguirá su curso. Cuando terminamos (al introducir la palabra `FIN`) mostraremos por pantalla el número de entradas válidas que hemos hecho (sin contar esta última, que sólo sirve para finalizar el programa).

10. Modificar el programa anterior para que nos muestre al final la media aritmética de las entradas válidas.

11. Modificar el programa anterior para que, además, nos diga al final cuál ha sido el número mayor y el menor que has introducido.

12. Realizar un juego en el que debes de acertar un número entre el 1 y el 50 que el ordenador ha elegido de forma aleatoria. El programa te indicará si has acertado, si te has pasado o si te has quedado corto. El programa finaliza cuando se acierta o cuando se superan el número máximo de intentos establecido en 5.

13. Modificar el programa anterior para que el programa te dé todos los intentos que necesites pero que cuando aciertes te informe de cuántas veces has fallado antes de lograrlo.

14. Modificar el programa anterior para que al final del programa te pida si quieres volver a jugar y en caso afirmativo comience una nueva partida.

15. Modificar el programa anterior para que al iniciar el juego te pida dos parámetros con objeto de cambiar la dificultad del juego: el número máximo (antes era siempre 50) y el número de intentos posibles (antes era siempre 5).

16. Escribir un programa que pida por teclado el radio de una circunferencia, admitiendo valores con decimales, y calcule la longitud y el área de la circunferencia (redondeando a cinco decimales). Las fórmulas son las siguientes:

    ```
    area     = 3.14159 * radio²
    longitud = 2 * 3.14159 * radio
    ```

17. Escribir un programa que reciba por teclado una temperatura en cualquiera de las tres unidades básicas (Celsius, Fahrenheit o Kelvin) y la devuelva en las otras dos. Tu programa reconocerá la unidad utilizada porque irá acompañada de una letra indicativa. Por ejemplo: `12C`, `280.57K` o `98.6F`. Se admitirán decimales en la entrada y se devolverá el resultado con dos decimales.

    Las fórmulas de conversión entre unidades son las siguientes:

    | Conversión | Fórmula |
    |---|---|
    | ºC → ºF | `ºF = ºC × 1.8 + 32` |
    | ºF → ºC | `ºC = (ºF - 32) ÷ 1.8` |
    | ºK → ºC | `ºC = ºK - 273.15` |
    | ºC → ºK | `ºK = ºC + 273.15` |
    | ºF → ºK | `ºK = 5/9 × (ºF - 32) + 273.15` |
    | ºK → ºF | `ºF = 1.8 × (ºK - 273.15) + 32` |

18. La tabla de tarifas impositivas en España para 2022 es la siguiente:

    | Base imponible (desde) | Base imponible (hasta) | Retención |
    |---|---|---|
    | 0 € | 12.450 € | 19 % |
    | 12.450 € | 20.200 € | 24 % |
    | 20.200 € | 35.200 € | 30 % |
    | 35.200 € | 60.000 € | 37 % |
    | 60.000 € | 300.000 € | 45 % |
    | Más de 300.000 € | — | 47 % |

    Escribir un programa que le pida al usuario su sueldo anual (puede ser un número con decimales) y le informe qué porcentaje de retención le corresponde, el importe de la misma y el importe neto restante que cobrará.

---

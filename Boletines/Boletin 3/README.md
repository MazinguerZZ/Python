# Ejercicios Genéricos de Programación 3

Este boletín de ejercicios está orientado a practicar con todo lo visto en boletines anteriores incluyendo, además:

- Cadenas de caracteres
- Uso de `switch`, `match` o una instrucción similar

---

1. Escribir un programa que pida una contraseña por teclado (dos veces) y si no coinciden nos la vuelva a pedir hasta que lo hagan.

2. Modificar el programa anterior para que cuando coincidan ambas contraseñas nos informe del número de intentos inválidos.

3. Escribir un programa que nos pida nuestro nombre y apellidos (dos peticiones diferentes hechas en ese orden) y nos lo escriba formateado de la siguiente forma:

   ```
   Morales Vázquez, José María
   ```

4. Escribir un programa que pida por teclado una cadena de texto y la escriba sin espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios que ha encontrado y suprimido.

5. Escribir un programa que pida por teclado una cadena de texto y la imprima escrita al revés. Es decir, si el usuario escribe `Hola Mundo` el programa debería de escribir `odnuM aloH`.

6. Escribir un programa que pida por teclado una cadena de texto y la separe en dos distintas. En la primera estarían las letras que ocupan una posición par y en la segunda las que ocupan una posición impar. Por ejemplo, si el usuario escribe `Hola Mundo` la primera cadena sería `Hl ud` y la segunda `oaMno`.

7. Escribir un programa que pida por teclado una cadena de texto y la escriba con el alfabeto típico de los hackers sustituyendo:
   - la letra `a` por el número `4`
   - la letra `e` por el número `3`
   - la letra `i` por el número `1`
   - la letra `o` por el número `0`

   Considera que las vocales pueden estar escritas en mayúsculas o minúsculas, pero no hace falta tener en cuenta que además podrían ir acentuadas.

8. Escribir un programa que reciba una cadena de texto por teclado y la muestre sin vocales. Por ejemplo, si recibe la cadena `"Hola Mundo"` debería de devolver `"Hl Mnd"`.

9. Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia, Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cuál es la capital de nuestro destino (París, Roma, Santiago de Chile o Tokio).

10. Escribir un programa que valide si un NIF español introducido por teclado es correcto. La longitud exacta de la cadena ha de ser de 9 caracteres. Los ocho primeros han de ser números comprendidos entre el 0 y el 9, y el último una letra que puede estar escrita en mayúsculas o minúsculas.

11. Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos comunique, además de si es válido, de qué tipo es.

    Un NIE es una cadena de 9 caracteres que siempre empieza por `X`, `Y` o `Z`, a continuación vienen 7 cifras y una letra final. Las letras inicial y final pueden estar escritas en mayúsculas o en minúsculas.

12. Las matrículas españolas constan de un número de cuatro dígitos y tres letras cualesquiera en mayúsculas, a excepción de las vocales, la `Ñ` y la `Q`. Escribir un programa que detecte si una matrícula introducida por teclado es válida o no.

13. Modificar el programa anterior contemplando que entre los números y las letras podría haber un espacio en blanco (uno solo) o un guión. En ambos casos se considerará también que la matrícula es válida (si cumple todo lo demás).

14. Modificar el programa que validaba si un NIF era correcto comprobando si la letra que incorpora lo es. El método de cálculo es el siguiente:

    ### ¿Cómo calcular la letra del NIF?

    Para obtener la letra del NIF se deben sumar las ocho cifras del código numérico del DNI, dividir el cómputo total entre 23 y quedarse con el resto de esta operación. El resultado del resto será un número entre 0 y 22. A cada uno de estos números le corresponderá una letra, según la siguiente tabla:

    | RESTO | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
    |-------|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|-----|
    | LETRA | T | R | W | A | G | M | Y | F | P | D | X  | B  | N  | J  | Z  | S  | Q  | V  | H  | L  | C  | K  | E  |

15. Escribir un programa que reciba por teclado una fecha en el formato `DD/MM/YYYY`. El programa debe de comprobar si la fecha es correcta teniendo en cuenta:
    - Que el formato sea el correcto.
    - Que la fecha sea totalmente válida teniendo en cuenta incluso los años bisiestos (aquellos que son divisibles entre cuatro).

---


# Ejercicios con Python 6

Este boletín de ejercicios está orientado a practicar con funciones.

---

**1.** Escribir una función en Python que reciba dos argumentos: el precio y el IVA, y calcule y devuelva el PVP una vez aplicado el IVA con dos decimales.

| Invocación de la función | Resultado en la consola |
|--------------------------|-------------------------|
| `print(pvp(14, 0))`      | `14`                    |
| `print(pvp(34.4, 21))`   | `41.62`                 |

---

**2.** Escribir una función en Python que genere de forma consecutiva tiradas de dados aleatorios entre el 1 y el 6 (ambos incluidos) y los muestre en pantalla, finalizando la ejecución cuando el valor de todos los dados es el mismo. Al finalizar debe decir cuántas veces ha tenido que lanzar los dados para alcanzar ese valor.

| Invocación de la función | Resultado en la consola |
|--------------------------|-------------------------|
| `tiradadosmultiple(3)`   | `2 – 5 - 1` |
|                          | `4 – 1 - 4` |
|                          | `4 – 6 - 6` |
|                          | `3 – 3 - 3` |
|                          | `He tenido que lanzar los dados 4 veces para que todos sean iguales` |

---

**3.** Escribir una función en Python que reciba una cadena de texto y un carácter y la escriba al revés suprimiendo las apariciones de ese carácter.

| Invocación de la función | Resultado en la consola |
|--------------------------|-------------------------|
| `volteayelmimina("Hola mundo cruel", "o")` | `La cadena al revés y sin el carácter 'o' es: leurc dnum alH` |
|  | `He eliminado 2 caracteres` |

---

**4.** Escribir una función en Python que reciba una cadena de texto que representa una fracción y devuelva su valor en decimal. La fracción tiene que ser introducida con el formato `numerador/denominador`, siendo numerador y denominador dos números enteros. Si se introduce algo que no corresponda con esto, debería de devolver un cero.

| Invocación de la función   | Resultado en la consola |
|----------------------------|-------------------------|
| `print(fraccion("25/10"))` | `2.5`                   |
| `print(fraccion("a/10"))`  | `0`                     |
| `print(fraccion("//10"))`  | `0`                     |
| `print(fraccion("10"))`    | `0`                     |

---

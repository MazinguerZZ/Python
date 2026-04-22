# Kata: Las Expresiones Importan
**Dificultad:** 1/8

---

## 📝 Enunciado

Dados tres enteros `a`, `b` y `c`, devuelve el número más grande que se puede obtener insertando los operadores `+`, `*` y paréntesis `()`. Es decir, prueba todas las combinaciones posibles de `a`, `b` y `c` con los operadores, sin reordenar los operandos, y devuelve el valor máximo.

### Ejemplo

Con los números 1, 2 y 3, algunas expresiones posibles son:

* `1 * (2 + 3) = 5`
* `1 * 2 * 3 = 6`
* `1 + 2 * 3 = 7`
* `(1 + 2) * 3 = 9`

El valor máximo que se puede obtener es **9**.

### Notas

* Los números son siempre positivos, en el rango `1 ≤ a, b, c ≤ 10`.
* Puedes usar la misma operación más de una vez.
* No es obligatorio usar todos los operadores o paréntesis.
* No puedes cambiar el orden de los operandos. Por ejemplo, con los números dados no puedes obtener la expresión `(1 + 3) * 2 = 8`.

### Ejemplos de entrada y salida

* `expressionsMatter(1, 2, 3) ==> 9`, porque `(1 + 2) * 3 = 9`
* `expressionsMatter(1, 1, 1) ==> 3`, porque `1 + 1 + 1 = 3`
* `expressionsMatter(9, 1, 1) ==> 18`, porque `9 * (1 + 1) = 18`
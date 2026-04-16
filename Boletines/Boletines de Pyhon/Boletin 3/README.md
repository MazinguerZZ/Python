# Ejercicios con Python 3

Este boletín de ejercicios está orientado a seguir practicando con estructuras de control y todo lo visto anteriormente pero se centra, además, en el manejo y gestión de cadenas de texto.

---

**1.** Escribir un programa en Python que pida al usuario una cadena de texto y la escriba sin espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios que ha encontrado y suprimido.

**2.** Escribir un programa que pida al usuario que escriba una cadena de texto y la imprima escrita al revés (es decir, si el usuario escribe `Hola Mundo` el programa debería de escribir `odnuM aloH`).

**3.** Escribir un programa que pida al usuario que escriba una cadena y la separe en dos distintas. En la primera de ellas estarían las letras que ocupan una posición par y en la segunda las que ocupan una posición impar. Por ejemplo, si el usuario escribe `Hola Mundo` la primera cadena sería `Hl ud` y la segunda `oaMno`.

**4.** Escribir un programa que pida al usuario una cadena de texto y la escriba con el alfabeto típico de los hackers sustituyendo las letras `a` por el número `4`, las letras `e` por el número `3`, las letras `i` por el número `1` y las letras `o` por el número `0`. Considera que las vocales pueden estar escritas en mayúsculas o minúsculas y tiene que funcionar con ambas, pero no hace falta que tengas en cuenta que además podrían ir acentuadas.

> **PISTA:** se hace más fácilmente con un `switch`.

**5.** Escribir un programa Python que reciba una cadena de texto y la muestre sin vocales. Por ejemplo, si recibe la cadena `"Hola Mundo"` debería de devolver `"Hl Mnd"`.

**6.** Escribe un programa en Python que valide si un NIF español es correcto. La longitud exacta de la cadena ha de ser de 9 caracteres. Los ocho primeros han de ser números comprendidos entre el 0 y el 9 y el último una letra, no importa que esté en mayúsculas o minúsculas. Usa para ello las funciones `isdigit` e `isalpha`:
[https://initialcommit.com/blog/python-isalpha-string-method](https://initialcommit.com/blog/python-isalpha-string-method)

**7.** Mejorar el programa anterior para que detecte si se trata de un NIF, un NIE o un CIF de empresa y nos comunique, además de si es válido, de qué tipo es.

- Un **CIF** es una cadena de 9 caracteres pero en este caso la primera es una letra y las otras ocho cifras.
- Un **NIE** es una cadena de 9 caracteres que siempre empieza por `X`, `Y` o `Z` y a continuación vienen 7 cifras y una letra final.

**8.** Las matrículas españolas constan de un número de cuatro dígitos y tres letras cualesquiera en mayúsculas a excepción de la `Ñ` y la `Q`. Escribe un programa en Python que detecte si una matrícula introducida por el usuario es válida o no.

---

**9.** La tabla de tarifas impositivas en España para 2022 es la siguiente:

### Tabla del IRPF de España para 2022

| Base imponible (desde) | Base imponible (hasta) | Retención |
|------------------------|------------------------|-----------|
| 0 €                    | 12.450 €               | 19 %      |
| 12.450 €               | 20.200 €               | 24 %      |
| 20.200 €               | 35.200 €               | 30 %      |
| 35.200 €               | 60.000 €               | 37 %      |
| 60.000 €               | 300.000 €              | 45 %      |
| Más de 300.000 €       | —                      | 47 %      |

Escribe un programa en Python que le pida al usuario su sueldo anual (puede ser un número con decimales) y le informe qué porcentaje de retención le corresponde, el importe de la misma y el importe neto restante que cobrará.

---

**10.** Haz un programa en Python que te calcule la letra del NIF. La forma de hacerlo es la siguiente:

## ¿Cómo calcular la letra del NIF?

Para obtener la letra del NIF deberemos tomar de sumar las ocho cifras del código numérico del DNI, dividir el cómputo total entre 23 y quedarnos con el resto de esta operación. El resultado del resto será un número entre 0 y 22. A cada uno de estos números le corresponderá una letra, según la siguiente tabla:

| RESTO | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|-------|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|-----|
| LETRA | T | R | W | A | G | M | Y | F | P | D | X  | B  | N  | J  | Z  | S  | Q  | V  | H  | L  | C  | K  | E  |

> **NOTA:** cuando aprendamos a manejarnos con colecciones y listas será mucho más fácil hacer esto. Por el momento puedes hacerlo con un `match` enooooorme!

---

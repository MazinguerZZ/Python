# Ejercicios con Python 5

Este boletín de ejercicios está orientado a practicar con todo lo visto hasta ahora.

---

**1.** Escribir un programa que genere una lista con 10 números aleatorios comprendidos entre el 1 y el 500 y la muestre por pantalla ordenada. A continuación nos debería de pedir un número por teclado y decirnos si está o no en la lista y cuántos de los números son menores al que le hemos dado.

**2.** Escribir un programa que nos pida el nombre, el nombre de la asignatura y las notas de un alumno de cada uno de los tres trimestres y lo almacene todo en una lista. Luego lo debería de mostrar todo en pantalla junto con la media que correspondería a la nota final. Un ejemplo de la salida por pantalla sería así:

```
Nombre: José María Morales
Asignatura: Python
Nota del primer trimestre: 8.5
Nota del segundo trimestre: 9.5
Nota del tercer trimestre: 10.0
Nota media final: 9.0
```

**3.** Escribir un programa que vaya llenando una lista con números hasta que introduzcamos uno negativo. En ese momento debe de parar y mostrarnos la lista ordenada ascendente y descendentemente.

> **NOTA:** Si introducimos algo que no sea un número debería de advertirnos, no introducirlo en la lista pero continuar la introducción de datos.

**4.** Crea un programa que pida al usuario un número de mes (por ejemplo, el `4`) y un año (por ejemplo `2022`) y diga cuántos días tiene (por ejemplo, `30`) y el nombre del mes. Hazlo usando listas. Recuerda que febrero tiene 29 días cuando el año es divisible por 4 y 28 el resto de los años.

**5.** Una lotería primitiva está formada por seis números y otro adicional para el reintegro. Los seis primeros números están comprendidos entre el 1 y el 49 (ambos inclusive) y no pueden estar repetidos. El reintegro es un número entre el 0 y el 9. Haced un programa en Python que calcule una combinación de números de forma aleatoria para la primitiva cumpliendo las normas explicadas antes y que luego la muestre por pantalla ordenada de menor a mayor. Lógicamente, también debería de mostrar el complementario.

**6.** La siguiente tabla muestra la población de los 20 países con más habitantes del mundo actualizada al año 2021:

### Comparativa: Población 2021

| País                                | Fecha | Densidad | Población     | Var.     |
|-------------------------------------|-------|----------|---------------|----------|
| China                               | 2021  | 147      | 1.412.360.000 | 0,02%    |
| India                               | 2021  | 424      | 1.393.409.033 | 0,97%    |
| Estados Unidos                      | 2021  | 34       | 332.183.000   | 0,29%    |
| Indonesia                           | 2021  | 142      | 272.249.000   | 0,76%    |
| Pakistán                            | 2021  | 280      | 222.590.000   | 1,99%    |
| Brasil                              | 2021  | 25       | 213.993.441   | 1,06%    |
| Nigeria                             | 2021  | 229      | 211.400.704   | 2,55%    |
| Bangladés                           | 2021  | 1.127    | 166.303.494   | 0,98%    |
| Rusia                               | 2021  | 9        | 145.558.000   | -0,42%   |
| México                              | 2021  | 66       | 130.262.220   | 1,93%    |
| Japón                               | 2021  | 333      | 125.681.593   | -0,46%   |
| Filipinas                           | 2021  | 367      | 110.200.000   | 1,31%    |
| Egipto                              | 2021  | 102      | 102.100.000   | 1,49%    |
| Etiopía                             | 2021  | 88       | 99.701.000    | 2,60%    |
| Viet Nam                            | 2021  | 296      | 98.168.829    | 0,60%    |
| República Democrática del Congo     | 2021  | 39       | 92.377.986    | 1,74%    |
| Irán                                | 2021  | 49       | 84.841.000    | 0,96%    |
| Türkiye                             | 2021  | 108      | 84.680.273    | 1,27%    |
| Alemania                            | 2021  | 233      | 83.237.124    | 0,10%    |
| Tailandia                           | 2021  | 136      | 69.951.000    | 0,22%    |

Haced un programa en Python que permita cargar estos datos (nombre del país y población, solamente) desde el teclado. Los países deberían de estar en una lista y los datos de población en otra diferente, pero las posiciones deberían de coincidir. Es decir, si Pakistán ocupa la posición 5 en una lista, su población debería de ocupar la misma posición en la otra para que exista una correspondencia.

La entrada de datos finaliza cuando se introduzca un `-1` como nombre de un país. En ese momento el programa debería de listar los países con sus poblaciones respectivas.

> **NOTA:** No es preciso que metas los 20 datos para probar que tu programa funciona. Seguramente te bastará con tres o cuatro…

**7.** Haced ahora un programa donde las listas conteniendo los países y sus poblaciones ya vienen escritas en el código. Tu programa ahora tendrá que pedir el nombre de un país por teclado y mostrar su población. Si el país que se pide no está en la lista debería de informar de ello.

---

# 13. Romano a Entero

Resuelta · Fácil

Los números romanos se representan con siete símbolos diferentes: `I`, `V`, `X`, `L`, `C`, `D` y `M`.

```
Símbolo      Valor
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

Por ejemplo, el `2` se escribe como `II` en números romanos, simplemente dos unos sumados. El `12` se escribe como `XII`, que es simplemente `X + II`. El número `27` se escribe como `XXVII`, que es `XX + V + II`.

Los números romanos se escriben normalmente de mayor a menor de izquierda a derecha. Sin embargo, el numeral para el cuatro no es `IIII`. En su lugar, el cuatro se escribe como `IV`. Como el uno está antes del cinco, se resta, dando como resultado cuatro. El mismo principio se aplica al número nueve, que se escribe como `IX`. Hay seis casos en los que se usa la sustracción:

* `I` puede colocarse antes de `V` (5) y `X` (10) para formar 4 y 9.
* `X` puede colocarse antes de `L` (50) y `C` (100) para formar 40 y 90.
* `C` puede colocarse antes de `D` (500) y `M` (1000) para formar 400 y 900.

Dado un número romano, conviértelo a entero.

**Ejemplo 1:**

```
Entrada: s = "III"
Salida: 3
Explicación: III = 3.
```

**Ejemplo 2:**

```
Entrada: s = "LVIII"
Salida: 58
Explicación: L = 50, V = 5, III = 3.
```

**Ejemplo 3:**

```
Entrada: s = "MCMXCIV"
Salida: 1994
Explicación: M = 1000, CM = 900, XC = 90 e IV = 4.
```

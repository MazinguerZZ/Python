# P2. Baraja el Arreglo

**Dificultad:** Fácil

Dado el arreglo `nums` que consta de `2n` elementos en la forma `[x1, x2, ..., xn, y1, y2, ..., yn]`.

Devuelve el array en el formato `[x1, y1, x2, y2, ..., xn, yn]`.

---

**Ejemplo 1:**

```
Input:  nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explicación: x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 → [2,3,5,4,1,7]
```

**Ejemplo 2:**

```
Input:  nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
```

**Ejemplo 3:**

```
Input:  nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
```

---

**Restricciones:**

- `1 <= n <= 500`
- `nums.length == 2n`
- `1 <= nums[i] <= 10^3`
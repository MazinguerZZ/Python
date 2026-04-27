# Q1. Concatenation of Array

**Dificultad:** Fácil

Dado un array de enteros `nums` de longitud `n`, se quiere crear un array `ans` de longitud `2n` donde `ans[i] == nums[i]` y `ans[i + n] == nums[i]` para `0 <= i < n` (indexado desde 0).

En concreto, `ans` es la concatenación de dos arrays `nums`.

Devuelve el array `ans`.

---

**Ejemplo 1:**

```
Input:  nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explicación:
- ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]
- ans = [1, 2, 1, 1, 2, 1]
```

**Ejemplo 2:**

```
Input:  nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explicación:
- ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]
- ans = [1, 3, 2, 1, 1, 3, 2, 1]
```

---

**Restricciones:**

- `n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`
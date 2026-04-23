# Kata: Elige los Primeros Elementos
**Dificultad:** 1/8

---

## 📝 Enunciado

Escribe una función que devuelva el/los primero(s) elemento(s) de una secuencia. Pasando un parámetro `n` (por defecto `1`) devolverá los primeros `n` elementos.

Si `n` == `0` devuelve una secuencia vacía `[]`.

### Ejemplos

```python
arr = ['a', 'b', 'c', 'd', 'e']
first(arr)    # --> ['a']
first(arr, 2) # --> ['a', 'b']
first(arr, 3) # --> ['a', 'b', 'c']
first(arr, 0) # --> []
```
# 22 – La Prueba de los Elementos

Te encuentras ante una prueba ancestral. Debes combinar elementos para abrir la puerta. Se te dan dos listas: una con elementos de fuego (`'fuego'`), agua (`'agua'`), tierra (`'tierra'`) y aire (`'aire'`), y otra con las combinaciones necesarias para abrir la puerta. Crea una función que reciba la lista de elementos disponibles y la combinación requerida, y devuelva `True` si la combinación está presente en los elementos disponibles, y `False` en caso contrario. Recuerda que el orden de los elementos no importa, y que un elemento puede aparecer varias veces.

---

| Valor de Entrada                                                        | Valor Esperado |
|-------------------------------------------------------------------------|----------------|
| `(["fuego", "agua", "tierra", "aire"], ["fuego", "agua"])`              | `"True"`       |
| `(["fuego", "fuego", "tierra"], ["fuego", "agua"])`                     | `"False"`      |
| `(["agua", "tierra", "aire", "agua"], ["agua", "agua", "tierra"])`      | `"True"`       |
| `(["fuego"], ["fuego", "fuego"])`                                       | `"False"`      |
| `(["fuego", "agua", "tierra", "aire", "fuego"], ["fuego", "aire", "fuego"])` | `"True"`  |

> - **Valor de Entrada:** El valor de entrada de la prueba.
> - **Valor Esperado:** El valor esperado de respuesta de la prueba.

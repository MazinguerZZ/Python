# 16 – Gestionar el Inventario del Héroe

Escribe una función que reciba una lista de objetos, un objeto nuevo, un tamaño máximo de inventario y una acción. Devuelve el inventario actualizado después de añadir o eliminar el objeto, según corresponda.

---

| Valor de Entrada                                             | Valor Esperado                    |
|--------------------------------------------------------------|-----------------------------------|
| `(["espada", "escudo"], "poción", 3, "agregar")`             | `"['espada', 'escudo', 'poción']"` |
| `(["espada", "escudo", "poción"], "arco", 3, "agregar")`     | `"['espada', 'escudo', 'poción']"` |
| `(["espada", "poción"], "escudo", 3, "eliminar")`            | `"['espada', 'poción']"`           |
| `(["espada", "escudo", "arco"], "arco", 3, "eliminar")`      | `"['espada', 'escudo']"`           |

> - **Valor de Entrada:** El valor de entrada de la prueba.
> - **Valor Esperado:** El valor esperado de respuesta de la prueba.

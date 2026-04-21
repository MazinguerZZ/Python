# 26 – Generar Nombres Épicos de Monstruos

Para poblar las mazmorras y enfrentarse a héroes, necesitas generar nombres de monstruos épicos. Escribe una función que reciba una lista de prefijos y sufijos, y devuelva todas las combinaciones posibles de prefijos y sufijos concatenados. Además, si se proporciona una lista de títulos (como `'Rey'`, `'Señor'`, `'Dios'`), la función debe agregar esos títulos a las combinaciones.

---

| Valor de Entrada | Valor Esperado |
|------------------|----------------|
| `(["Gran", "Pequeño"], ["Goblin", "Orco"], [])` | `"['Gran Goblin', 'Gran Orco', 'Pequeño Goblin', 'Pequeño Orco']"` |
| `(["Oscuro", "Nocturno"], ["Espectro", "Vampiro"], [])` | `"['Oscuro Espectro', 'Oscuro Vampiro', 'Nocturno Espectro', 'Nocturno Vampiro']"` |
| `(["Furioso", "Escarlata"], ["Draco", "Lobo"], ["Rey", "Señor"])` | `"['Rey Furioso Draco', 'Rey Furioso Lobo', 'Rey Escarlata Draco', 'Rey Escarlata Lobo', 'Señor Furioso Draco', 'Señor Furioso Lobo', 'Señor Escarlata Draco', 'Señor Escarlata Lobo']"` |

> - **Valor de Entrada:** El valor de entrada de la prueba.
> - **Valor Esperado:** El valor esperado de respuesta de la prueba.

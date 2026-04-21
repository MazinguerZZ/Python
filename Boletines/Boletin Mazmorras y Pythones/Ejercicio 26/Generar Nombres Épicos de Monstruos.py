def generar_nombre_monstruo(prefijos, sufijos, titulos):
    lista = []

    for prefijo in prefijos:
        for sufijo in sufijos:
            nombre = prefijo + " " + sufijo
            lista.append(nombre)

    if titulos:
        resultado_final = []
        for titulo in titulos:
            for nombre in lista:
                resultado_final.append(titulo + " " + nombre)

        return resultado_final
    return lista

print(generar_nombre_monstruo(["Gran", "Pequeño"], ["Goblin", "Orco"], []))
print(generar_nombre_monstruo(["Oscuro", "Nocturno"], ["Espectro", "Vampiro"], []))
print(generar_nombre_monstruo(["Furioso", "Escarlata"], ["Draco", "Lobo"], ["Rey", "Señor"]))
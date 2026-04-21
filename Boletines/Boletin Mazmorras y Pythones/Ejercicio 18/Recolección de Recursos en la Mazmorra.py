def recolectar_recurso(recursos, recurso_buscado):
    for recurso in recursos:
        if recurso == recurso_buscado:
            return f"Has recolectado {recurso_buscado}!"
        else:
            return f"{recurso_buscado} no está disponible en la mazmorra."



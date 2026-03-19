from datetime import date, time, datetime, timedelta

hoy = date.today()
print(hoy)
ahora = datetime.now()
print(ahora)

hora = time(7, 22, 14)
fecha = date(2020, 12, 31)
momento = datetime(1968, 10, 8, 18, 15)
print(fecha)
print(hora)
print(momento)

formateado = momento.strftime("%A %d-%B-%Y")
print(formateado)

texto = "2025-01-03 14:30"
formato = "%Y-%m-%d %H:%M"
objeto = datetime.strptime(texto, formato)
print(objeto)
print(objeto.year)
print(objeto.day)

# srtftime convierte un objeto a una cadena de texto
# strptime convierte una cadena de texto a objeto


fechafuturo = objeto - timedelta(days=3527, hours=5
                                 , weeks=12)
print(fechafuturo)
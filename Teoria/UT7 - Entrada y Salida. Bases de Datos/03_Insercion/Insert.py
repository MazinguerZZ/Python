import mysql.connector

try:
    connect = mysql.connector.connect(user='dam2', password='asdf.1234', host='localhost', database='adat8')
    cursor = connect.cursor()
    
    # Datos a insertar
    titulo = "Mi Nuevo Album"
    artista_id = 1
    
    # Inserción simple
    sql = "INSERT INTO Album (Title, ArtistId) VALUES (%s, %s)"
    valores = (titulo, artista_id)
    
    cursor.execute(sql, valores)
    connect.commit()  # IMPORTANTE: guardar los cambios
    
    print("Álbum insertado correctamente")
    print("ID del nuevo álbum:", cursor.lastrowid)
    
    cursor.close()
    connect.close()
    
except mysql.connector.Error as err:
    print("Error:", err)
import mysql.connector

try:
    connect = mysql.connector.connect(user='dam2', password='asdf.1234', host='localhost', database='adat8')
    cursor = connect.cursor()
    
    # Desactivar autocommit (opcional, por defecto ya está desactivado)
    connect.autocommit = False
    
    # Ver datos antes
    cursor.execute("SELECT * FROM Album WHERE ArtistId = 1")
    print("Antes:", cursor.fetchall())
    
    # Operación 1: Insertar
    cursor.execute("INSERT INTO Album (Title, ArtistId) VALUES (%s, %s)", ("Album Transacción", 1))
    
    # Operación 2: Actualizar
    cursor.execute("UPDATE Album SET Title = 'Modificado' WHERE AlbumId = 350")
    
    # Si todo va bien, confirmamos
    connect.commit()
    print("Transacción completada")
    
    # Ver datos después
    cursor.execute("SELECT * FROM Album WHERE ArtistId = 1")
    print("Después:", cursor.fetchall())
    
    cursor.close()
    connect.close()
    
except mysql.connector.Error as err:
    print("Error:", err)
    print("Haciendo rollback...")
    connect.rollback()  # Deshacer cambios si hay error
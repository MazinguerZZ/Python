import mysql.connector

try:
    connect = mysql.connector.connect(user='dam2', password='asdf.1234', host='localhost', database='adat8')
    cursor = connect.cursor()
    
    # 1. Insertamos un álbum
    cursor.execute("INSERT INTO Album (Title, ArtistId) VALUES (%s, %s)", ("Álbum Bueno", 1))
    print("Primer INSERT correcto")
    
    # 2. Intentamos insertar uno con error (ArtistId muy grande para causar error)
    cursor.execute("INSERT INTO Album (Title, ArtistId) VALUES (%s, %s)", ("Álbum Error", 999999))
    print("Segundo INSERT correcto")  # Esta línea no se ejecutará si hay error
    
    # Si llegamos aquí, todo OK
    connect.commit()
    print("TODO CORRECTO - COMMIT realizado")
    
except mysql.connector.Error as err:
    print("ERROR:", err)
    print("Haciendo rollback - se deshacen todos los cambios")
    connect.rollback()  # Deshace el primer INSERT también
    
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connect' in locals() and connect.is_connected():
        connect.close()
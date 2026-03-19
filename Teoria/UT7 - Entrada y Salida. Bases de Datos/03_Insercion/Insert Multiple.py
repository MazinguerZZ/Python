import mysql.connector

try:
    connect = mysql.connector.connect(user='dam2', password='asdf.1234', host='localhost', database='adat8')
    cursor = connect.cursor()
    
    # Múltiples álbumes a insertar
    albumes = [
        ("Album Rock 1", 1),
        ("Album Rock 2", 1),
        ("Balada Romantica", 2),
        ("Musica Clasica", 3)
    ]
    
    sql = "INSERT INTO Album (Title, ArtistId) VALUES (%s, %s)"
    
    cursor.executemany(sql, albumes)
    connect.commit()
    
    print("Álbumes insertados:", cursor.rowcount)
    
    cursor.close()
    connect.close()
    
except mysql.connector.Error as err:
    print("Error:", err)
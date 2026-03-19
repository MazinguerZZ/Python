import mysql.connector

try:
    connect = mysql.connector.connect(user='dam2', password='asdf.1234', host='localhost', database='adat8')
    cursor = connect.cursor()
    id = 341
    sql1 = "SELECT * from Album where AlbumId = " + str(id)
    sql2 = "UPDATE Album SET  Title = 'Los pajaritos' WHERE AlbumId = " + str(id) # Sin los commit, los datos no se actulizan en la BBDD
    cursor.execute(sql1)
    resultado = cursor.fetchall()
    print(resultado)
    print(cursor.execute(sql2))
    cursor.execute(sql1)
    resultado = cursor.fetchall()
    print(resultado)
    connect.commit()
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)
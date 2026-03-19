import mysql.connector

try:
    connect = mysql.connector.connect(user='dam2', password='asdf.1234', host='localhost', database='adat8')
    cursor = connect.cursor()
    # Metodo 1 de select
    cursor.execute('select title, AlbumId from Album where AlbumId = 347')

    # Metodo 2 de select
    # id = 347
    # sql = "select title, AlbumId from Album where AlbumId = " + str(id)
    # cursor.execute(sql)

    # Metodo 1
    # for fila in cursor:
    #     print(fila)

    # Metodo 2
    tupla = cursor.fetchall()
    if len(tupla) == 0:
        print('El select no devuelve datos')
    else:
        print(tupla)

    # Metodo 3
    # for title, AlbumId in cursor:
        # print("(", AlbumId, ")", title )

    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)
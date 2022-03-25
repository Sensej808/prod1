import psycopg2
from config import *

global connection

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "SELECT version();"
    #     )
    #     print(f"Server version:  {cursor.fetchone()}")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE offers(
    #         num serial PRIMARY KEY,
    #         read int,
    #         id int,
    #         name varchar(50) NOT NULL,
    #         offer text);"""
    #     )

    #    print("Table created successfully")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         f"""SELECT offer FROM offers WHERE read = {0};"""
    #     )
    #     print(cursor.fetchone())
    #     cursor.execute(
    #         """UPDATE offers SET read = 1;"""
    #     )

    with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM offers WHERE Id > 0"""
        )
        print("Data was successfully inserted")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE Id = 1;"""
    #     )
    #     print(cursor.fetchone())

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE offers;"""
    #     )


except Exception as _ex:
    print("Error:", _ex)
finally:
    if connection:
        connection.close()
        print("Connection closed")

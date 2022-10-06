import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port)
        print(" Connection with the bank ", db_name, " wass successful ")
    except OperationalError as e:
        print(f"An error '{e}' ocurred")
    return connection


def create_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Tabble create sucessfully !")
        cursor.close()
    except OperationalError as e:
        print(f"An error '{e}' ocurred")

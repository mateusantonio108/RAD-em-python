import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = none
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port)
        print(" Connection with the bank ", db_name, " wass sucessfully")
    except OperationalError as e:
        print(f" An error '{e} ocurred ")
    return connection


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query):
        print("Query executed sucessfully")
    except OperationalError as e:
        print(f"An error '{e}' ocurred")


def create_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("table create!")
    except OperationalError as e:
        print(f"An error '{e} ocurred")


conection = create_connection("postgres", "postgres", "admin", "127.0.0.1", "1234")

create_database_query = "CREATE DATABASE BB"
create_database(connection, create_database_query)

connection.close()

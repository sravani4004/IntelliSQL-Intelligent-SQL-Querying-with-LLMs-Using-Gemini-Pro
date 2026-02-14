import mysql.connector


def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",
            database="intellisql"
        )

    except:
        return None
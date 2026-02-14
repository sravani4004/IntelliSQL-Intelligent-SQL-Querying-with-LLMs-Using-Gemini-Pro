from db_config import get_connection


def execute_query(query):

    if query is None or "Error" in query:
        return "No valid SQL generated. Check API quota."

    conn = get_connection()

    if conn is None:
        return "Database not connected."

    cursor = conn.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except Exception as e:
        return str(e)

    finally:
        conn.close()
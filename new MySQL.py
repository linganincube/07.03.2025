import mysql.connector

# Database configuration
config = {
    'user': 'root',
    'password': 'Ntando123@',
    'host': 'localhost',
    'database': 'mysql',
    'raise_on_warnings': True
}

QUERY_SELECT_ALL = "SELECT * FROM "  # Introduce constant for query


def fetch_all_rows(query, connection):
    """Fetch all rows for a given SQL query."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()


try:
    # Establish a connection to the database
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Connected to MySQL database")

        # Fetch and print rows using the extracted function
        rows = fetch_all_rows(QUERY_SELECT_ALL, connection)
        for row in rows:
            print(row)
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Ensure the connection is closed properly
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
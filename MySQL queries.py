import mysql.connector
import datetime

def get_current_date_from_mysql(host="127.0.0.1", port=3306, user="root", password="Ntando123@"):
    """
    Connects to a MySQL server, retrieves the current date, and prints it.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        port (int): The port number of the MySQL server.
        user (str): The username for connecting to the MySQL server.
        password (str): The password for connecting to the MySQL server.

    Returns:
        None. Prints the current date to the console.
    """
    try:
        # Connect to server
        cnx = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )

        # Get a cursor
        cur = cnx.cursor()

        # Execute a query
        cur.execute("SELECT CURDATE()")

        # Fetch one result
        row = cur.fetchone()

        if row:
            print("Current date from MySQL: {0}".format(row[0]))
        else:
            print("No date returned from MySQL.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close connection
        if 'cnx' in locals() and cnx.is_connected():
            cur.close()
            cnx.close()
            print("MySQL connection closed.")

def get_current_date_python():
    """
    Gets the current date using Python's datetime module and prints it.
    """
    today = datetime.date.today()
    print(f"Current date from Python: {today}")

def get_mysql_server_version(host="127.0.0.1", port=3306, user="root", password="Ntando123@"):
    """
    Connects to a MySQL server and retrieves the server version.
    Args:
        host (str): The hostname or IP address of the MySQL server.
        port (int): The port number of the MySQL server.
        user (str): The username for connecting to the MySQL server.
        password (str): The password for connecting to the MySQL server.
    Returns:
        None. Prints the server version to the console.
    """
    try:
        cnx = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )
        cur = cnx.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()[0]
        print(f"MySQL Server version: {version}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cur.close()
            cnx.close()
            print("MySQL connection closed.")

def get_databases(host="127.0.0.1", port=3306, user="root", password="Ntando123@"):
    """
    Connects to a MySQL server and retrieves a list of databases.
    Args:
        host (str): The hostname or IP address of the MySQL server.
        port (int): The port number of the MySQL server.
        user (str): The username for connecting to the MySQL server.
        password (str): The password for connecting to the MySQL server.
    Returns:
        None. Prints the list of databases to the console.
    """
    try:
        cnx = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )
        cur = cnx.cursor()
        cur.execute("SHOW DATABASES")
        databases = [db[0] for db in cur.fetchall()]
        print("Databases:")
        for db in databases:
            print(f"- {db}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cur.close()
            cnx.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    get_current_date_from_mysql()
    get_current_date_python()
    get_mysql_server_version()
    get_databases()
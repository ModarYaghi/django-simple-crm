"""
A Python module to create the database.
This module will be use one time.
"""

import MySQLdb


def create_database(db_name, host, user, password):
    """Create the database using the 'mysqlclient' method"""

    # Initialize 'conn' and 'cursor' to None so that they are always defined.
    # This prevent an "unbound variable" error in the finally block if an exception
    # occurs before they are assigned a valid connection or cursor object.
    conn = None
    cursor = None

    try:
        conn = MySQLdb.connect(host=host, user=user, passwd=password)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4")

        conn.commit()
        print(f"Database '{db_name}' is created or already exists.")

    except MySQLdb.OperationalError as e:
        print(f"Operational error: {e}")

    except MySQLdb.IntegrityError as e:
        print(f"Integrity error: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    DB_NAME = "elderco"
    HOST = "localhost"
    USER = "fmnDj"
    PASSWD = "Fmn44.65!"

    create_database(db_name=DB_NAME, host=HOST, user=USER, password=PASSWD)

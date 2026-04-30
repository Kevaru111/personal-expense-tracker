import sqlite3

DATABASE_NAME = "expense_tracker.db"

def connect_db():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection

def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    with open("schema.sql", "r") as file:
        sql_script = file.read()
        cursor.executescript(sql_script)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created succesfully.")
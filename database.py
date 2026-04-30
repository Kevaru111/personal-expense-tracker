import sqlite3
from models import Transaction, User, Category, PaymentMethod

DATABASE_NAME = "expense_tracker.db"

def connect_db():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    with open("schema.sql", "r") as file:
        sql_script = file.read()
        cursor.executescript(sql_script)

    connection.commit()
    connection.close()

# INSERTS IN DATABASE

def insert_transaction(transaction: Transaction):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
            INSERT INTO transactions(
            user_id,
            category_id,
            payment_method_id,
            amount,
            transaction_type,
            description,
            transaction_date
            ) 
            VALUES(?, ?, ?, ?, ?, ?, ?)
        """,
        (
            transaction.user_id,
            transaction.category_id,
            transaction.payment_method_id,
            transaction.amount,
            transaction.transaction_type,
            transaction.description,
            transaction.transaction_date
        )
    )

    connection.commit()
    connection.close()

def insert_user(user: User):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
            INSERT INTO users (username, email)
            VALUES (?, ?)
        """,
        (
            user.username,
            user.email
        )
    )

    connection.commit()
    connection.close()

def insert_category(category: Category):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
            INSERT INTO categories (name, category_type)
            VALUES (?, ?)
        """,
        (
            category.name,
            category.category_type
        )
    )

    connection.commit()
    connection.close()

def insert_payment_method(payment_method: PaymentMethod):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO payment_methods (name)
        VALUES (?)
        """,
        (
            payment_method.name,
        )
    )

    connection.commit()
    connection.close()

def get_all_users():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """ 
            SELECT id, username, email FROM users
        """
    )
    
    users = cursor.fetchall()

    connection.close()
    return users

def view_all_transactions():
    print("View all transactions selected.")

def view_transactions_by_category():
    print("View transactions by category selected.")

def view_monthly_summary():
    print("View monthly summary selected.")


if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully.")
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

def get_categories_by_type(category_type):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """ 
            SELECT id, name, category_type 
            FROM categories
            WHERE category_type = ?
            ORDER BY id
        """,
        (category_type,)
    )

    categories = cursor.fetchall()

    connection.close()
    return categories

def get_all_payment_methods():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name
        FROM payment_methods
        ORDER BY id
        """
    )

    payment_methods = cursor.fetchall()

    connection.close()
    return payment_methods

def get_transactions_by_user(user_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """ 
            SELECT 
            transactions.id,
            transactions.transaction_date,
            transactions.transaction_type,
            categories.name,
            payment_methods.name,
            transactions.amount,
            transactions.description
            FROM transactions
            JOIN categories ON transactions.category_id = categories.id
            LEFT JOIN payment_methods ON transactions.payment_method_id = payment_methods.id
            WHERE transactions.user_id = ?
            ORDER BY transactions.transaction_date DESC, transactions.id DESC
        """,
        (user_id,)
    )

    transactions = cursor.fetchall()
    connection.close()

    return transactions

def get_all_categories():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(

        """
            SELECT id, name, category_type FROM categories
            ORDER BY category_type, name
        """
        
    )

    categories = cursor.fetchall()
    connection.close()

    return categories



def get_transactions_by_user_and_category(user_id, category_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            t.id,
            t.transaction_date,
            t.transaction_type,
            categories.name,
            payment_methods.name,
            t.amount,
            t.description
        FROM transactions as t
        JOIN categories ON t.category_id = categories.id
        LEFT JOIN payment_methods ON t.payment_method_id = payment_methods.id
        WHERE t.user_id = ?
        AND t.category_id = ?
        ORDER BY t.transaction_date DESC, t.id DESC
        """,
        (user_id, category_id)
    )

    transactions = cursor.fetchall()

    connection.close()

    return transactions


# def view_monthly_summary():
    # print("View monthly summary selected.")


if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully.")
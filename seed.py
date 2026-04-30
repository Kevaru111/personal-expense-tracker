from database import connect_db

def seed_data():
    connection = connect_db()
    cursor = connection.cursor()
    #  Users insert data
    cursor.execute(
        "INSERT INTO users(username, email) VALUES(?, ?)",
        ("Tom", "tom@gmail.com")
    )

    # Categories insert data
    cursor.execute(
        "INSERT INTO categories (name, category_type) VALUES(?, ?)",
        ("Food", "expense")
    )

    cursor.execute(
        "INSERT INTO categories (name, category_type) VALUES(?, ?)",
        ("Transport", "expense")
    )

    cursor.execute(
        "INSERT INTO categories (name, category_type) VALUES(?, ?)",
        ("Rent", "expense")
    )

    cursor.execute(
        "INSERT INTO categories (name, category_type) VALUES(?, ?)",
        ("Salary", "income")
    )

    # Payment methods: insert data

    cursor.execute(
        "INSERT INTO payment_methods (name) VALUES(?)",
        ("Cash",)
    )

    cursor.execute(
        "INSERT INTO payment_methods (name) VALUES(?)",
        ("Card",)
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    seed_data()
    print("Default data inserted successfully")
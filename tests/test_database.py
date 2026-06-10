import database
from models import User, Category, PaymentMethod, Transaction

def test_insert_user(tmp_path, monkeypatch):
    
    test_db = tmp_path / "test_expense_tracker.db"
    monkeypatch.setattr(database, "DATABASE_NAME", str(test_db))

    database.create_tables()

    user = User(username = "test_user", email = "test@example.com")

    database.insert_user(user)
    users = database.get_all_users()

    assert len(users) == 1
    assert users[0][1] == "test_user"
    assert users[0][2] == "test@example.com"

def test_get_categories_by_type(tmp_path, monkeypatch):
    test_db = tmp_path / "test_expense_tracker.db"
    monkeypatch.setattr(database, "DATABASE_NAME", str(test_db))

    database.create_tables()

    database.insert_category(Category(name="Salary", category_type="income"))
    database.insert_category(Category(name="Food", category_type="expense"))

    income_categories = database.get_categories_by_type("income")

    assert len(income_categories) == 1
    assert income_categories[0][1] == "Salary"
    assert income_categories[0][2] == "income" 

from models import Transaction, User, Category, PaymentMethod
from database import (insert_transaction, insert_user, insert_category, insert_payment_method,
                      get_all_users, get_categories_by_type, get_all_payment_methods, get_transaction_by_user) 


def show_menu():
    print("\n Personal Expense Tracker")
    print("1. Add transaction")
    print("2. View all transactions")
    print("3. View transactions by category")
    print("4. View monthly summary")
    print("5. Exit")

def select_user():
    users = get_all_users()

    if not users:
        print("No users found. Please add a user first.")
        return None
    
    print("\n Select user: ")

    for user in users:
        print(f"{user[0]}. {user[1]} - {user[2]}")

    user_id = int(input("Enter user ID: "))
    return user_id

def add_transaction(user_id):
    print("\n Add new transaction")

    transaction_type = input("Enter transaction type (income/expense): ").lower()
    if transaction_type not in ["income", "expense"]:
        print("Invalid transaction type.")
        return

    category_id = choose_category(transaction_type)
    if category_id is None:
        return

    payment_method_id = choose_payment_method()
    if payment_method_id is None:
        return

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return
    
    description = input("Enter description: ")
    transaction_date = input("Enter date (YYYY-MM-DD): ")

    transaction = Transaction(
        user_id=user_id,
        category_id=category_id,
        payment_method_id=payment_method_id,
        amount=amount,
        transaction_type=transaction_type,
        description=description,
        transaction_date=transaction_date
    )

    insert_transaction(transaction)
    print("Transaction added successfully.")

def choose_category(transaction_type):
    categories = get_categories_by_type(transaction_type)

    if not categories:
        print("No categories found.")
        return None
    
    print("\n Choose category: ")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    choice = int(input("Enter category number: "))

    if choice < 1 or choice > len(categories):
        print("Invalid category choice.")
        return None
    
    selected_category = categories[choice - 1]
    category_id = selected_category[0]

    return category_id

def choose_payment_method():
    payment_methods = get_all_payment_methods()

    if not payment_methods:
        print("No payment methods found.")
        return None
    
    print("\n Choose payment method: ")

    for index, method in enumerate(payment_methods, start=1):
        print(f"{index}. {method[1]}")

    choice = int(input("Enter payment method number: "))

    if choice < 1 or choice > len(payment_methods):
        print("Invalid payment method choice.")
        return None
    
    selected_method = payment_methods[choice - 1]
    payment_method_id = selected_method[0]

    return payment_method_id

def view_all_transactions(user_id):
    transactions = get_transaction_by_user(user_id)

    if not transactions:
        print("\nNo transactons found.")
        return
    
    for transaction in transactions:
        transaction_id = transaction[0]
        transaction_date = transaction[1]
        transaction_type = transaction[2],
        category_name = transaction[3],
        payment_methods_name = transaction[4],
        amount = transaction[5]
        description = transaction[6]

        print(
            f"{transaction_id}. {transaction_date} | "
            f"{transaction_type} | "
            f"{category_name} | "
            f"{payment_methods_name} | "
            f"{amount:.2f} | "
            f"{description}"
        )




def view_transactions_by_category():
    print("View transactions by category selected.")

def view_monthly_summary():
    print("View monthly summary selected.")

def main():
    current_user_id = select_user()

    if current_user_id is None:
        return

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction(current_user_id)
        elif choice == "2":
            view_all_transactions(current_user_id)
        elif choice == "3":
            view_transactions_by_category()
        elif choice == "4":
            view_monthly_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
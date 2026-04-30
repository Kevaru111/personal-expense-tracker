def show_menu():
    print("\n Personal Expense Tracker")
    print("1. Add transaction")
    print("2. View all transactions")
    print("3. View transactions by category")
    print("4. View monthly summary")
    print("5. Exit")

def add_transaction():
    print("Add transaction selected.")

def view_all_transactions():
    print("View all transactions selected.")

def view_transactions_by_category():
    print("View transactions by category selected.")

def view_monthly_summary():
    print("View monthly summary selected.")

def main():
    
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_all_transactions()
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
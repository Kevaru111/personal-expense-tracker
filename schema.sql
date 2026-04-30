CREATE TABLE users(
     id integer PRIMARY KEY AUTOINCREMENT,
     username TEXT NOT NULL UNIQUE,
     email TEXT UNIQUE,
     created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
    

CREATE TABLE categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(50) NOT NULL UNIQUE,
    category_type TEXT NOT NULL CHECK(category_type IN ('income', 'expense'))
);

CREATE TABLE payment_methods(
    id integer PRIMARY KEY AUTOINCREMENT,
    name TEXT(50) NOT NULL UNIQUE
);

CREATE TABLE transactions(
    id integer PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    payment_method_id INTEGER,
    amount REAL NOT NULL CHECK(amount > 0),
    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('income', 'expense')),
    description TEXT,
    transaction_date TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(category_id) REFERENCES categories(id),
    FOREIGN KEY(payment_method_id) REFERENCES payment_methods(id)
);
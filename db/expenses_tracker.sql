PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS payees;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS users;

CREATE TABLE payees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR,
    amount INT,
    date VARCHAR,
    submitted BOOLEAN,
    payee_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
        FOREIGN KEY (payee_id)
            REFERENCES payees (id),
        FOREIGN KEY (category_id)
            REFERENCES categories (id)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    expenses_limit INT
);
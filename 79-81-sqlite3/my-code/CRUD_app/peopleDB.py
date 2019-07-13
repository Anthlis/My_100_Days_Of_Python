import sqlite3

con = sqlite3.connect("peopleDB.db")
print("Database opened successfully")

con.execute(
    "create table People (id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "name TEXT NOT NULL, address TEXT NOT NULL, email TEXT UNIQUE NOT NULL, phone TEXT NOT NULL)")

print("Table created successfully")

con.close()
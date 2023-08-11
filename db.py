import sqlite3

conn = sqlite3.connect("database.db")

print("opened database successfully")

conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER, gender TEXT, email TEXT, phone INTEGER, Birth_date TEXT)")

print("table created successfully")

conn.close()
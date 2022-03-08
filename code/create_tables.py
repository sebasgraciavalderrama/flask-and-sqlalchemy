# We call this script to create tables.
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

delete_query = "DROP TABLE IF EXISTS users"
cursor.execute(delete_query)

delete_query = "DROP TABLE IF EXISTS items"
cursor.execute(delete_query)

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price REAL)"
cursor.execute(create_table)

connection.commit()
connection.close()
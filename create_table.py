import sqlite3

connection = sqlite3.connect('data.db')
cursor= connection.cursor()
create_table="Create Table if not exists users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
#in sqlite3 'INTEGER' is the same as 'int' except 'INTEGER' can autoincrement
create_table="Create Table if not exists items(id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)
connection.commit()
connection.close()

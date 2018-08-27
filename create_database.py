import sqlite3

db = sqlite3.connect('guestbook.db')
db.execute('create table users (id INTEGER PRIMARY KEY autoincrement, username text, password text, date_joined int)')
db.execute('create table posts (id INTEGER PRIMARY KEY autoincrement, poster_id int, title text, body text, time_posted int)')
db.commit()
db.close()
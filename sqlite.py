import sqlite3

db = sqlite3.connect('database.db')
#db.row_factory = sqlite3.Row
#db.execute('create table person(firstname text, lastname text, age int)')
#db.execute('insert into person (firstname,lastname,age)values("Dan","Finn",36)')
#db.execute('update person set firstname = "Daniel" where lastname = "Finn"')
#contents = db.execute('select * from person')
removal = db.execute('delete from person where lastname = "Finn"')
db.commit()

#for each in contents:
#  print (each['firstname'])

#db.commit()

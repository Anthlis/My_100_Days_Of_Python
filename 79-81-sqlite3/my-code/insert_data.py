import sqlite3


connection = sqlite3.connect('addressbook.db')

c = connection.cursor()

c.execute("INSERT INTO Details VALUES('Anthlis', '123 A Street Name, Timbuktoo', '01234567890')")

connection.commit()

connection.close()
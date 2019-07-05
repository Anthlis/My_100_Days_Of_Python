import sqlite3

conn = sqlite3.connect('addressbook.db')

c = conn.cursor()

for row in c.execute("SELECT * from Details"):
    # print(row)
    print(row[0])

for row in c.execute("SELECT * from Details"):
    print(row[0] + " lives at " + row[1] + "and has phone number " + str(row[2]))



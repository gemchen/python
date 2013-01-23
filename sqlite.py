import sqlite3

con = sqlite3.connect('./mm.db3')
cur = con.cursor()
# cur.execute('CREATE TABLE movies (o_id INTEGER PRIMARY KEY, name VARCHAR(20), location VARCHAR(512))')
# con.commit()
# cur.execute('INSERT INTO movies (o_id, name, location) VALUES(NULL, "apple", "broccoli")')
# con.commit()
# print cur.lastrowid

cur.execute('SELECT * FROM movies')
print cur.fetchall()
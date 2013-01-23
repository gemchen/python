# -*-coding: utf-8 -*- 
import os,sqlite3

con = sqlite3.connect('./mm.db3')
cur = con.cursor()
# cur.execute('CREATE TABLE movies (o_id INTEGER PRIMARY KEY, name VARCHAR(100), location VARCHAR(512))')
# con.commit()


def insert(_name, _location):
	cur.execute('INSERT INTO movies (o_id, name, location) VALUES(NULL, \"'+_name+'\", \"'+_location+'\")')
	con.commit()

rootDir = "/Users/gemchen/Movies"
print("your root dir is:"+rootDir)
for root,dirs,files in os.walk(rootDir):
	for f in files:
		path = os.path.join(root,f)
		insert(f,path)

print cur.lastrowid
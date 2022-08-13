import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('When I was born...', 'I was a baby')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('How long I was a child', 'I was a child until I became a man')
            )

connection.commit()
connection.close()
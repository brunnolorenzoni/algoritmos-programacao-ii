from Database import Database

db = Database()

conn = db.connect()

# create a cursor
cur = conn.cursor()

# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')

 # display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)

# close the communication with the PostgreSQL
cur.close()
db.disconnect()
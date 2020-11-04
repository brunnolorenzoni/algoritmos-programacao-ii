import psycopg2
from config import config

class Database():
    
  conn = None

  def connect(self):
    try:
      # read connection parameters
      params = config()

      # connect to the PostgreSQL server
      print('Connecting to the PostgreSQL database...')
      self.conn = psycopg2.connect(**params)
      
      return self.conn
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
      
  def disconnect(self):
    self.conn.close()
    print('Database connection closed.')
    return self.conn
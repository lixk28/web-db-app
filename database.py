import os
import sqlite3

INSERT  = 1
DELETE  = 2
QUERY   = 3
UPDATE  = 4

db_path = './db/book.db'
sql_path = './sql/schema.sql'

def init_db():
  if os.path.exists(db_path):
    os.remove(db_path)
  with open(sql_path, 'r') as sql_file:
    sql_script = sql_file.read()
  conn = sqlite3.connect(database=db_path)
  cursor = conn.cursor()
  cursor.executescript(sql_script)
  cursor.close()
  conn.commit()
  conn.close()

if __name__ == "__main__":
  init_db()
  pass
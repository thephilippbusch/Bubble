from sqlalchemy import create_engine
from decouple import config

SERVER_ENV = config("SERVER_ENV")
SERVER_ADMIN_UID = config("SERVER_ADMIN_PASSWORD")
SERVER_ADMIN_PASSWORD = config("SERVER_ADMIN_PASSWORD")

engine = create_engine(config("DATABASE_URL"))

conn = engine.connect()

def init_db():
  init_commands = (
    """
      CREATE TABLE IF NOT EXISTS users (
        uid VARCHAR(255) NOT NULL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255),
        password VARCHAR(255)
      )
    """,
    f"""
      INSERT INTO users (uid, name, surname, password)
      VALUES ('{SERVER_ADMIN_UID}', 'administrator', 'admin', '{SERVER_ADMIN_PASSWORD}')
    """
  )

  for command in init_commands:
    conn.execute(command)

class Database:
  def connection():
    return conn
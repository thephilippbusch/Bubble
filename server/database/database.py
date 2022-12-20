from sqlalchemy import create_engine
from decouple import config
import bcrypt

SERVER_ENV = config("SERVER_ENV")
SERVER_ADMIN_UID = config("SERVER_ADMIN_UID")
SERVER_ADMIN_PASSWORD = config("SERVER_ADMIN_PASSWORD")

engine = create_engine(config("DATABASE_URL"))

conn = engine.connect()

hashed_admin_pw = bcrypt.hashpw(str.encode(SERVER_ADMIN_PASSWORD), bcrypt.gensalt(12))

def init_db():
  init_commands = (
    """
      CREATE TABLE IF NOT EXISTS users (
        uid VARCHAR(255) NOT NULL PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255),
        password VARCHAR(255)
      )
    """,
    """
      CREATE TABLE IF NOT EXISTS list (
        lid VARCHAR(255) NOT NULL PRIMARY KEY,
        uid VARCHAR(255),
        title VARCHAR(255) NOT NULL,
        CONSTRAINT fk_user
          FOREIGN KEY(uid)
            REFERENCES users(uid)
      )
    """,
    """
      CREATE TABLE IF NOT EXISTS entries (
        eid VARCHAR(255) NOT NULL PRIMARY KEY,
        lid VARCHAR(255),
        name VARCHAR(255) NOT NULL,
        description VARCHAR(255) NOT NULL,
        CONSTRAINT fk_list
          FOREIGN KEY(lid) 
            REFERENCES list(lid)
      )
    """,
    f"""
      INSERT INTO users (uid, username, name, surname, password)
      SELECT '{SERVER_ADMIN_UID}', 'admin', 'administrator', 'admin', '{hashed_admin_pw.decode()}'
      WHERE NOT EXISTS (SELECT uid FROM users WHERE uid = '{SERVER_ADMIN_UID}');
    """
  )

  for command in init_commands:
    conn.execute(command)

class Database:
  def connection():
    return conn
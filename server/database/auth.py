import bcrypt
from uuid import uuid4

from server.database.database import Database
from server.auth.auth_handler import signJWT

conn = Database.connection()

class Auth:
  def sign_in(username: str, password: str):
    try:
      query = f"""
        SELECT uid, password
        FROM users WHERE username = '{username}';
      """

      res = conn.execute(query).first()

      if res is not None:
        db_password = res["password"]

        if bcrypt.checkpw(str.encode(password), str.encode(db_password)):
          token = signJWT(res["uid"], expires_in=None)
          return {
            "successful": True,
            "data": {
              "token": token,
              "uid": res["uid"]
            }
          }
        return {
          "successful": False,
          "error": "Wrong password!"
        }
      return {
        "successful": False,
        "error": str(e)
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def sign_up(username: str, name: str, surname: str, password: str):
    try:
      hashed_pw = bcrypt.hashpw(str.encode(password), bcrypt.gensalt(12))

      query = f"""
        INSERT INTO users (uid, username, name, surname, password)
        VALUES ({uuid4()}, {username}, {name}, {surname}, {hashed_pw.decode()})
        RETURNING *;
      """

      res = conn.execute(query).first()

      if res is not None:
        token = signJWT(res["uid"], expires_in=None)
        return {
          "successful": True,
          "data": {
            "token": token,
            "user": dict(res)
          }
        }
      return {
        "successful": False,
        "error": str(e)
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }
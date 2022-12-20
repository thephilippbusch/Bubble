from server.database.database import Database
from uuid import uuid4
from sqlalchemy import text

conn = Database.connection()

class List:
  def get_list_by_id(lid: str):
    try:
      query = (f"""
        SELECT * FROM list
        WHERE lid = '{lid}';
      """)

      res = conn.execute(query).first()

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": f"No list exists with the ID {lid}!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def search_list(query_string: str):
    try:
      query = (f"""
        SELECT * FROM list
        WHERE title LIKE '%{query_string}%';
      """)

      res = conn.execute(text(query)).fetchall()

      if res:
        return {
          "successful": True,
          "data": res
        }
      return {
        "successful": False,
        "error": f"No lists were found with the search query {query_string}!"
      }
    except Exception as e:
      print("Error at search_list: " + str(e))
      return {
        "successful": False,
        "error": str(e)
      }

  def create_list(uid: str, title: str):
    try:
      query = (f"""
        INSERT INTO list (lid, title, uid)
        VALUES ('{uuid4()}', '{title}', '{uid}')
        RETURNING *;
      """)

      res = conn.execute(query).first()

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": f"List could not be created"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def update_list(lid: str, title: str):
    try:
      query = (f"""
        UPDATE list
        SET title = '{title}'
        WHERE lid = '{lid}'
        RETURNING *;
      """)

      res = conn.execute(query).first()

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": f"List could not be updated!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def remove_list(lid: str):
    try:
      query = (f"""
        DELETE FROM list
        WHERE lid = '{lid}';
      """)

      res = conn.execute(query)

      if res:
        data = dict(res)
        return { "successful": True }
      return {
        "successful": False,
        "error": f"List could not be removed!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def get_user_lists(uid: str):
    try:
      query = (f"""
        SELECT l.* FROM users u
        JOIN list l ON l.uid = u.uid
        WHERE u.uid = '{uid}';
      """)

      res = conn.execute(query).first()

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": f"No Lists were found for User {uid}!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

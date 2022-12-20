from server.database.database import Database
from uuid import uuid4
from sqlalchemy import text

conn = Database.connection()

class Entries:
  def get_entry_by_id(eid: str):
    try:
      query = (f"""
        SELECT * FROM entries
        WHERE eid = '{eid}';
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
        "error": f"No entry exists with the ID {eid}!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def search_entries(query_string: str):
    try:
      query = (f"""
        SELECT * FROM entries
        WHERE name LIKE '%{query_string}%';
      """)

      res = conn.execute(text(query)).fetchall()

      if res:
        return {
          "successful": True,
          "data": res
        }
      return {
        "successful": False,
        "error": f"No entries were found with the search query {query_string}!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def get_list_entries(lid: str):
    try:
      query = (f"""
        SELECT e.* FROM list l
        JOIN entries e ON e.lid = l.lid
        WHERE l.lid = '{lid}';
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
        "error": f"No Entries were found for List {lid}!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def create_entry(lid: str, name: str):
    try:
      query = (f"""
        INSERT INTO entries (eid, name, lid)
        VALUES ('{uuid4()}', '{name}', '{lid}')
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
        "error": f"Entry could not be created"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def update_entry(eid: str, name: str):
    try:
      query = (f"""
        UPDATE list
        SET name = '{name}'
        WHERE lid = '{eid}'
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

  def remove_entry(eid: str):
    try:
      query = (f"""
        DELETE FROM entries
        WHERE eid = '{eid}';
      """)

      res = conn.execute(query)

      if res:
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

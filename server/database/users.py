from server.database.database import Database

conn = Database.connection()

class Users:
  def get_user_by_id(uid: str):
    try:
      query = (f"""
        SELECT * FROM users
        WHERE uid = '{uid}';
      """)

      res = conn.execute(query)

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": "No user was found!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }
  
  def get_user_by_query(query: str):
    try:
      query = (f"""
        SELECT * FROM users
        WHERE name LIKE '%{query}%' OR surname LIKE '%{query}%';
      """)

      res = conn.execute(query)

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": "No users were found!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def get_users(uid: str):
    try:
      query = (f"""
        SELECT * FROM users
        WHERE uid = '{uid}';
      """)

      res = conn.execute(query)

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": "No user was found!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def create_user(uid: str):
    try:
      query = (f"""
        SELECT * FROM users
        WHERE uid = '{uid}';
      """)

      res = conn.execute(query)

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": "No user was found!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def update_user(uid: str):
    try:
      query = (f"""
        SELECT * FROM users
        WHERE uid = '{uid}';
      """)

      res = conn.execute(query)

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": "No user was found!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }

  def remove_user(uid: str):
    try:
      query = (f"""
        SELECT * FROM users
        WHERE uid = '{uid}';
      """)

      res = conn.execute(query)

      if res:
        data = dict(res)
        return {
          "successful": True,
          "data": data
        }
      return {
        "successful": False,
        "error": "No user was found!"
      }
    except Exception as e:
      print(e)
      return {
        "successful": False,
        "error": str(e)
      }
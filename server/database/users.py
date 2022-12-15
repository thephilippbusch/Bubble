from server.database.database import Database

conn = Database.connection()

class Users:
  def get_user(uid: str):
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

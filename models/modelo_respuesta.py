from util.conexion      import connect_to_db

class respuesta():
 @classmethod
 def insert(self, mecanico, peticion, info):
    try:
      con = connect_to_db()
      cursor = con.cursor()
      sql = f'INSERT INTO respuesta (mecanico, peticion, info) VALUES("{mecanico}","{peticion}","{info}");'
      print(sql)
      cursor.execute(sql)
      result = cursor.rowcount 
      cursor.execute("commit")
      con.close()
      return result
    except Exception as error: print(error)
from util.conexion      import connect_to_db

class respuesta():
  @classmethod
  def select_all(self):
    conexion = connect_to_db()
    cursor = conexion.cursor()
    sql = f'''
      SELECT respuesta.id, usuario.nombres, usuario.apellido, peticion.info, respuesta.info 
      FROM respuesta 
      INNER JOIN usuario ON usuario.id = respuesta.mecanico
      INNER JOIN peticion ON peticion.id = respuesta.peticion
      ORDER BY peticion.id;
    '''
    cursor.execute(sql)
    info = cursor.fetchall()
    cursor.close()
    return info
  
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

  
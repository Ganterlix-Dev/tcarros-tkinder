from util.conexion import connect_to_db

class peticion():
  @classmethod
  def select_all(self):
    conexion = connect_to_db()
    cursor = conexion.cursor()
    sql = f'''
      SELECT peticion.id, usuario.nombres, usuario.apellido, vehiculo.marca, peticion.info 
      FROM peticion 
      INNER JOIN usuario ON usuario.id = peticion.usuario
      INNER JOIN vehiculo ON vehiculo.id = peticion.vehiculo
      ORDER BY peticion.id;
    '''
    cursor.execute(sql)
    info = cursor.fetchall()
    cursor.close()
    return info
  
  @classmethod
  def select_one(self, id):
    conexion = connect_to_db()
    cursor = conexion.cursor()
    sql = f'''
      SELECT peticion.id, usuario.nombres, usuario.apellido, vehiculo.marca, peticion.info 
      FROM peticion 
      INNER JOIN usuario ON usuario.id = peticion.usuario
      INNER JOIN vehiculo ON vehiculo.id = peticion.vehiculo
      WHERE peticion.id={id}
      ORDER BY peticion.id;
    '''
    cursor.execute(sql)
    info = cursor.fetchall()
    cursor.close()
    return info
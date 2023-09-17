from util.conexion    import connect_to_db
from bcrypt           import checkpw

class admin():
  @classmethod
  def login(self, email, clave: str):
    con = connect_to_db()
    cursor = con.cursor()
    sql = f'SELECT * FROM usuario WHERE email="{email}"'
    cursor.execute(sql)
    user = cursor.fetchone()
    if not user:
      return 'el usuario no existe o el correo es incorrecto'
    
    clave_hasheada = user[5]
    
    clave_correcta = checkpw(clave.encode("UTF-8"), clave_hasheada.encode("UTF-8"))
    print(clave_correcta)

    if not clave_correcta:
      return 'la clave es incorrecta'
    
    tipo_usuario = user[6]
    
    if tipo_usuario == "cliente":
      return 'solo el administrador y el mecanico tienen permiso a la aplicacion'
    
    if tipo_usuario == "administrador":
      return 'Admin'
    
    if tipo_usuario == "mecanico":
      return 'Mecanico'
    
  @classmethod
  def select_all(self):
    con = connect_to_db()
    cursor = con.cursor()
    sql = f"SELECT id, nombres, apellido, numero, email, tipo_usuario FROM usuario"
    cursor.execute(sql)
    info = cursor.fetchall()
    cursor.close()
    return info
  
  @classmethod
  def select_one(self, id):
    con = connect_to_db()
    cursor = con.cursor()
    sql = f"SELECT * FROM usuario WHERE id = {id};"
    cursor.execute(sql)
    info = cursor.fetchone()
    cursor.close()
    return info
  
  @classmethod
  def select_by_email(self, email):
    con = connect_to_db()
    cursor = con.cursor()
    sql = f"SELECT * FROM usuario WHERE email = '{email}';"
    cursor.execute(sql)
    info = cursor.fetchone()
    cursor.close()
    return info

  @classmethod
  def insert(self, nombres, apellido, numero, email, clave, tipo_usuarios):
    try:
      con = connect_to_db()
      cursor = con.cursor()
      sql = f'INSERT INTO usuario (nombres, apellido, numero, email, clave, tipo_usuario) VALUES("{nombres}","{apellido}","{numero}","{email}","{clave}","{tipo_usuarios}");'
      print(sql)
      cursor.execute(sql)
      result = cursor.rowcount 
      cursor.execute("commit")
      con.close()
      return None, False
    except Exception as error: 
      print(error)
      return error, True

  @classmethod
  def update(self, id, nombres, apellido, numero, email, tipo_usuarios):
    try:
      con = connect_to_db()
      cursor = con.cursor()
      sql = f"UPDATE usuario SET nombres = '{nombres}', apellido = '{apellido}', numero = '{numero}', email = '{email}', tipo_usuario = '{tipo_usuarios}' WHERE id = {id};"
      cursor.execute(sql)
      result = cursor.rowcount 
      cursor.execute("commit")
      con.close()
      return result
    except Exception as error: print(error)
          

  @classmethod
  def delete(self, id):
    try:
      con = connect_to_db()
      cursor = con.cursor()
      sql = f"DELETE FROM usuario WHERE id = {id};"
      cursor.execute(sql)
      result = cursor.rowcount 
      cursor.execute("commit")
      con.close()
      return result
    except Exception as error: print(error)
from util.conexion      import connect_to_db

class mecanic():
  @classmethod
  def select_all(self):
    con = connect_to_db()
    cursor = con.cursor()
    sql = f"SELECT * FROM vehiculos"
    cursor.execute(sql)
    info = cursor.fetchall()
    cursor.close()
    return info
  
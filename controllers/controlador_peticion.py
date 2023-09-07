from models.modelo_peticiones import peticion

class mostrar():
  @classmethod
  def select_all(self):
    peti = peticion.select_all()
    return {"error": False, "msg": peti}
from models.modelo_respuesta import respuesta as resp

class controlador_resp:
  @classmethod
  def select_all(self):
    result = resp.select_all()
    return {"error": False, "msg": result}
    
    
    
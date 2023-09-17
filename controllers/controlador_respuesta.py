from models.modelo_respuesta import respuesta as resp

class controlador_resp:
  @classmethod
  def insert(id_mecanico, id_peticion, respuesta):
   result = resp.insert(id_mecanico, id_peticion, respuesta)
   if not id_mecanico or not id_peticion or not respuesta: 
    return {"error": True, "msg": result}
    
    
    
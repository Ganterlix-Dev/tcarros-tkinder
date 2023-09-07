from models.modelo_user import admin
import bcrypt
import re

class controlador_user:
  @classmethod
  def validar_datos(self, email,clave):
    if not email and not clave:
      return "faltan campos por llenar"
    
    correo_valido = r"^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$"

    if not re.match(correo_valido, email):
      return "el correo electronico no es valido"
    
    respuesta_modelo = admin.login(email, clave)

    return respuesta_modelo
  
  @classmethod
  def insert(self, nombres, apellido, numero, email, clave, tipo):
    if not nombres or not apellido or not numero or not email or not clave or not tipo:
      return {"error": True, "msg": "Faltan campos por llenar."}

    try: 
      numero = int(numero)
    except ValueError:
      return {"error": True, "msg": "El numero de telefono es incorrecto"}

    if numero < 1000000000 or numero > 100000000000:    
      return {"error": True, "msg": "El numero telefonico tiene que estar en el rango de 11 digitos."}

    validar_correo = r"^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$"

    if not re.match(validar_correo, email):
      return {"error": True, "msg": "El correo electronico no es valido, intentelo nuevamente."}
    
    if tipo != "cliente" and tipo != "administrador" and tipo != "mecanico":
      return {"error": True, "msg": "El tipo de usuario debe ser: cliente, administrador o mecanico"}
    
    clave_hash = bcrypt.hashpw(clave.encode("UTF-8"), bcrypt.gensalt(10))

    result = admin.insert(nombres, apellido, numero, email, clave_hash, tipo)
    return {"error": False, "msg": result}

  @classmethod
  def select_all(self):
    user = admin.select_all()
    return {"error": False, "msg": user}
  
  @classmethod
  def select_one(self, id):
    user = admin.select_one(id)
    return {"error": False, "msg": user}
  
  @classmethod
  def select_by_email(self, email):
    user = admin.select_by_email(email)
    return {"error": False, "msg": user}
        
  @classmethod
  def update(self, id, nombres, apellido, numero, email, tipo):
    if not id and not nombres or not apellido or not numero or not email:
      return {"error": True, "msg": "Faltan campos por llenar."}

    try: 
      numero = int(numero)
    except ValueError:
      return {"error": True, "msg": "El numero de telefono es incorrecto"}

    if numero < 1000000000 or numero > 100000000000:    
      return {"error": True, "msg": "'El numero telefonico tiene que estar en el rango de 11 digitos.'"}

    validar_correo = r"^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$"

    if not re.match(validar_correo, email):
      return {"error": True, "msg": "'El correo electronico no es valido, intentelo nuevamente.'"}
    
    if tipo != "cliente" and tipo != "administrador" and tipo != "mecanico":
      return {"error": True, "msg": "El tipo de usuario debe ser: cliente, administrador o mecanico"}

    result = admin.update(id, nombres, apellido, numero, email, tipo)
    return {"error": False, "msg": result}

  @classmethod
  def delete(self, id):
    try:
      print(id)
      result = admin.delete(int(id))
      return {"error": False, "msg": result}
    except ValueError:
      return {"error": True, "msg": "ID incorrecto"}
    
    
    
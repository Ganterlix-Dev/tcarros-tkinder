from tkinter.messagebox                import *
from jinja2                            import Environment,FileSystemLoader
from controllers.controlador_user      import controlador_user
from controllers.controlador_vehiculo  import meca as mecanico
from controllers.controlador_peticion  import mostrar as peticion 
from controllers.controlador_respuesta import controlador_resp as respuesta
import pdfkit

def generar_pdf_usuario():    
  path_wkhtmltopdf = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
  config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

  env = Environment(loader=FileSystemLoader("template"))
  usuario_template = env.get_template("reporte.html")

  usuario = {
    "from": "Usuarios",
    "cols": ["ID", "Nombre", "Apellido", "Telefono", "Correo", "Tipo de usuario"],
    "rows": controlador_user.select_all()["msg"]
  }

  html = usuario_template.render(usuario)
  pdfkit.from_string(html,'reporte_usuario.pdf', configuration=config)
  showinfo("EXITO", "Reporte en PDF generado exitosamente!")

def generar_pdf_vehiculo():    
  path_wkhtmltopdf = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
  config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

  env = Environment(loader=FileSystemLoader("template"))
  usuario_template = env.get_template("reporte.html")

  vehiculo = {
    "from": "Vehiculo",
    "cols": ["ID", "Placa", "Marca", "Modelo", "Fecha", "Color"],
    "rows": mecanico.select_all()["msg"]
  }

  html = usuario_template.render(vehiculo)
  pdfkit.from_string(html,'reporte_vehiculo.pdf', configuration=config)
  showinfo("EXITO", "Reporte en PDF generado exitosamente!")

def generar_pdf_peticion():    
  path_wkhtmltopdf = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
  config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

  env = Environment(loader=FileSystemLoader("template"))
  usuario_template = env.get_template("reporte.html")

  petic = {
    "from": "Peticion",
    "cols": ["ID", "Nombre del cliente", "Apellido del cliente", "Vehiculo", "Informacion"],
    "rows": peticion.select_all()["msg"]
  }

  html = usuario_template.render(petic)
  pdfkit.from_string(html,'reporte_peticion.pdf', configuration=config)
  showinfo("EXITO", "Reporte en PDF generado exitosamente!")

def generar_pdf_respuesta():    
  path_wkhtmltopdf = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
  config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

  env = Environment(loader=FileSystemLoader("template"))
  usuario_template = env.get_template("reporte.html")

  resp = {
    "from": "Respuesta",
    "cols": ["ID", "Nombre del mecanico", "Apellido del mecanico", "Peticion", "Respuesta"],
    "rows": respuesta.select_all()["msg"]
  }

  html = usuario_template.render(resp)
  pdfkit.from_string(html,'reporte_respuesta.pdf', configuration=config)
  showinfo("EXITO", "Reporte en PDF generado exitosamente!")

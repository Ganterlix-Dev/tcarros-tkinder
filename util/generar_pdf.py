from tkinter.messagebox           import *
from jinja2                       import Environment,FileSystemLoader
from controllers.controlador_user import controlador_user
import pdfkit

def generar_pdf_usuario():    
  path_wkhtmltopdf = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
  config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

  env = Environment(loader=FileSystemLoader("template"))
  usuario_template = env.get_template("reporte.html")

  usuario = {
    "cols": ["ID", "Nombre", "Apellido", "Telefono", "Correo", "Tipo de usuario"],
    "rows": controlador_user.select_all()["msg"]
  }

  html = usuario_template.render(usuario)
  pdfkit.from_string(html,'reporte.pdf', configuration=config)
  showinfo("EXITO", "Reporte en PDF generado exitosamente!")



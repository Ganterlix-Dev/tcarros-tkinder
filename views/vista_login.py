from tkinter                      import *
from tkinter.messagebox           import *
from controllers.controlador_user import controlador_user
from views.vista_admin            import Admin_vista
from views.vista_mecanico         import Mecanico_vista
import json

class Inicio_sesion(Frame):
  def iniciar_sesion(self, email, password):
    respuesta = controlador_user.validar_datos(email, password)
    if not respuesta.startswith("Admin") and not respuesta.startswith("Mecanico"):
      showerror("ERROR", respuesta)
    else:
      usuario = controlador_user.select_by_email(email=email)
      usuario = usuario["msg"]
      columns = ["id", "nombre", "apellido", "telefono", "correo", "clave", "tipo_usuario"]
      data    = {}
      sesion  = open("sesion.json", "w")

      for index, value in enumerate(usuario):
        data[columns[index]] = value

      sesion.write(json.dumps(data))
      
      if respuesta == "Admin":
        Admin_vista(self.root, img=self.admin, logo=self.logo)
      else:
        Mecanico_vista(self.root, img=self.mecanico, logo=self.logo)

  def __init__(self, root, admin_img, mecanico_img, logo):
    super().__init__(
      root, 
      bg="#104e8b",
      width=600, height=400,
    )
    self.root     = root
    self.admin    = admin_img
    self.mecanico = mecanico_img
    self.logo     = logo
    self.propagate(False)

    email_variable  = StringVar()
    pass_variable   = StringVar()

    Label(
      self,
      bg="#104e8b",
      text="Inicio de sesion",
      fg="white",
      font=("Calibri", 26)
    ).pack(anchor=CENTER, pady=20)

    Label(
      self,
      bg="#104e8b",
      text="Correo electronico",
      fg="white",
      font=("Calibri", 18),
      width=32, 
      justify="left", anchor=W
    ).pack(anchor=CENTER)

    Entry(
      self,
      borderwidth=0,
      font=("Calibri", 16),
      width=35,
      textvariable=email_variable
    ).pack(anchor=CENTER, pady=10)

    Label(
      self,
      bg="#104e8b",
      text="Clave",
      fg="white",
      font=("Calibri", 18),
      width=32, 
      justify="left", anchor=W
    ).pack(anchor=CENTER)

    Entry(
      self,
      borderwidth=0,
      font=("Calibri", 16),
      width=35,
      show="*",
      textvariable=pass_variable
    ).pack(anchor=CENTER, pady=10)

    Button(
      self,
      borderwidth=0,
      text='Ingresar al sistema',
      font=("Calibri", 18),
      bg="gainsboro",
      cursor="hand2",
      command=lambda: self.iniciar_sesion(email_variable.get(), pass_variable.get())
    ).pack(anchor=CENTER, pady=20)

    self.pack(padx=20, pady=100, anchor=E)
        
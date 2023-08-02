from tkinter                      import *
from tkinter.messagebox           import *
from controllers.controlador_user import controlador_user
from views.vista_admin            import Admin_vista
from views.vista_mecanico         import Mecanico_vista

class Inicio_sesion(Frame):
  def iniciar_sesion(self, email, password):
    respuesta = controlador_user.validar_datos(email, password)
    if not respuesta.startswith("Admin") and not respuesta.startswith("Mecanico"):
      showerror("ERROR", respuesta)
    else:
      if respuesta == "Admin":
        Admin_vista(self.root)
      else:
        Mecanico_vista(self.root)

  def __init__(self, root):
    super().__init__(
      root, 
      bg='steel blue',
      width=600, height=400,
      padx=10, pady=10
    )
    self.root = root
    self.propagate(False)

    email_variable  = StringVar()
    pass_variable   = StringVar()

    Label(
      self,
      text="Inicio de sesion",
      bg="steel blue",
      fg="white",
      font=("Calibri", 26)
    ).pack(anchor=CENTER, pady=20)

    Label(
      self,
      text="Correo electronico",
      bg="steel blue",
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
      text="Clave",
      bg="steel blue",
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

    self.pack(padx=20, pady=20)
        
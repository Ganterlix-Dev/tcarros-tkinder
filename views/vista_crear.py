from tkinter                      import *
from tkinter.messagebox           import *
from controllers.controlador_user import controlador_user
from os                           import remove

class Crear_vista(Toplevel):
  def crear(self,nombre, apellido, telefono, correo, clave, tipo_usuario):
    resultado = controlador_user.insert(nombre, apellido, telefono, correo, clave, tipo_usuario)
    if resultado["error"]:
      showerror("ERROR", resultado["msg"])
    else:
      showinfo("EXITO", "Usuario creado exitosamente")

  def __init__(self, root_admin, root, logo):
    self.root = root
    self.logo = logo

    super().__init__(
      root_admin, 
      bg='steel blue'
    )

    def cerrar():
      remove("sesion.json")
      self.root.destroy()

    self.title("Crear")
    self.geometry("800x600")
    self.resizable(False, False)
    self.propagate(False)
    self.protocol("WM_DELETE_WINDOW", lambda: cerrar())
    self.iconphoto(False, self.logo, self.logo)

    def volver():
      self.destroy()
      root_admin.deiconify()

    content_frame = Frame(
      self, 
      bg='DodgerBlue4',
      width=800, height=600,
      padx=10, pady=10
    )
    content_frame.pack(padx=20, pady=20)
    content_frame.grid_propagate(False)

    Button(
      self,
      text="Volver",
      borderwidth=0,
      bg="firebrick1",
      fg="white",
      font=("Calibri", 14),
      command=volver
    ).place(x=0, y=0)

    datos = ["Nombre", "Apellido", "Telefono", "Correo", "Clave", "Tipo de usuario"]
    
    nombre_variable   = StringVar()
    apellido_variable = StringVar()
    telefono_variable = StringVar()
    correo_variable   = StringVar()
    clave_variable    = StringVar()
    tipo_variable     = StringVar()

    variables = [
      nombre_variable,
      apellido_variable,
      telefono_variable,
      correo_variable,
      clave_variable,
      tipo_variable
    ]
    
    for index, dato in enumerate(datos):
      Label(
        content_frame,
        text=dato,
        bg="DodgerBlue4",
        fg="white",
        font=("Calibri", 16),
        width=32, 
        justify="left", anchor=W
      ).pack(anchor=CENTER)

      Entry(
        content_frame,
        borderwidth=0,
        font=("Calibri", 14),
        width=35,
        textvariable=variables[index]
      ).pack(anchor=CENTER, pady=10)

    Button(
      content_frame,
      borderwidth=0,
      text='Crear',
      font=("Calibri", 18),
      bg="gainsboro",
      cursor="hand2",
      padx=10, pady=10,
      command=lambda: self.crear(
        nombre_variable.get(),
        apellido_variable.get(),
        telefono_variable.get(),
        correo_variable.get(),
        clave_variable.get(),
        tipo_variable.get(),
      )
    ).pack(anchor=CENTER)

    if self:
      root_admin.withdraw()
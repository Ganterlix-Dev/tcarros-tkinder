from tkinter                      import *
from tkinter.messagebox           import *
from controllers.controlador_user import controlador_user

class Crear_vista(Toplevel):
  def crear(self, nombre, apellido, telefono, correo, tipo_usuario):
    resultado = controlador_user.insert(nombre, apellido, telefono, correo, tipo_usuario)
    if resultado["error"]:
      showerror("ERROR", resultado["msg"])
    else:
      showinfo("EXITO", "Usuario creado exitosamente")

  def __init__(self, root):
    self.root = root

    super().__init__(
      root, 
      bg='steel blue',
      padx=10, pady=10
    )

    self.title("Crear")
    self.geometry("800x600")
    self.resizable(False, False)
    self.propagate(False)
    self.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())


    content_frame = Frame(
      self, 
      bg='DodgerBlue4',
      width=800, height=600,
      padx=10, pady=10
    )
    content_frame.pack(padx=20, pady=20)
    content_frame.propagate(False)

    datos = ["Nombre", "Apellido", "Telefono", "Correo", "Tipo de usuario"]
    
    nombre_variable   = StringVar()
    apellido_variable = StringVar()
    telefono_variable = StringVar()
    correo_variable   = StringVar()
    tipo_variable     = StringVar()

    variables = [
      nombre_variable,
      apellido_variable,
      telefono_variable,
      correo_variable,
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
        tipo_variable.get(),
      )
    ).pack(anchor=CENTER)

    if self:
      self.root.withdraw()
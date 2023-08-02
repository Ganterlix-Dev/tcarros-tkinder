from tkinter                      import *
from tkinter.messagebox           import *
from controllers.controlador_user import controlador_user

class Mostrar_vista(Toplevel):
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
    content_frame.grid_propagate(False)

    columnas  = ["ID","Nombre", "Apellido", "Telefono", "Correo", "Tipo de usuario"]
    filas     = controlador_user.select_all()
    filas     = filas["msg"] 
    x         = 0
    y         = 1 

    for col in columnas:
      Label(
        content_frame,
        text=col,
        bg="DodgerBlue4",
        fg="white",
        font=("Calibri", 14),
        justify="left",
        pady=10, padx=15,
      ).grid(row=0, column=x)

      x+=1

    for row in filas:
      x = 0
      for user in row:
        Label(
          content_frame,
          text=user,
          bg="DodgerBlue4",
          fg="white",
          font=("Calibri", 14),
          pady=10, padx=15,
        ).grid(row=y, column=x)
      
        x+=1

      y+=1

    if self:
      self.root.withdraw()
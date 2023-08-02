from tkinter              import *
from views.vista_crear    import Crear_vista
from views.vista_editar   import Editar_vista
from views.vista_mostrar  import Mostrar_vista
from views.vista_eliminar import Eliminar_vista
from util.generar_pdf     import generar_pdf 

class Admin_vista(Toplevel):
  def __init__(self, root):
    self.root = root

    super().__init__(
      root, 
      bg='steel blue',
      padx=10, pady=10
    )

    self.title("CRUD del admin")
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

    Label(
      content_frame,
      text="Bienvenido Admin",
      bg="DodgerBlue4",
      fg="white",
      font=("Calibri", 26)
    ).pack(anchor=CENTER)

    Button( 
      content_frame,
      borderwidth=0,
      text='agregar usuario',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=50,
      command=lambda: Crear_vista(self)
    ).pack(anchor=CENTER, pady=20)

    Button( 
      content_frame,
      borderwidth=0,
      text='editar usuario',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=50,
      command=lambda: Editar_vista(self)
    ).pack(anchor=CENTER, pady=20)

    Button( 
      content_frame,
      borderwidth=0,
      text='mostrar usuarios',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=50,
      command=lambda: Mostrar_vista(self)
    ).pack(anchor=CENTER, pady=20)

    Button( 
      content_frame,
      borderwidth=0,
      text='eliminar usuario',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=50,
      command=lambda: Eliminar_vista(self)
    ).pack(anchor=CENTER, pady=20)

    Button( 
      content_frame,
      borderwidth=0,
      text='generar reporte PDF',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=50,
      command=generar_pdf
    ).pack(anchor=CENTER, pady=20)

    if self:
      self.root.withdraw()


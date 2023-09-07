from tkinter              import *
from tkinter.messagebox   import *

from views.vista_crear    import Crear_vista
from views.vista_editar   import Editar_vista
from views.vista_mostrar  import Mostrar_vista
from views.vista_eliminar import Eliminar_vista
from util.generar_pdf     import generar_pdf 
from os                   import remove

class Admin_vista(Toplevel):
  def __init__(self, root, img, logo):
    self.root = root
    self.img  = img
    self.logo = logo

    super().__init__(root)
    
    Label(self, image=img, width=1200, height=600).place(x=0, y=0)

    def cerrar():
      remove("sesion.json")
      self.root.destroy()

    self.title("CRUD del admin")
    self.geometry("1200x600")
    self.resizable(False, False)
    self.propagate(False)
    self.protocol("WM_DELETE_WINDOW", lambda: cerrar())
    self.iconphoto(False, self.logo, self.logo)

    def salir():
      if askyesno("Seguro?", "Seguro que desea salir?"):
        self.destroy()
        root.deiconify()

    Button(
      self,
      text="Cerrar sesión",
      borderwidth=0,
      bg="firebrick1",
      fg="white",
      font=("Calibri", 14),
      command=salir
    ).place(x=0, y=0)

    Label(
      self,
      text="Bienvenido Admin",
      bg="DodgerBlue4",
      fg="white",
      font=("Calibri", 26)
    ).pack(anchor=W, padx=170, pady=(50, 0))

    Button( 
      self,
      borderwidth=0,
      text='agregar usuario',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: Crear_vista(self, self.root, self.logo)
    ).pack(anchor=W, pady=20, padx=120)

    Button( 
      self,
      borderwidth=0,
      text='editar usuario',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: Editar_vista(self, self.root, self.logo)
    ).pack(anchor=W, pady=20, padx=120)

    Button( 
      self,
      borderwidth=0,
      text='mostrar usuarios',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: Mostrar_vista(self, self.root, self.logo)
    ).pack(anchor=W, pady=20, padx=120)

    Button( 
      self,
      borderwidth=0,
      text='eliminar usuario',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: Eliminar_vista(self, self.root, self.logo)
    ).pack(anchor=W, pady=20, padx=120)

    Button( 
      self,
      borderwidth=0,
      text='generar reporte PDF',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=generar_pdf
    ).pack(anchor=W, pady=20, padx=120)

    if self:
      self.root.withdraw()


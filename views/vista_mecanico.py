from tkinter                import *
from tkinter.messagebox     import *
from views.vista_peticiones import Peticiones_vista
from views.vista_respuesta  import Respuesta_vista
from os                     import remove

class Mecanico_vista(Toplevel):
  def __init__(self, root, img, logo):
    self.root = root
    self.img  = img
    self.logo = logo

    super().__init__(root)

    Label(self, image=img, width=1200, height=600).place(x=0, y=0)

    def cerrar():
      remove("sesion.json")
      self.root.destroy()

    self.title("Vista del mecanico")
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
      text="Bienvenido Mecanico",
      bg="DodgerBlue4",
      fg="white",
      font=("Calibri", 26)
    ).pack(anchor=W, padx=170, pady=(100, 0))

    Button( 
      self,
      borderwidth=0,
      text='ver peticiones',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: Peticiones_vista(self, self.root)
    ).pack(anchor=W, pady=20, padx=120)

    Button( 
      self,
      borderwidth=0,
      text='responder una petición',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: Respuesta_vista(self, self.root)
    ).pack(anchor=W, pady=20, padx=120)

    if self:
      self.root.withdraw()
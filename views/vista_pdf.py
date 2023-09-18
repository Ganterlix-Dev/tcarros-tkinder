from tkinter              import *
from tkinter.messagebox   import *

from os                   import remove

class PDF_Vista(Toplevel):
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

    self.title("Generar PDFs")
    self.geometry("800x600")
    self.resizable(False, False)
    self.propagate(False)
    self.protocol("WM_DELETE_WINDOW", lambda: cerrar())
    self.iconphoto(False, self.logo, self.logo)

    def salir():
      if askyesno("Seguro?", "Seguro que desea salir?"):
        remove("sesion.json")
        self.destroy()
        root.deiconify()

    Button(
      self,
      borderwidth=0,
      text="Cerrar sesión",
      bg="firebrick1",
      fg="white",
      font=("Calibri", 14),
      command=salir
    ).place(x=0, y=0)

    Button( 
      self,
      borderwidth=0,
      text='Generar reporte de usuarios',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: showinfo("creando", "creando pdf:p")
    ).pack(anchor=CENTER, pady=20, padx=120)

    Button( 
      self,
      borderwidth=0,
      text='Generar reporte de vehiculos',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: showinfo("creando", "creando pdf:p")
    ).pack(anchor=CENTER, pady=20, padx=120)

    Button( 
      self,
      borderwidth=0,
      text='Generar reporte de peticiones',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: showinfo("creando", "creando pdf:p")
    ).pack(anchor=CENTER, pady=20, padx=120)

    Button( 
      self,
      borderwidth=0,
      text='Generar reporte de respuestas',
      font=("Calibri", 18),
      bg="gainsboro",
      fg="black",
      cursor="hand2",
      width=30,
      command=lambda: showinfo("creando", "creando pdf:p")
    ).pack(anchor=CENTER, pady=20, padx=120)

    if self:
      root_admin.withdraw()


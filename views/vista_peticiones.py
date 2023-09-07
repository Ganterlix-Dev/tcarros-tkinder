from tkinter import *
from controllers.controlador_peticion import peticion as peticion_modelo
from os import remove


class Peticiones_vista(Toplevel):
  def __init__(self, root_admin, root):
    self.root = root

    super().__init__(root_admin, bg='DodgerBlue4', padx=20, pady=20)

    def cerrar():
      remove("sesion.json")
      self.root.destroy()

    self.title("Peticiones")
    self.geometry("1200x600")
    self.resizable(False, False)
    self.propagate(False)
    self.protocol("WM_DELETE_WINDOW", lambda: cerrar())

    def volver():
      self.destroy()
      root_admin.deiconify()

    content_frame = Frame(
      self, 
      bg='DeepSkyBlue4',
      width=1000, height=600,
      padx=10, pady=10
    )
    content_frame.pack(padx=10, pady=10)
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

    peticiones = peticion_modelo.select_all()

    Label(
      content_frame,
      text="ID",
      bg="DeepSkyBlue4",
      fg="white",
      font=("Calibri", 14)
    ).grid(row=0, column=0, padx=50)

    Label(
      content_frame,
      text="Nombre y apellido del cliente",
      bg="DeepSkyBlue4",
      fg="white",
      font=("Calibri", 14)
    ).grid(row=0, column=1, padx=50)

    Label(
      content_frame,
      text="Marca del vehiculo del cliente",
      bg="DeepSkyBlue4",
      fg="white",
      font=("Calibri", 14)
    ).grid(row=0, column=2, padx=50)

    Label(
      content_frame,
      text="Problema",
      bg="DeepSkyBlue4",
      fg="white",
      font=("Calibri", 14)
    ).grid(row=0, column=3, padx=50)

    row_count = 1

    for peticion in peticiones:
      Label(
        content_frame,
        text=peticion[0],
        bg="DeepSkyBlue4",
        fg="white",
        font=("Calibri", 14)
      ).grid(row=row_count, column=0, padx=15, pady=10)

      Label(
        content_frame,
        text=f"{peticion[1]} {peticion[2]}",
        bg="DeepSkyBlue4",
        fg="white",
        font=("Calibri", 14)
      ).grid(row=row_count, column=1, padx=15, pady=10)

      Label(
        content_frame,
        text=peticion[3],
        bg="DeepSkyBlue4",
        fg="white",
        font=("Calibri", 14)
      ).grid(row=row_count, column=2, padx=15, pady=10)

      words = peticion[4].split()

      for index, _ in enumerate(words):
        if (index + 1) % 4 == 0:
          words.insert(index, "\n")

      Label(
        content_frame,
        text=" ".join(words),
        bg="DeepSkyBlue4",
        fg="white",
        font=("Calibri", 14)
      ).grid(row=row_count, column=3, padx=15, pady=10)

      row_count += 1

    if self:
      root_admin.withdraw()
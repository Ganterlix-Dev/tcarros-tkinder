from tkinter                      import *
from tkinter.messagebox           import *
from controllers.controlador_user import controlador_user
from os                           import remove

class Editar_vista(Toplevel):
  def editar(self, id, nombre, apellido, telefono, correo, tipo_usuario):
    resultado = controlador_user.update(id, nombre, apellido, telefono, correo, tipo_usuario)
    if resultado["error"]:
      showerror("ERROR", resultado["msg"])
    else:
      showinfo("EXITO", "Usuario editado exitosamente")

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

    datos = ["Nombre", "Apellido", "Telefono", "Correo", "Tipo de usuario"]
    
    id_variable       = StringVar()

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

    id_label = Label(
      content_frame,
      text="ID del usuario a editar",
      bg="DodgerBlue4",
      fg="white",
      font=("Calibri", 16),
      width=32, 
      justify="left", anchor=W
    )
    id_label.pack(anchor=CENTER)

    id_entry = Entry(
      content_frame,
      borderwidth=0,
      font=("Calibri", 14),
      width=35,
      textvariable=id_variable
    )
    id_entry.pack(anchor=CENTER, pady=10)

    buscar_btn = Button(
      content_frame,
      borderwidth=0,
      text='Buscar',
      font=("Calibri", 18),
      bg="gainsboro",
      cursor="hand2",
      padx=10, pady=10,
      command=lambda: on_search(id_variable.get())
    )
    buscar_btn.pack(anchor=CENTER)

    def on_search(id):
      if not id:
        showerror("ERROR", "Ingrese un id")
      try:
        id = int(id)
      except ValueError:
        showerror("ERROR", "El id debe ser un numero")
      else:
        resultado = controlador_user.select_one(id)
        if not resultado["msg"]:
          showerror("ERROR", "Usuario no encontrado")
        else:
          on_update(id_label, id_entry, buscar_btn, resultado["msg"])
    
    def on_update(id_label, id_entry, buscar_btn, user):
      user = [user[1], user[2], user[3], user[4], user[6]]
      id_label.destroy()
      id_entry.destroy()
      buscar_btn.destroy()
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

        entry = Entry(
          content_frame,
          borderwidth=0,
          font=("Calibri", 14),
          width=35,
          textvariable=variables[index]
        )
        entry.insert(INSERT, user[index])
        entry.pack(anchor=CENTER, pady=10)

      Button(
        content_frame,
        borderwidth=0,
        text='Editar',
        font=("Calibri", 18),
        bg="gainsboro",
        cursor="hand2",
        padx=10, pady=10,
        command=lambda: self.editar(
          id_variable.get(),
          nombre_variable.get(),
          apellido_variable.get(),
          telefono_variable.get(),
          correo_variable.get(),
          tipo_variable.get(),
        )
      ).pack(anchor=CENTER)

    if self:
      root_admin.withdraw()
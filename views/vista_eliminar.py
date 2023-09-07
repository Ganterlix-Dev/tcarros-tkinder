from tkinter                      import *
from tkinter.messagebox           import *
from controllers.controlador_user import controlador_user
from os                           import remove

class Eliminar_vista(Toplevel):
  def eliminar(self, id):
    if askyesno("Estas seguro", "Seguro de eliminar a este usuario?"):
      resultado = controlador_user.delete(id)
      if resultado["msg"] == 0 or resultado["error"]:
        showerror("ERROR", "Usuario no encontrado")
      else:
        showinfo("EXITO", "Usuario eliminado exitosamente")

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
    
    id_variable       = StringVar()

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
      text='Eliminar',
      font=("Calibri", 18),
      bg="gainsboro",
      cursor="hand2",
      padx=10, pady=10,
      command=lambda: self.eliminar(id_variable.get())
    )
    buscar_btn.pack(anchor=CENTER)

    if self:
      root_admin.withdraw()
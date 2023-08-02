from tkinter                      import *
from tkinter.messagebox           import *
from controllers.controlador_user import controlador_user

class Eliminar_vista(Toplevel):
  def eliminar(self, id):
    if askyesno("Estas seguro", "Seguro de eliminar a este usuario?"):
      resultado = controlador_user.delete(id)
      if resultado["msg"] == 0 or resultado["error"]:
        showerror("ERROR", "Usuario no encontrado")
      else:
        showinfo("EXITO", "Usuario eliminado exitosamente")

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
      self.root.withdraw()
from tkinter import *

class Mecanico_vista(Toplevel):
  def __init__(self, root):
    self.root = root

    super().__init__(
      root, 
      bg='steel blue',
      padx=10, pady=10
    )

    self.title("Vista del mecanico")
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
      text="Vista de mecanico",
      bg="DodgerBlue4",
      fg="white",
      font=("Calibri", 26)
    ).pack(anchor=CENTER)

    if self:
      self.root.withdraw()
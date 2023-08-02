from tkinter            import Tk
from views.vista_login  import Inicio_sesion

root = Tk()
root.title("Inicio de sesion")
root.geometry("600x400")
root.resizable(False, False)

Inicio_sesion(root)

root.mainloop()


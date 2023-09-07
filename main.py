from tkinter            import *
from views.vista_login  import Inicio_sesion

root = Tk()
root.title("Inicio de sesion")
root.geometry("1200x600")
root.resizable(False, False)

logo          = PhotoImage(file="img/logo.png")
img           = PhotoImage(file="img/loginn.png")
admin_img     = PhotoImage(file="img/admin.png")
mecanico_img  = PhotoImage(file="img/mecanico.png")

root.iconphoto(False, logo, logo)

Label(root, image=img, width=1200, height=600).place(x=0, y=0)

Inicio_sesion(root, admin_img=admin_img, mecanico_img=mecanico_img, logo=logo)

root.mainloop()


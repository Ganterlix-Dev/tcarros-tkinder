from tkinter                          import *
from tkinter.messagebox               import *
from controllers.controlador_peticion import peticion as peticion_controlador
from os                               import remove
import json

class Respuesta_vista(Toplevel):
  def __init__(self, root_admin, root):
    self.root = root

    super().__init__(root_admin, bg='steel blue', padx=20, pady=20)

    def cerrar():
      remove("sesion.json")
      self.root.destroy()
    
    self.title("Respuesta")
    self.geometry("1000x600")
    self.resizable(False, False)
    self.propagate(False)
    self.protocol("WM_DELETE_WINDOW", lambda: cerrar())

    def volver():
      self.destroy()
      root_admin.deiconify()

    content_frame = Frame(
      self, 
      bg='DeepSkyBlue4',
      width=800, height=400,
      padx=10, pady=10
    )
    content_frame.pack(padx=10, pady=10)

    Button(
      self,
      text="Volver",
      borderwidth=0,
      bg="firebrick1",
      fg="white",
      font=("Calibri", 14),
      command=volver
    ).place(x=0, y=0)

    datos = ["Usuario", "Vehiculo", "Problema"]

    id_variable         = StringVar()
    
    respuesta_variable  = StringVar()

    id_label = Label(
      content_frame,
      text="ID de la petición",
      bg="DeepSkyBlue4",
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
      command=lambda: buscar_peticion(id_variable.get())
    )
    buscar_btn.pack(anchor=CENTER)

    def buscar_peticion(id):
      if not id:
        showerror("ERROR", "Ingrese un id")
      try:
        id = int(id)
      except ValueError:
        showerror("ERROR", "El id debe ser un numero")
      else:
        peticion = peticion_controlador.select_one(id)
        if not peticion:
          showerror("ERROR", "Peticion no encontrada. Intente con otro id")
        else: actualizar_campos(id_label, id_entry, buscar_btn, peticion[0], id)

    def responder(id_peticion, respuesta):
      sesion = open("sesion.json", "r")
      datos_mecanico  = sesion.readlines()[0]
      datos_mecanico  = json.loads(datos_mecanico) #Datos convertidos a JSON
      
      id_mecanico     = datos_mecanico["id"] #Extraigo el id del mecanico del JSON

      print(id_mecanico, id_peticion, respuesta) #Estos son los datos que debes pasarle al controlador con el metodo insert que TU VAS A CREAR

      # Ahora lo que tienes que hacer es crear el modelo y el controlador de la tabla respuesta

      # models -> modelo_respuesta.py
      # controllers -> controlador_respuesta.py

      # Tanto en el modelo como en el controlador vas a crear la clase y agregarle el metodo insert con los parametros mecanico (donde ira el id del mecanico), peticion (donde ira el id de la peticion), y la respuesta (que seria la info de la respuesta)

      # Cuando crees ambos importas el controlador y llamas al metodo pasandole los parametros:

      # controlador_respuesta.insert(id_mecanico, id_peticion, respuesta)

      # Y por ultimo muestras un mensaje con showinfo que diga que la respuesta se registro exitosamente

    def actualizar_campos(id_label, id_entry, buscar_btn, peticion, id):
      words = peticion[4].split()
      
      for index, _ in enumerate(words):
        if (index + 1) % 4 == 0:
          words.insert(index, "\n")
      
      peticion = [peticion[1] + " " + peticion[2], peticion[3], " ".join(words)]

      id_label.destroy()
      id_entry.destroy()
      buscar_btn.destroy()

      iterador = 0

      for index, dato in enumerate(datos):
        Label(
          content_frame,
          text=dato,
          fg="white",
          bg="DeepSkyBlue4",
          font=("Calibri", 16), 
          justify="left", anchor=W
        ).grid(row=0, column=iterador, pady=10)

        Label(
          content_frame,
          text=peticion[index],
          fg="white",
          bg="DeepSkyBlue4",
          font=("Calibri", 16), 
          justify="left", anchor=W
        ).grid(row=1, column=iterador, pady=10)

        iterador+=1

      Label(
        content_frame,
        text="Respuesta",
        fg="white",
        bg="DeepSkyBlue4",
        font=("Calibri", 16), 
        justify="left", anchor=W
      ).grid(row=2, column=0, pady=10)

      Entry(
        content_frame,
        borderwidth=0,
        font=("Calibri", 16),
        width=50,
        textvariable=respuesta_variable
      ).grid(row=2, column=1, pady=10)

      Button(
        content_frame,
        borderwidth=0,
        text='Responder',
        font=("Calibri", 18),
        bg="gainsboro",
        cursor="hand2",
        padx=10, pady=10,
        command=lambda: responder(
          id, respuesta_variable.get()
        )
      ).grid(row=3, column=1)

    if self:
      root_admin.withdraw()
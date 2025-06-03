import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class trabajador():
    
    def __init__(self,nombre,apellido,edad):
      self.nombre = nombre
      self.apellido = apellido
      self.edad = edad
    def datos(self):
      tk.Label(ventanap, text="Hola {self.nombre} {self.apellido} con {self.edad}")
    def periodo():
     tk.Label(ventanap, text="vacaciones").pack()


     tk.Label(ventanap, text="selección su grupo:").pack()
     opcion = tk.StringVar(value="invierno")
     tk.Radiobutton(ventanap, text="invierno", variable=opcion, value="invierno").pack()
     tk.Radiobutton(ventanap, text="primavera", variable=opcion, value="primavera").pack()
     tk.Radiobutton(ventanap, text="verano", variable=opcion, value="verano").pack()
     tk.Radiobutton(ventanap, text="otoño", variable=opcion, value="otoño").pack()

     tk.Label(ventanap, text="Numero de lista:").pack()
     combo = ttk.Combobox(ventanap, values=["Uno", "Dos", "Tres","cuatro"])
     combo.pack()
     combo.current(0)
t1 = trabajador("rodrigo","perez","24")
t1.datos("rodrigo","perez","24")
ventanap = tk.Tk()
ventanas = tk.Frame(ventanap, bg="white", width=120)
ventanas.pack(side="left", fill="y")
ventanap.title("control de asistencias")
ventanap.geometry("420x250")
boton1 = tk.Button(ventanas,text="vacaciones",width=15).pack(pady=10)
ventanap.mainloop()

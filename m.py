import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class trabajador():
    
    def __init__(self,nombre,edad):
      self.lista = []
      self.ventanap = ventanap
      self.nombre = nombre
      self.edad = edad
    def datos(self):
      self.areas()
      tk.Label(ventanap, text=f"Hola {self.nombre} {self.apellido} con {self.edad}")
    def periodo(self):
     tk.Label(ventanap, text="vacaciones").pack()
     
     tk.Label(ventanap, text="selección su grupo:").pack()
     self.opcion = tk.StringVar(value="invierno")
     tk.Radiobutton(ventanap, text="invierno", variable=self.opcion, value="invierno").pack()
     tk.Radiobutton(ventanap, text="primavera", variable=self.opcion, value="primavera").pack()
     tk.Radiobutton(ventanap, text="verano", variable=self.opcion, value="verano").pack()
     tk.Radiobutton(ventanap, text="otoño", variable=self.opcion, value="otoño").pack()

     tk.Label(ventanap, text="Numero de lista:").pack()
     self.combo = ttk.Combobox(ventanap, values=["Uno", "Dos", "Tres","cuatro"])
     self.combo.pack()
     self.combo.current(0)
    def agregar (self,nombre):
        if self.nombre not in self.lista:
            self.lista.append(self.nombre) 
        else:
            tk.Label(ventanap,text=f"{self.nombre} ya esta agregado").pack()
    def lista_de_trabajadore(self):
        tk.Label(ventanap,text="lista de empleados").pack()
        for nombre in self.lista:
            tk.Label(ventanap,text=f"{self.nombre}").pack()
    def areas():
     for widget in areas.winfo_children():
        widget.destroy()
ventanap = tk.Tk()
ventanap.title("control de asistencias")
ventanap.geometry("420x250")
areas = tk.Frame(ventanap, bg="white")
areas.pack(side="right", expand=True, fill="both")
ventanas = tk.Frame(ventanap, bg="white", width=120)
ventanas.pack(side="left", fill="y")
boton1 = tk.Button(ventanas,text="vacaciones",width=15).pack(pady=10)
ventanap.mainloop()
ventanas.pack(side="left", fill="y")
ventanap.title("control de asistencias")
ventanap.geometry("420x250")
boton1 = tk.Button(ventanas,text="vacaciones",width=15).pack(pady=10)
ventanap.mainloop()

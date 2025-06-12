import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class trabajador():
    
    def __init__(self, nombre, edad):
        self.lista = []
        self.nombre = nombre
        self.edad = edad


    def periodo(self):
        for widget in areas.winfo_children():
            widget.destroy()
        tk.Label(areas, text="vacaciones:").pack()
        tk.Label(areas, text="seleccione su periodo de vacaciones:").pack()
        self.opcion = tk.StringVar(value="invierno")
        tk.Radiobutton(areas, text="invierno", variable=self.opcion, value="invierno").pack()
        tk.Radiobutton(areas, text="primavera", variable=self.opcion, value="primavera").pack()
        tk.Radiobutton(areas, text="verano", variable=self.opcion, value="verano").pack()
        tk.Radiobutton(areas, text="otoño", variable=self.opcion, value="otoño").pack()
        tk.Label(areas, text="numero de lista:").pack()
        self.combo = ttk.Combobox(areas, values=["uno", "dos", "tres", "cuatro"])
        self.combo.pack()
        self.combo.current(0)

        def vacaciones():
            periodo = self.opcion.get()
            numero = self.combo.get()
            self.periodovacaciones = (periodo, numero)
            tk.Label(areas, text=f"vacaciones asignadas: {periodo}, lista {numero}").pack()

        tk.Button(areas, text="asignar", command=vacaciones).pack(pady=5)
    def datos(self):
        for widget in areas.winfo_children():
            widget.destroy()
        tk.Label(areas, text=f"hola {self.nombre} con {self.edad}").pack()
        if hasattr(self, 'periodovacaciones'):
            periodo, numero = self.periodovacaciones
            tk.Label(areas, text=f"vacaciones asignadas: {periodo}, lista {numero}").pack()
        else:
            tk.Label(areas, text="vacaciones no asignadas aun.").pack()

    def agregar(self):
        if self.nombre not in self.lista:
            self.lista.append(self.nombre)
        else:
            tk.Label(areas, text=f"{self.nombre} ya esta agregado").pack()

    def listadetrabajadores(self):
        self.areas()
        tk.Label(areas, text="lista de empleados").pack()
        for nombre in self.lista:
            tk.Label(areas, text=f"{nombre}").pack()
ventanap = tk.Tk()
ventanap.title("control de asistencias")
ventanap.geometry("420x250")
areas = tk.Frame(ventanap, bg="white")
areas.pack(side="right", expand=True, fill="both")
ventanas = tk.Frame(ventanap, bg="white", width=120)
ventanas.pack(side="left", fill="y")
tk.Label(ventanas, text="seleccione una opcion del menu:").pack(padx=10)
trabajador1 = trabajador("juan", 30)
boton1 = tk.Button(ventanas, text="vacaciones", width=15, command=trabajador1.periodo)
boton1.pack(pady=10)
boton2 = tk.Button(ventanas, text="datos", width=15, command=trabajador1.datos)
boton2.pack(pady=5)
boton3 = tk.Button(ventanas, text="lista de empleados", width=15, command=trabajador1.listadetrabajadores)
boton3.pack(pady=5)
ventanap.mainloop()

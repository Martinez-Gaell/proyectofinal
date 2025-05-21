import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

trabajador1 = {
    
}
trabajador2 = {
    
}
trabajador3 = {
    
}
trabajador4 ={
    
}
def periodos():
    tk.Label(ventanap, text="vacaciones").pack()
    tk.Label(ventanap, text="datos del alumno", font=("Arial", 14)).pack(pady=10)

    tk.Label(ventanap, text="ingrese el nombre del alumno").pack()
    campo_texto_uno = tk.Entry(ventanap)
    campo_texto_uno.pack(pady=5)

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
ventanap = tk.Tk()
ventanas = tk.Frame(ventanap, bg="white", width=120)
ventanas.pack(side="left", fill="y")
ventanap.title("control de asistencias")
ventanap.geometry("420x250")
boton1 = tk.Button(ventanas,text="vacaciones",width=15).pack(pady=10)
ventanap.mainloop()
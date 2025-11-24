import tkinter as tk
from tkinter import messagebox
from controller.controlador_coches import ControladoresCoches

class InterfazCoches:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Coches")
        self.ventana.geometry("650x500")

        tk.Label(self.ventana, text="Marca").pack()
        self.marca = tk.Entry(self.ventana)
        self.marca.pack()

        tk.Label(self.ventana, text="Modelo").pack()
        self.modelo = tk.Entry(self.ventana)
        self.modelo.pack()

        tk.Label(self.ventana, text="Precio").pack()
        self.precio = tk.Entry(self.ventana)
        self.precio.pack()

        tk.Button(self.ventana, text="Guardar Coche", command=self.guardar).pack(pady=5)
        tk.Button(self.ventana, text="Mostrar Coches", command=self.mostrar).pack(pady=5)

        self.resultado = tk.Text(self.ventana, height=12, width=80)
        self.resultado.pack()

        self.ventana.mainloop()

    def guardar(self):
        mensaje = ControladoresCoches.guardar_coche(
            self.marca.get(),
            self.modelo.get(),
            self.precio.get()
        )
        messagebox.showinfo("Resultado", mensaje)

    def mostrar(self):
        self.resultado.delete("1.0", tk.END)
        for coche in ControladoresCoches.consultar_coches():
            self.resultado.insert(
                tk.END,
                f"ID:{coche[0]} | {coche[2]} {coche[3]} - ${coche[4]}\n"
            )

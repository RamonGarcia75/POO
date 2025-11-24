import tkinter as tk
from tkinter import messagebox
from controller.controlador_notas import ControladoresNotas

class InterfazNotas:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Notas")
        self.ventana.geometry("650x500")

        tk.Label(self.ventana, text="Título").pack()
        self.titulo = tk.Entry(self.ventana, width=50)
        self.titulo.pack()

        tk.Label(self.ventana, text="Contenido").pack()
        self.contenido = tk.Text(self.ventana, height=5, width=50)
        self.contenido.pack()

        tk.Button(self.ventana, text="Guardar Nota", command=self.guardar).pack(pady=5)
        tk.Button(self.ventana, text="Mostrar Notas", command=self.mostrar).pack(pady=5)

        self.resultado = tk.Text(self.ventana, height=12, width=80)
        self.resultado.pack()

        self.ventana.mainloop()

    def guardar(self):
        mensaje = ControladoresNotas.guardar_nota(
            self.titulo.get(),
            self.contenido.get("1.0", tk.END)
        )
        messagebox.showinfo("Resultado", mensaje)

    def mostrar(self):
        self.resultado.delete("1.0", tk.END)
        for nota in ControladoresNotas.consultar_notas():
            self.resultado.insert(tk.END, f"ID:{nota[0]} | {nota[2]} -> {nota[3]}\n")

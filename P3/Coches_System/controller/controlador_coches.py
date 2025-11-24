from model.modelo_coches import Coches
from tkinter import messagebox

class ControladoresCoches:

    def guardar_coche(self, marca, modelo, precio):
        if marca == "" or modelo == "" or precio == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        respuesta = Coches.insertar(marca, modelo, precio)
        self.respuesta_sql("Guardar", respuesta)

    def consultar_coches(self):
        return Coches.mostrar()

    def cambiar_coche(self, marca, modelo, precio, id):
        respuesta = Coches.actualizar(marca, modelo, precio, id)
        self.respuesta_sql("Actualizar", respuesta)

    def eliminar_coche(self, id):
        respuesta = Coches.eliminar(id)
        self.respuesta_sql("Eliminar", respuesta)

    def respuesta_sql(self, titulo, respuesta):
        if respuesta:
            messagebox.showinfo(titulo, "Operación realizada con éxito")
        else:
            messagebox.showerror(titulo, "Ocurrió un error")

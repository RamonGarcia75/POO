from model.modelo_notas import Notas

class ControladoresNotas:

    @staticmethod
    def guardar_nota(titulo, contenido):
        if titulo == "" or contenido == "":
            return "Campos vacíos ❌"
        return "Nota guardada ✅" if Notas.insertar(titulo, contenido) else "Error ❌"

    @staticmethod
    def consultar_notas():
        return Notas.mostrar()

    @staticmethod
    def eliminar_nota(id):
        return "Nota eliminada ✅" if Notas.eliminar(id) else "Error ❌"

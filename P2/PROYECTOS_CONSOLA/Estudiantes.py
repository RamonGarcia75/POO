class Estudiante:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
        self.NOTA_MINIMA_APROBACION = 70

    def imprimir_datos(self):
        print("Datos del Estudiante")
        print(f"Nombre: {self.nombre}")
        print(f"Nota Obtenida: {self.nota}")

    def mostrar_resultado(self):
        print("\n--- Resultado ---")
        
#from conexionBD import import *

class Estudiante:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        try:
            nota = float(nota)
            if not 0 <= nota <= 100:
                raise ValueError("La nota debe estar entre 0 y 100.")
            self._nota = nota
        except ValueError:
            raise ValueError("La nota debe ser un número válido.")

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrar(self):
        print("\n--- Resultado ---")
        if self.nota >= 60:
            print(f"¡Felicidades, {self.nombre}! Has APROBADO con {self.nota}.")
        else:
            print(f"Lo siento, {self.nombre}. Has REPROBADO con {self.nota}.")

    @staticmethod
    def insertar(nombre, nota):
        print(">>> Implementar código SQL para INSERTAR aquí <<<")
        # Ejemplo: return conexionBD.ejecutar_sql("INSERT INTO estudiantes (nombre, nota) VALUES (%s, %s)", (nombre, nota))
        return "Registro insertado (Simulado)"

    @staticmethod
    def consultar():
        print(">>> Implementar código SQL para CONSULTAR aquí <<<")
        # Ejemplo: return conexionBD.ejecutar_sql("SELECT id, nombre, nota FROM estudiantes")
        return []

    @staticmethod
    def actualizar(nombre, nota, id_estudiante):
        print(">>> Implementar código SQL para ACTUALIZAR aquí <<<")
        # Ejemplo: return conexionBD.ejecutar_sql("UPDATE estudiantes SET nombre=%s, nota=%s WHERE id=%s", (nombre, nota, id_estudiante))
        return "Registro actualizado (Simulado)"

    @staticmethod
    def eliminar(id_estudiante):
        print(">>> Implementar código SQL para ELIMINAR aquí <<<")
        # Ejemplo: return conexionBD.ejecutar_sql("DELETE FROM estudiantes WHERE id=%s", (id_estudiante,))
        return "Registro eliminado (Simulado)"
 
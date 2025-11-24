from conexionBD import ConexionBD
from datetime import datetime

class Coches:

    @staticmethod
    def insertar(marca, modelo, precio):
        try:
            conexion = ConexionBD.conectar()
            cursor = conexion.cursor()
            sql = "INSERT INTO coches (fecha, marca, modelo, precio) VALUES (%s, %s, %s, %s)"
            fecha = datetime.now()
            valores = (fecha, marca, modelo, precio)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print("Error al insertar:", e)
            return False

    @staticmethod
    def mostrar():
        try:
            conexion = ConexionBD.conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM coches")
            return cursor.fetchall()
        except Exception as e:
            print("Error al mostrar:", e)
            return []

    @staticmethod
    def actualizar(marca, modelo, precio, id):
        try:
            conexion = ConexionBD.conectar()
            cursor = conexion.cursor()
            sql = "UPDATE coches SET marca=%s, modelo=%s, precio=%s WHERE id=%s"
            valores = (marca, modelo, precio, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print("Error al actualizar:", e)
            return False

    @staticmethod
    def eliminar(id):
        try:
            conexion = ConexionBD.conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM coches WHERE id=%s", (id,))
            conexion.commit()
            return True
        except Exception as e:
            print("Error al eliminar:", e)
            return False

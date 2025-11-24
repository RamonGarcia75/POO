from conexionBD import ConexionBD
from datetime import datetime

class Notas:

    @staticmethod
    def insertar(titulo, contenido):
        conexion = ConexionBD.conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO notas (fecha, titulo, contenido) VALUES (%s,%s,%s)"
        cursor.execute(sql, (datetime.now(), titulo, contenido))
        conexion.commit()
        return True

    @staticmethod
    def mostrar():
        conexion = ConexionBD.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM notas")
        return cursor.fetchall()

    @staticmethod
    def eliminar(id):
        conexion = ConexionBD.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM notas WHERE id=%s", (id,))
        conexion.commit()
        return True

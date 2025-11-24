import mysql.connector

class ConexionBD:
    @staticmethod
    def conectar(base_datos):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=base_datos
        )

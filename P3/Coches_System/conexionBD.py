import mysql.connector

class ConexionBD:
    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_coches_system"
        )
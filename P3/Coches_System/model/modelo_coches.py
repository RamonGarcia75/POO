import mysql.connector
from tkinter import messagebox

# --- CONFIGURACIÓN DE CONEXIÓN (Usando tu script) ---
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_coches'
    )
    cursor = conexion.cursor(buffered=True)
except mysql.connector.Error as err:
    messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos: {err}")
    conexion = None
    cursor = None
except Exception as e:
    messagebox.showerror("Error General", f"Ocurrió un error inesperado: {e}")
    conexion = None
    cursor = None

# --- CLASE MODELO/PERSISTENCIA ---
class GestorVehicular:
    @staticmethod
    def _ejecutar_consulta(consulta, parametros=None, es_select=False):
        """Función interna para manejar la ejecución de consultas y errores de BD."""
        if not conexion or not cursor:
            # El error ya fue notificado en la conexión inicial, solo retorna fallo.
            return [] if es_select else False

        try:
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            
            if es_select:
                return cursor.fetchall()
            else:
                conexion.commit()
                return True
        except mysql.connector.Error as err:
            conexion.rollback()
            messagebox.showerror("Error de BD", f"Error al ejecutar la operación: {err}")
            return [] if es_select else False

    # ----------------------------------------
    # AUTOS (CRUD)
    # ----------------------------------------

    @staticmethod
    def insertar_auto(marca, color, modelo, velocidad, caballaje, plazas):
        sql = "INSERT INTO autos (marca, color, modelo, velocidad, caballaje, plazas) VALUES (%s, %s, %s, %s, %s, %s)"
        parametros = (marca, color, modelo, velocidad, caballaje, plazas)
        return GestorVehicular._ejecutar_consulta(sql, parametros)

    @staticmethod
    def consultar_autos():
        sql = "SELECT id, marca, color, modelo, velocidad, caballaje, plazas FROM autos"
        return GestorVehicular._ejecutar_consulta(sql, es_select=True)
        
    @staticmethod
    def cambiar_auto(id_auto, nueva_marca):
        sql = "UPDATE autos SET marca = %s WHERE id = %s"
        parametros = (nueva_marca, id_auto)
        return GestorVehicular._ejecutar_consulta(sql, parametros)

    @staticmethod
    def borrar_auto(id_auto):
        sql = "DELETE FROM autos WHERE id = %s"
        return GestorVehicular._ejecutar_consulta(sql, (id_auto,))

    # ----------------------------------------
    # CAMIONETAS (CRUD)
    # ----------------------------------------
    
    @staticmethod
    def insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        # Mapea el booleano de Python a 1/0 para MySQL
        cerrada_bd = 1 if cerrada else 0 
        sql = "INSERT INTO camionetas (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        parametros = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada_bd)
        return GestorVehicular._ejecutar_consulta(sql, parametros)

    @staticmethod
    def consultar_camionetas():
        sql = "SELECT id, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada FROM camionetas"
        return GestorVehicular._ejecutar_consulta(sql, es_select=True)
        
    @staticmethod
    def cambiar_camioneta(id_camioneta):
        # Esta función requiere más parámetros si quieres cambiar campos. Es un placeholder.
        messagebox.showinfo("Modelo", f"Lógica de Actualizar Camioneta ID: {id_camioneta} debe ser implementada con todos los campos.")
        return True 

    @staticmethod
    def borrar_camioneta(id_camioneta):
        sql = "DELETE FROM camionetas WHERE id = %s"
        return GestorVehicular._ejecutar_consulta(sql, (id_camioneta,))

    # ----------------------------------------
    # CAMIONES (CRUD)
    # ----------------------------------------

    @staticmethod
    def insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, ejes, cap_carga):
        sql = "INSERT INTO camiones (marca, color, modelo, velocidad, caballaje, plazas, ejes, cap_carga) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        parametros = (marca, color, modelo, velocidad, caballaje, plazas, ejes, cap_carga)
        return GestorVehicular._ejecutar_consulta(sql, parametros)

    @staticmethod
    def consultar_camiones():
        sql = "SELECT id, marca, color, modelo, velocidad, caballaje, plazas, ejes, cap_carga FROM camiones"
        return GestorVehicular._ejecutar_consulta(sql, es_select=True)

    @staticmethod
    def cambiar_camion(id_camion):
        # Esta función requiere más parámetros si quieres cambiar campos. Es un placeholder.
        messagebox.showinfo("Modelo", f"Lógica de Actualizar Camión ID: {id_camion} debe ser implementada con todos los campos.")
        return True 

    @staticmethod
    def borrar_camion(id_camion):
        sql = "DELETE FROM camiones WHERE id = %s"
        return GestorVehicular._ejecutar_consulta(sql, (id_camion,)) 
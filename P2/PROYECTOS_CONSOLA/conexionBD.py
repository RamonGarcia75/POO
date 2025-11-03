import mysql.connector

try:
    # Conectar con la BD en MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='', # Deja la contraseña vacía si no tienes una en phpMyAdmin/MySQL local
        database='sistema_estudiantes' # Usamos el nombre que definimos antes
    )
    
    # Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    # buffered=True permite ejecutar múltiples consultas sin problemas
    cursor = conexion.cursor(buffered=True) 

except Exception as e:
    # Captura el error específico para ayudar al usuario
    print(f"Ocurrió un error con la conexión a la Base de Datos. Por favor verifica tus credenciales y que MySQL esté activo.")
    print(f"Detalle del error: {e}")
    
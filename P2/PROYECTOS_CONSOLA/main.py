import os
from Estudiantes import Estudiante

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def esperarTecla(self):
        print("\nPresiona ENTER para continuar...")
        input()

    def datos_estudiante(self, tipo):
        self.borrarPantalla()
        print(f"--- {tipo.upper()} ESTUDIANTE ---")
        nombre = input("Nombre del Estudiante: ")
        
        while True:
            try:
                nota = float(input("Nota del Estudiante (0-10): "))
                if not 0 <= nota <= 10:
                    print("La nota debe estar entre 0 y 10.")
                    continue
                break
            except ValueError:
                print("Error: Ingresa un número válido para la nota.")
        
        return nombre, nota

    def menu_acciones(self, tipo):
        if tipo == 'insertar':
            nombre, nota = self.datos_estudiante('INSERTAR')
            respuesta = Estudiante.insertar(nombre, nota)
            self.respuesta_sql(respuesta)
        
        elif tipo == 'consultar':
            self.borrarPantalla()
            print("--- CONSULTAR ESTUDIANTES ---")
            registros = Estudiante.consultar()
            if registros:
                for registro in registros:
                    print(f"ID: {registro[0]}, Nombre: {registro[1]}, Nota: {registro[2]}")
            else:
                print("No hay estudiantes registrados o conexión fallida.")
            self.esperarTecla()
        
        elif tipo == 'actualizar':
            self.borrarPantalla()
            id_act = input("ID del Estudiante a actualizar: ")
            nombre, nota = self.datos_estudiante('ACTUALIZAR')
            respuesta = Estudiante.actualizar(nombre, nota, id_act)
            self.respuesta_sql(respuesta)
        
        elif tipo == 'eliminar':
            self.borrarPantalla()
            id_del = input("ID del Estudiante a eliminar: ")
            respuesta = Estudiante.eliminar(id_del)
            self.respuesta_sql(respuesta)

    def respuesta_sql(self, respuesta):
        print("\n--- RESPUESTA DEL SISTEMA ---")
        print(respuesta)
        self.esperarTecla()

    def menu_estudiante(self):
        while True:
            self.borrarPantalla()
            print("--- MENÚ PRINCIPAL ---")
            print("1. Insertar Estudiante")
            print("2. Consultar Estudiantes")
            print("3. Actualizar Estudiante")
            print("4. Eliminar Estudiante")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                self.menu_acciones('insertar')
            elif opcion == '2':
                self.menu_acciones('consultar')
            elif opcion == '3':
                self.menu_acciones('actualizar')
            elif opcion == '4':
                self.menu_acciones('eliminar')
            elif opcion == '5':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def main(self):
        self.menu_estudiante()

if __name__ == "__main__":
    app = App()
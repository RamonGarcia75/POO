class Universidad:
    def __init__(self, nombre="UTD"):
        self._nombre = nombre 

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre or nuevo_nombre.strip() == "":
            print("ERROR: El nombre de la universidad no puede estar vacío.")
        else:
            self._nombre = nuevo_nombre.strip()

class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante:
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad  
        self.carrera = carrera          

    def mostrar_datos_completos(self):
        print("-" * 40)
        print("Datos del Estudiante (Objeto 'persona'):")
        print(f"Nombre del Estudiante: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Especialidad: {self.carrera.especialidad}")
        print(f"Universidad: {self.universidad.nombre}") 
        print("-" * 40)


mi_universidad = Universidad(nombre="Universidad Autónoma")

mi_carrera = Carrera("Medicina")

persona = Estudiante(
    nombre="Sofía López", 
    edad=20, 
    universidad=mi_universidad, 
    carrera=mi_carrera
)

print("\n--- DATOS INICIALES ---")
persona.mostrar_datos_completos()

print("\n--- CAMBIANDO NOMBRE DE UNIVERSIDAD ---")
mi_universidad.nombre = "Instituto Tecnológico Nacional"
print("¡Nombre de la Universidad cambiado con éxito!")

persona.mostrar_datos_completos()


print("\n--- PRUEBA DE VALIDACIÓN ---")
mi_universidad.nombre = "    " 
print(f"Nombre actual después del intento fallido: {mi_universidad.nombre}")
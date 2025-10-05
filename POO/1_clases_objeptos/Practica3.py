class Alumnos:
    def __init__(self, nombre, edad, matricula):
        self.__nombre = nombre
        self.edad = edad
        self.matricula = matricula
        self.curso_actual = "Ninguno"
    
    def inscribirse(self, curso_nombre):
        self.curso_actual = curso_nombre
        print(f"INSCRIPCION: {self.nombre} se inscribió en {self.curso_actual}.")
    
    def __str__(self):
        return f"[ALUMNO] Nombre: {self.nombre}, Matrícula: {self.matricula}, Curso: {self.curso_actual}"

class Profesores:
    def __init__(self, nombre, experiencia, num_profesor):
        self.nombre = nombre
        self.experiencia = experiencia
        self.num_profesor = num_profesor
        
    def impartir_y_evaluar(self, curso_nombre):
        print(f"ACCION PROF.: {self.nombre} está impartiendo y evaluando el curso de {curso_nombre}.")

    def __str__(self):
        return f"[PROFESOR] Nombre: {self.nombre}, Experiencia: {self.experiencia} años"

class Curso:
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.profesor_asignado = "Sin asignar"

    def asignar_profesor(self, profesor_nombre):
        self.profesor_asignado = profesor_nombre
        print(f"ASIGNACION: El curso {self.nombre} tiene asignado a {self.profesor_asignado}.")
        
    def __str__(self):
        return f"[CURSO] Nombre: {self.nombre} (Código: {self.codigo}), Profesor Asignado: {self.profesor_asignado}"

curso_matematicas = Curso("Matematicas", 220, 30)
prof_pedro = Profesores("Pedro", 70, 19875)
alumno_carlos = Alumnos("Carlos", 18, 103465)

curso_matematicas.asignar_profesor(prof_pedro.nombre)
alumno_carlos.inscribirse(curso_matematicas.nombre)
prof_pedro.impartir_y_evaluar(curso_matematicas.nombre)

print(curso_matematicas)
print(prof_pedro)
print(alumno_carlos)

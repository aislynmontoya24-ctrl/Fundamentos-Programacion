# -- coding: utf-8 --

class Alumno:
    # Constructor: inicializa los atributos del alumno
    def _init_(self, nombre: str, numero_control: str, carrera=None, email: str = None):
        # Nombre completo del alumno
        self.nombre = nombre
        # Número de control (identificador único)
        self.numero_control = numero_control
        # Carrera a la que pertenece (objeto de tipo Carrera)
        self.carrera = carrera
        # Diccionario para guardar las calificaciones del alumno {materia: calificación}
        self.calificaciones = {}
        # 🔹 Nuevo atributo: correo electrónico del alumno
        self.email = email

    # Asigna una carrera al alumno
    def asignar_carrera(self, carrera):
        self.carrera = carrera

    # Consulta la calificación de una materia específica
    def consulta_calificacion(self, nombre_materia: str):
        if nombre_materia in self.calificaciones:
            return self.calificaciones[nombre_materia]
        else:
            return f'No hay calificación registrada para "{nombre_materia}".'

    # Representación en texto del objeto Alumno
    def _repr_(self):
        return f'Alumno("{self.nombre}", "{self.numero_control}", email="{self.email}")'


class Universidad:
    def _init_(self, nombre: str):
        # Nombre de la universidad
        self.nombre = nombre
        # Lista de carreras que ofrece la universidad
        self.carreras = []
        # Lista de alumnos registrados
        self.alumnos = []
        # Lista de profesores asociados
        self.profesores = []

    # ------------------- Gestión de carreras -------------------
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def obtener_carrera(self, nombre_carrera: str):
        for c in self.carreras:
            if c.nombre == nombre_carrera:
                return c
        return None

    # ------------------- Otros registros -------------------
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)


class Carrera:
    def _init_(self, nombre: str):
        # Nombre de la carrera (por ejemplo: "Ingeniería")
        self.nombre = nombre
        # Lista de materias que pertenecen a la carrera
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_materia(self, nombre_materia: str):
        for m in self.materias:
            if m.nombre == nombre_materia:
                return m
        return None

    def _repr_(self):
        return f'Carrera("{self.nombre}")'


class Materia:
    def _init_(self, nombre: str, carrera: Carrera, calificacion_final: float = None):
        # Nombre de la materia (ejemplo: "Cálculo I")
        self.nombre = nombre
        # Carrera a la que pertenece esta materia
        self.carrera = carrera
        # Calificación final opcional
        self.calificacion_final = calificacion_final

    def _repr_(self):
        return f'Materia("{self.nombre}", carrera="{self.carrera.nombre}")'


class Profesor:
    def _init_(self, nombre: str, materia: Materia):
        # Nombre del profesor
        self.nombre = nombre
        # Materia que imparte (objeto Materia)
        self.materia = materia

    # Registra la calificación de un alumno en la materia que imparte
    def registra_calificacion(self, alumno: Alumno, calificacion: float):
        alumno.calificaciones[self.materia.nombre] = calificacion
        print(f'Calificación registrada: {alumno.nombre} -> '
              f'{self.materia.nombre}: {calificacion}')

    def _repr_(self):
        return f'Profesor("{self.nombre}", {self.materia})'


if _name_ == "_main_":

    uni = Universidad("Instituto")

    ing = Carrera("Ingeniería")
    lic = Carrera("Licenciatura en Ciencias Sociales")

    uni.agregar_carrera(ing)
    uni.agregar_carrera(lic)

    calc = Materia("Cálculo I", ing)
    fis = Materia("Física I", ing)
    sociologia = Materia("Introducción a la Sociología", lic)

    ing.agregar_materia(calc)
    ing.agregar_materia(fis)
    lic.agregar_materia(sociologia)

    # Se incluye el nuevo atributo email
    juan = Alumno("Juan Pérez", "2023001", email="juan.perez@instituto.edu")
    luisa = Alumno("Luisa Gómez", "2023002", email="luisa.gomez@instituto.edu")

    juan.asignar_carrera(ing)
    luisa.asignar_carrera(ing)

    uni.agregar_alumno(juan)
    uni.agregar_alumno(luisa)

    prof_garcia = Profesor("Dr. García", calc)
    prof_rodriguez = Profesor("Mtra. Rodríguez", fis)

    uni.agregar_profesor(prof_garcia)
    uni.agregar_profesor(prof_rodriguez)

    prof_garcia.registra_calificacion(juan, 8.5)
    prof_garcia.registra_calificacion(luisa, 9.0)
    prof_rodriguez.registra_calificacion(juan, 7.5)

    print(juan.consulta_calificacion("Cálculo I"))   
    print(juan.consulta_calificacion("Física I"))   
    print(luisa.consulta_calificacion("Cálculo I")) 
    print(luisa.consulta_calificacion("Física I"))  

    print("Materias de Ingeniería:", [m.nombre for m in ing.materias])
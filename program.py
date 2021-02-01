from peewee import *


def menu():
    print("*" * 20)
    print("- Menú Principal -")
    print("[1] - Alumnos")
    print("[2] - Cursos")
    print("[3] - AlumnosCursos")
    print("[0] - Salir")
    print("*" * 20)
    opc = int(input("Elige una opcion:\n"))
    return opc


def menuAlumnosCursos():
    print("*" * 20)
    print("- Menú Inscripciones -")
    print("[1] - Alta inscripcion")
    print("[2] - Baja")
    print("[3] - Modificar inscripcion")
    print("[4] - Buscar inscripcion")
    print("[5] - Mostrar inscripciones")
    print("[0] - Salir")
    print("*" * 20)
    opc = int(input("Elige una opcion:\n"))
    return opc


def menuAlumnos():
    print("*" * 20)
    print("- Menú Alumno -")
    print("[1] - Alta Alumno")
    print("[2] - Baja Alumno")
    print("[3] - Modificar Alumno")
    print("[4] - Buscar Alumno")
    print("[5] - Mostrar Alumnos")
    print("[0] - Salir")
    print("*" * 20)
    opc = int(input("Elige una opcion:\n"))
    return opc


def menuCurso():
    print("*" * 20)
    print("- Menú Curso -")
    print("[1] - Alta Curso")
    print("[2] - Baja Curso")
    print("[3] - Modificar Curso")
    print("[4] - Buscar Curso")
    print("[5] - Mostrar Cursos")
    print("[0] - Salir")
    print("*" * 20)
    opc = int(input("Elige una opcion:\n"))
    return opc


def continuar():
    print("*" * 20)
    print("Quieres continuar?")
    print("[1] - Seguir")
    print("[0] - Salir")
    print("*" * 20)
    opc = int(input("Elige una opcion:\n"))
    return opc


def altaAlumno():
    nombre = input("Introduce nombre\n")
    apellido = input("Introduce apellido\n")
    telefono = input("Introduce telefono\n")
    edad = int(input("Introduce edad\n"))
    alumno = Alumno(nombre=nombre, apellido=apellido, telefono=telefono, edad=edad)
    alumno.save()

    print("Quieres matricular al alumno en algun curso?\n")
    respuesta = input("Si/No")
    if respuesta == "Si" or respuesta == "si":
        altaAlumnoCurso(alumno.numeroExp)


def altaCurso():
    nomCurso = input("Introduce el nombre del curso\n")
    descripcion = input("Introduce la descripcion del curso\n")
    curso = Curso.create(nombre=nomCurso, descripcion=descripcion)
    curso.save()


def altaAlumnoCurso(exp):
    listaCursos = []
    for curso in Curso.select():
        print("**************************************")
        print("--Cursos Disponibles --")
        print("- Codigo:", curso.codigoCurso)
        print("- Nombre:", curso.nombre)
        print("- Descripcion:", curso.descripcion)
        print("**************************************")
        codigo = curso.codigoCurso
        listaCursos.append(codigo)

    if not listaCursos:
        print("No existen cursos, no puedes matricular al alumno\n")
    else:
        cod = int(input("Introduce el codigo del curso en el que quieres matricular al alumno"))
        for c in listaCursos:
            if cod == c:
                print("Curso encontrado")
                matriculado = AlumnoCurso.create(numExp=exp, codCurso=cod)
                matriculado.save()
            else:
                print("Curso no encontrado")


def bajaAlumno():
    pass


def bajaCurso():
    pass


def bajaAlumnoCurso():
    pass


def modificarAlumno():
    pass


def modificarCurso():
    pass


def modificarAlumnoCurso():
    pass


def buscarAlumno():
    pass


def buscarCurso():
    pass


def buscarAlumnoCurso():
    pass


def mostrarAlumno():
    pass


def mostrarCurso():
    pass


def mostrarAlumnoCurso():
    pass


db = MySQLDatabase('alumnoCurso', user='root', password='',
                   host='localhost', port=3306)


# Alumno
class Alumno(Model):
    numeroExp = PrimaryKeyField()
    nombre = CharField()
    apellido = CharField()
    telefono = CharField()
    edad = IntegerField()

    class Meta:
        database = db  # This model uses the "alumnosCursos.db" database.


# Curso
class Curso(Model):
    codigoCurso = PrimaryKeyField()
    nombre = CharField()
    descripcion = CharField()

    class Meta:
        database = db  # This model uses the "alumnosCursos.db" database.


# AlumnosCursos
class AlumnoCurso(Model):
    numExp = ForeignKeyField(Alumno, backref='alumno')
    codCurso = ForeignKeyField(Curso, backref='curso')

    class Meta:
        database = db  # This model uses the "alumnosCursos.db" database.


db.connect()
db.create_tables([Alumno, Curso, AlumnoCurso])
print("Empezamos")
salir = False

while not salir:
    opcion = menu()
    if opcion == 1:
        salirA = False
        while not salirA:
            opcionA = menuAlumnos()
            if opcionA == 1:
                altaAlumno()
            elif opcionA == 2:
                bajaAlumno()
            elif opcionA == 3:
                modificarAlumno()
            elif opcionA == 4:
                buscarAlumno()
            elif opcionA == 5:
                mostrarAlumno()
            elif opcionA == 0:
                salirA = True
            else:
                print("Elige un numero entre 0 y 5")
    elif opcion == 2:
        salirC = False
        while not salirC:
            opcionC = menuCurso()
            if opcionC == 1:
                altaCurso()
            elif opcionC == 2:
                bajaCurso()
            elif opcionC == 3:
                modificarCurso()
            elif opcionC == 4:
                buscarCurso()
            elif opcionC == 5:
                mostrarCurso()
            elif opcionC == 0:
                salirC = True
            else:
                print("Elige un numero entre 0 y 5")
    elif opcion == 3:
        salirAc = False
        while not salirAc:
            opcionAc = menuAlumnosCursos()
            if opcionAc == 1:
                altaAlumnoCurso()
            elif opcionAc == 2:
                bajaAlumnoCurso()
            elif opcionAc == 3:
                menuAlumnosCursos()
            elif opcionAc == 4:
                buscarAlumnoCurso()
            elif opcionAc == 5:
                mostrarAlumnoCurso()
            elif opcionAc == 0:
                salirAc = True
            else:
                print("Elige un numero entre 0 y 5")
    elif opcion == 0:
        print("SALIMOS")
        salir = True
        db.close()
    else:
        print("Introduce un numero entre 0 y 3")
print("FIN")

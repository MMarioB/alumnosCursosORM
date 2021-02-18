from peewee import *
import configparser
import pymysql


def menu():
    print("*" * 20)
    print("- Menú Principal -")
    print("[1] - Alumnos")
    print("[2] - Cursos")
    print("[3] - Inscripciones")
    print("[0] - Salir")
    print("*" * 20)
    opc = int(input("Elige una opcion:\n"))
    return opc


def menuAlumnosCursos():
    print("*" * 20)
    print("- Menú Inscripciones -")
    print("[1] - Baja inscripcion")
    print("[2] - Buscar inscripcion")
    print("[3] - Mostrar inscripciones")
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
    else:
        print("Salimos")


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
    print(listaCursos)
    salir = False
    while not salir:
        if not listaCursos:
            print("No existen cursos, no puedes matricular al alumno\n")
            break
        else:
            cod = int(input("Introduce el codigo del curso en el que quieres matricular al alumno"))
            for c in listaCursos:
                if cod == c:
                    print("Curso encontrado")
                    matriculado = AlumnoCurso.create(numExp=exp, codCurso=cod)
                    matriculado.save()
                    salir = True
                    break
                else:
                    print("Curso no encontrado. No ha sido posible matricular al alumno")


def bajaAlumno():
    mostrarAlumno()
    numexp = int(input("Introduce el numero de expediente del alumno que quieres borrar"))
    AlumnoCurso.delete().where(AlumnoCurso.numExp == numexp).execute()
    Alumno.delete().where(Alumno.numeroExp == numexp).execute()


def bajaCurso():
    mostrarCurso()
    codcur = int(input("Introduce el codigo del curso que quieres borrar"))
    AlumnoCurso.delete().where(AlumnoCurso.codCurso == codcur).execute()
    Curso.delete().where(Curso.codigoCurso == codcur).execute()


def bajaAlumnoCurso():
    mostrarAlumnoCurso()
    numexp = int(input("Introduce el numero de expediente del alumno que quieres borrar"))
    AlumnoCurso.delete().where(AlumnoCurso.numExp == numexp).execute()


def modificarAlumno():
    numexp = int(input("Introduce el numero de expediente del alumno que quieres modificar"))
    alumnomod = Alumno.select().where(Alumno.numeroExp == numexp).get()
    nombre_ = input("Introduce el nombre modificado")
    apellido_ = input("Introduce el apellido modificado")
    telefono_ = input("Introduce el telefono modificado")
    edad_ = input("Introduce la edad modificada")
    alumnomod.nombre = nombre_
    alumnomod.apellido = apellido_
    alumnomod.telefono = telefono_
    alumnomod.edad = edad_
    alumnomod.save()


def modificarCurso():
    codcur = int(input("Introduce el codigo del curso que quieres modificar"))
    cursomod = Curso.select().where(Curso.codigoCurso == codcur).get()
    nombre_ = input("Introduce el nombre modificado del curso")
    descripcion_ = input("Introduce la descripcion modificada del curso")
    cursomod.nombre = nombre_
    cursomod.descripcion = descripcion_
    cursomod.save()


def buscarAlumno():
    listaAlumnos = []
    for alumno in Alumno.select():
        codigo = alumno.numeroExp
        listaAlumnos.append(codigo)
    print("Expedientes:",listaAlumnos)
    numexp = int(input("Introduce el numero de expediente del alumno que quieres buscar"))
    if numexp not in listaAlumnos:
        print("No se ha encontrado ningun alumno con ese numero de expediente")
    else:
        alumnobus = Alumno.select().where(Alumno.numeroExp == numexp).get()
        print("**************************************")
        print("Expediente: " + str(alumnobus.numeroExp))
        print("Nombre: " + alumnobus.nombre)
        print("Apellido: " + alumnobus.apellido)
        print("Telefono: " + alumnobus.telefono)
        print("Edad: " + str(alumnobus.edad))
        print("**************************************")



def buscarCurso():
    pass


def buscarAlumnoCurso():
    pass


def mostrarAlumno():
    for alumno in Alumno.select():
        print("**************************************")
        print("-- Alumnos --")
        print("- Expediente:", alumno.numeroExp)
        print("- Nombre:", alumno.nombre)
        print("- Apellido:", alumno.apellido)
        print("- Telefono:", alumno.telefono)
        print("- Edad:", alumno.edad)
        print("**************************************")


def mostrarCurso():
    for curso in Curso.select():
        print("**************************************")
        print("--Cursos Disponibles --")
        print("- Codigo:", curso.codigoCurso)
        print("- Nombre:", curso.nombre)
        print("- Descripcion:", curso.descripcion)
        print("**************************************")


def mostrarAlumnoCurso():
    """
    SELECT * FROM alumno LEFT OUTER JOIN alumnocurso ON alumnocurso.numExp_id = alumno.numeroExp LEFT OUTER JOIN curso ON alumnocurso.codCurso_id = curso.codigoCurso
    """
    # Esto me saca los alumnos que estan matriculados
    query = (Alumno
             .select(AlumnoCurso.numExp, Alumno.nombre, Alumno.apellido, Curso.nombre)
             .join(AlumnoCurso)
             .join(Curso)
             .tuples()
             )
    for alumno in query:
        print(alumno)


# fichero configuracion
config = configparser.ConfigParser()
config.read('config.ini')

database_name = config['DEFAULT']['DB_NAME']
database_user = config['DEFAULT']['DB_USER']
database_host = config['DEFAULT']['DB_HOST']
database_port = config['DEFAULT']['DB_PORT']
database_password = config['DEFAULT']['DB_PASSWORD']

# creamos base de datos en phpmyadmin con pymysql
try:
    conexion = pymysql.connect(host=database_host,
                               user=database_user,
                               password=database_password)
    conexion.cursor().execute("CREATE DATABASE IF NOT EXISTS alumnoCurso;")
    print("Conexión correcta")

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

# conectamos con la base de datos a traves de peewee
db = MySQLDatabase(database_name, user=database_user, password=database_password,
                   host=database_host, port=int(database_port))


# Alumno
class Alumno(Model):
    numeroExp = AutoField()
    nombre = CharField()
    apellido = CharField()
    telefono = CharField()
    edad = IntegerField()

    class Meta:
        database = db  # This model uses the "alumnosCursos.db" database.


# Curso
class Curso(Model):
    codigoCurso = AutoField()
    nombre = CharField()
    descripcion = CharField()

    class Meta:
        database = db  # This model uses the "alumnosCursos.db" database.


# AlumnosCursos
class AlumnoCurso(Model):
    numExp = ForeignKeyField(Alumno)
    codCurso = ForeignKeyField(Curso)

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
                bajaAlumnoCurso()
            elif opcionAc == 2:
                buscarAlumnoCurso()
            elif opcionAc == 3:
                mostrarAlumnoCurso()
            elif opcionAc == 0:
                salirAc = True
            else:
                print("Elige un numero entre 0 y 3")
    elif opcion == 0:
        print("SALIMOS")
        salir = True
        db.close()
    else:
        print("Introduce un numero entre 0 y 3")
print("FIN")

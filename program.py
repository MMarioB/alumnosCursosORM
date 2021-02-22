from peewee import *
import configparser
import pymysql


def lee_entero():
    while True:
        entrada = input("->")
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("Error!! Has introducido algo que no es un numero")


def menu():
    print("*" * 20)
    print("- Menú Principal -")
    print("[1] - Alumnos")
    print("[2] - Cursos")
    print("[3] - Inscripciones")
    print("[0] - Salir")
    print("*" * 20)
    opc = lee_entero()
    return opc


def menuAlumnosCursos():
    print("*" * 20)
    print("- Menú Inscripciones -")
    print("[1] - Baja inscripcion")
    print("[2] - Buscar inscripcion")
    print("[3] - Mostrar inscripciones")
    print("[0] - Salir")
    print("*" * 20)
    opc = lee_entero()
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
    opc = lee_entero()
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
    opc = lee_entero()
    return opc


def continuar():
    print("*" * 20)
    print("Quieres continuar?")
    print("[1] - Seguir")
    print("[0] - Salir")
    print("*" * 20)
    opc = lee_entero()
    while True:
        if opc == 0:
            return opc
        elif opc == 1:
            return opc
        else:
            print("Opcion incorrecta")
            opc = lee_entero()


def validarEdad():
    while True:
        entrada = input("Introduce una edad\n ")
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("Error!! Has introducido algo que no es una edad")


def altaAlumno():
    nombre = input("Introduce el nombre\n")
    while True:
        if not nombre:
            print("Cadena vacia")
            nombre = input("Introduce el nombre\n")
        else:
            break
    apellido = input("Introduce el apellido\n")
    while True:
        if not apellido:
            print("Cadena vacia")
            apellido = input("Introduce el apellido\n")
        else:
            break
    telefono = input("Introduce el telefono\n")
    while True:
        if telefono.isdigit():
            break
        else:
            telefono = input("Introduce el telefono de nuevo\n")
    edad = validarEdad()
    alumno = Alumno(nombre=nombre, apellido=apellido, telefono=telefono, edad=edad)
    alumno.save()

    print("Quieres matricular al alumno en algun curso?\n")
    respuesta = input(
        "Introduce si para matricularlo. (cualquier cosa que sea distinta de si no matriculará al alumno)")
    if respuesta == "Si" or respuesta == "si":
        altaAlumnoCurso(alumno.numeroExp)
    else:
        print("Salimos")


def altaCurso():
    nomCurso = input("Introduce el nombre del curso\n")
    while True:
        if not nomCurso:
            print("Cadena vacia")
            nomCurso = input("Introduce el nombre del curso\n")
        else:
            break
    descripcion = input("Introduce la descripcion del curso\n")
    while True:
        if not descripcion:
            print("Cadena vacia")
            descripcion = input("Introduce la descripcion del curso\n")
        else:
            break
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
    if not listaCursos:
        print("No existen cursos, no puedes matricular al alumno\n")
    else:
        print("Introduce el codigo del curso en el que quieres matricular al alumno")
        cod = lee_entero()
        query = (Alumno
                 .select(AlumnoCurso.numExp, Alumno.nombre, Alumno.apellido, Curso.nombre)
                 .join(AlumnoCurso)
                 .join(Curso)
                 .where(AlumnoCurso.codCurso == cod and AlumnoCurso.numExp == exp)
                 .tuples()
                 )
        for alum in query:
            print(alum)
        if not query:
            print("NO DEBERIA ENTRAR AQUI")
            matriculado = AlumnoCurso.create(numExp=exp, codCurso=cod)
            matriculado.save()
        else:
            print("Ya esta matriculado en ese curso")
            # AlumnoCurso.delete().where(AlumnoCurso.numExp == exp and AlumnoCurso.codCurso == cod).execute()


def bajaAlumno():
    mostrarAlumno()
    listaAlumnos = []
    for alumno in Alumno.select():
        codigo = alumno.numeroExp
        listaAlumnos.append(codigo)
    print("Expedientes:", listaAlumnos)
    print("Introduce el numero de expediente del alumno que quieres borrar")
    numexp = lee_entero()
    if numexp not in listaAlumnos:
        print("No se ha encontrado ningun alumno con ese numero de expediente")
    else:
        print("Alumno dado de baja")
        AlumnoCurso.delete().where(AlumnoCurso.numExp == numexp).execute()
        Alumno.delete().where(Alumno.numeroExp == numexp).execute()


def bajaCurso():
    mostrarCurso()
    listaCursos = []
    for curso in Curso.select():
        codigo = curso.codigoCurso
        listaCursos.append(codigo)
    print("Codigos:", listaCursos)
    print("Introduce el numero de expediente del alumno que quieres buscar")
    codcur = lee_entero()
    if codcur not in listaCursos:
        print("No se ha encontrado ningun alumno con ese numero de expediente")
    else:
        AlumnoCurso.delete().where(AlumnoCurso.codCurso == codcur).execute()
        Curso.delete().where(Curso.codigoCurso == codcur).execute()


def bajaAlumnoCurso():
    mostrarAlumnoCurso()
    listaAlumnos = []
    for alumno in Alumno.select():
        codigo = alumno.numeroExp
        listaAlumnos.append(codigo)
    print("Expedientes:", listaAlumnos)
    print("Introduce el numero de expediente del alumno que quieres borrar")
    numexp = lee_entero()
    if numexp not in listaAlumnos:
        print("No se ha encontrado ningun alumno con ese numero de expediente")
    else:
        AlumnoCurso.delete().where(AlumnoCurso.numExp == numexp).execute()


def modificarAlumno():
    listaAlumnos = []
    for alumno in Alumno.select():
        codigo = alumno.numeroExp
        listaAlumnos.append(codigo)
    print("Expedientes:", listaAlumnos)
    print("Introduce el numero de expediente del alumno que quieres buscar")
    numexp = lee_entero()
    if numexp not in listaAlumnos:
        print("No se ha encontrado ningun alumno con ese numero de expediente")
    else:
        print("Quieres matricular al alumno en algun curso, o quieres modificar sus datos?\n")
        respuesta = input(
            "Introduce si para matricularlo. (cualquier cosa que sea distinta de si no matriculará al alumno)")
        if respuesta == "Si" or respuesta == "si":
            altaAlumnoCurso(numexp)
        else:
            alumnomod = Alumno.select().where(Alumno.numeroExp == numexp).get()
            nombre_ = input("Introduce el nombre\n")
            while True:
                if not nombre_:
                    print("Cadena vacia")
                    nombre_ = input("Introduce el nombre\n")
                else:
                    break
            apellido_ = input("Introduce el apellido\n")
            while True:
                if not apellido_:
                    print("Cadena vacia")
                    apellido_ = input("Introduce el apellido\n")
                else:
                    break
            telefono_ = input("Introduce el telefono\n")
            while True:
                if telefono_.isdigit():
                    break
                else:
                    telefono_ = input("Introduce el telefono de nuevo\n")
            edad_ = validarEdad()
            alumnomod.nombre = nombre_
            alumnomod.apellido = apellido_
            alumnomod.telefono = telefono_
            alumnomod.edad = edad_
            alumnomod.save()


def modificarCurso():
    listaCursos = []
    for curso in Curso.select():
        codigo = curso.codigoCurso
        listaCursos.append(codigo)
    print("Expedientes:", listaCursos)
    print("Introduce el codigo del curso que quieres modificar")
    codcur = lee_entero()
    if codcur not in listaCursos:
        print("No se ha encontrado ningun curso con ese codigo")
    else:
        cursomod = Curso.select().where(Curso.codigoCurso == codcur).get()
        nombre_ = input("Introduce el nombre del curso\n")
        while True:
            if not nombre_:
                print("Cadena vacia")
                nombre_ = input("Introduce el nombre del curso\n")
            else:
                break
        descripcion_ = input("Introduce la descripcion del curso\n")
        while True:
            if not descripcion_:
                print("Cadena vacia")
                descripcion_ = input("Introduce la descripcion del curso\n")
            else:
                break
        cursomod.nombre = nombre_
        cursomod.descripcion = descripcion_
        cursomod.save()


def buscarAlumno():
    listaAlumnos = []
    for alumno in Alumno.select():
        codigo = alumno.numeroExp
        listaAlumnos.append(codigo)
    print("Expedientes:", listaAlumnos)
    print("Introduce el numero de expediente del alumno que quieres buscar")
    numexp = lee_entero()
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
    listaCursos = []
    for curso in Curso.select():
        codigo = curso.codigoCurso
        listaCursos.append(codigo)
    print("Expedientes:", listaCursos)
    print("Introduce el codigo del curso que quieres buscar")
    codcur = lee_entero()
    if codcur not in listaCursos:
        print("No se ha encontrado ningun curso con ese codigo")
    else:
        codigobus = Curso.select().where(Curso.codigoCurso == codcur).get()
        print("**************************************")
        print("Codigo: " + str(codigobus.codigoCurso))
        print("Nombre: " + codigobus.nombre)
        print("Descripcion: " + codigobus.descripcion)
        print("**************************************")


def buscarAlumnoCurso():
    listaAlumnos = []
    for alumno in Alumno.select():
        codigo = alumno.numeroExp
        listaAlumnos.append(codigo)
    print("Expedientes:", listaAlumnos)
    print("Introduce el numero de expediente del alumno que quieres buscar")
    numexp = lee_entero()
    if numexp not in listaAlumnos:
        print("No se ha encontrado ningun alumno con ese numero de expediente")
    else:
        query = (Alumno
                 .select(AlumnoCurso.numExp, Alumno.nombre, Alumno.apellido, Curso.nombre)
                 .join(AlumnoCurso)
                 .join(Curso)
                 .where(Alumno.numeroExp == numexp)
                 .tuples()
                 )
        for alumno in query:
            print(alumno)


def mostrarAlumno():
    for alumno in Alumno.select():
        print("**************************************")
        print("-- Alumnos --")
        print("- Expediente:", alumno.numeroExp)
        print("- Nombre:", alumno.nombre)
        print("- Apellido:", alumno.apellido)
        print("- Telefono:", alumno.telefono)
        print("- Edad:", alumno.edad)
        print("- Cursos:")
        codigoal = alumno.numeroExp
        query = (Alumno
                 .select(AlumnoCurso.numExp, Alumno.nombre, Alumno.apellido, Curso.nombre)
                 .join(AlumnoCurso)
                 .join(Curso)
                 .where(Alumno.numeroExp == codigoal)
                 .tuples()
                 )
        if not query:
            print("  - " + "No esta matriculado en ningun curso")
        else:
            for al in query:
                print("  - " + al[3])
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
    for curso in Curso.select():
        print("**************************************")
        print("--Cursos Disponibles --")
        print("- Codigo:", curso.codigoCurso)
        print("- Nombre:", curso.nombre)
        print("- Descripcion:", curso.descripcion)
        print("- Alumnos Matriculados:")
        cursomostrar = curso.nombre
        query = (Alumno
                 .select(AlumnoCurso.numExp, Alumno.nombre, Alumno.apellido, Curso.nombre)
                 .join(AlumnoCurso)
                 .join(Curso)
                 .where(Curso.nombre == cursomostrar)
                 .tuples()
                 )
        if not query:
            print("  - " + "No tiene alumnos matriculados")
        else:
            for alumno in query:
                print("  - " + alumno[1], alumno[2])
        print("**************************************")


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
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
                        altaAlumno()
            elif opcionA == 2:
                bajaAlumno()
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
                        bajaAlumno()
            elif opcionA == 3:
                modificarAlumno()
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
                        modificarAlumno()
            elif opcionA == 4:
                buscarAlumno()
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
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
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
                        altaCurso()
            elif opcionC == 2:
                bajaCurso()
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
                        bajaCurso()
            elif opcionC == 3:
                modificarCurso()
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
                        modificarCurso()
            elif opcionC == 4:
                buscarCurso()
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
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
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
                        bajaAlumnoCurso()
            elif opcionAc == 2:
                buscarAlumnoCurso()
                while True:
                    op1 = continuar()
                    if op1 == 0:
                        break
                    else:
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

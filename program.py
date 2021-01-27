from peewee import *

db = SqliteDatabase('alumnosCursos.db')


# Alumno
class Alumno(Model):
    numeroExp = IntegerField()
    nombre = CharField()
    apellido = CharField()
    telefono = CharField()
    edad = IntegerField()

    class Meta:
        database = db  # This model uses the "alumnosCursos.db" database.


# Curso
class Curso(Model):
    codigoCurso = IntegerField()
    nombre = CharField()
    descripcion = CharField()

    class Meta:
        database = db  # This model uses the "alumnosCursos.db" database.


# AlumnosCursos
class AlumnoCurso(Model):
    numExp = ForeignKeyField(Alumno, backref='curso')
    codCurso = ForeignKeyField(Curso, backref='alumno')

    class Meta:
        database = db  # This model uses the "alumnosCursos.db" database.


db.connect()
db.create_tables([Alumno, Curso, AlumnoCurso])

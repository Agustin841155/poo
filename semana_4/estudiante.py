class Estudiante:
  #Atributos 
  nombre= "agustin"
  matricula= "1719110184"
  carrera= "tic´s"
  edad= "18"
  cuatrimestre= "segundo"

  #Metodos
  def elegir(self):
    print("elegir")
  def asignar(self):
    print("asignar")

  def __init__(self):
    print:("metodos estudiante")

class EstudianteAgustin (Estudiante):
  #Atributos
  promedio=("9.6")
  beca="ninguna"
  tutor="oscar"
  grupo="21"
  nivel_de_ingles="A2"

  #Metodos
  def elegir(self):
    print("elegir una carrera")
  def asignar(self):
    print("se le asigna un grupo segun su carrera")

  def __init__(self):
    print("Estudiante agustin")

OBJETO=Estudiante()
OBJETO.elegir()
OBJETO.asignar()
print(OBJETO.nombre)
print(OBJETO.matricula)
print(OBJETO.carrera)
print(OBJETO.edad)
print(OBJETO.cuatrimestre)

OBJETO_ESTUDIANTE_AGUSTIN=EstudianteAgustin()
OBJETO_ESTUDIANTE_AGUSTIN.elegir()
OBJETO_ESTUDIANTE_AGUSTIN.asignar()
print(OBJETO_ESTUDIANTE_AGUSTIN.nombre)
print(OBJETO_ESTUDIANTE_AGUSTIN.matricula)
print(OBJETO_ESTUDIANTE_AGUSTIN.carrera)
print(OBJETO_ESTUDIANTE_AGUSTIN.edad)
print(OBJETO_ESTUDIANTE_AGUSTIN.cuatrimestre)
print(OBJETO_ESTUDIANTE_AGUSTIN.promedio)
print(OBJETO_ESTUDIANTE_AGUSTIN.beca)
print(OBJETO_ESTUDIANTE_AGUSTIN.tutor)
print(OBJETO_ESTUDIANTE_AGUSTIN.grupo)
print(OBJETO_ESTUDIANTE_AGUSTIN.nivel_de_ingles)
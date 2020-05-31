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

class Estudianteagustin (Estudiante):
  #Atributos
  promedio=("9.6")
  beca="ninguna"
  tutor="oscar"
  grupo="21"
  nivel_de_ingles="A2"

  #Metodos
  def tareas(self):
    print("tareas")
  def pasar(self):
    print("pasar")

  def __init__(self):
    print("Estudiante agustin")

objeto=Estudiante()
objeto.elegir()
objeto.asignar()
print(objeto.nombre)
print(objeto.matricula)
print(objeto.carrera)
print(objeto.edad)
print(objeto.cuatrimestre)

objeto_estudiante_agustin=Estudianteagustin()
objeto_estudiante_agustin.tareas()
objeto_estudiante_agustin.pasar()
objeto_estudiante_agustin.elegir()
objeto_estudiante_agustin.asignar()
print(objeto_estudiante_agustin.nombre)
print(objeto_estudiante_agustin.matricula)
print(objeto_estudiante_agustin.carrera)
print(objeto_estudiante_agustin.edad)
print(objeto_estudiante_agustin.cuatrimestre)
print(objeto_estudiante_agustin.promedio)
print(objeto_estudiante_agustin.beca)
print(objeto_estudiante_agustin.tutor)
print(objeto_estudiante_agustin.grupo)
print(objeto_estudiante_agustin.nivel_de_ingles)

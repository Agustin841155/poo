class Estudiante:
  #ATRIBUTOS
  Metas_definidas="tiene un objetivo"
  Autodiciplina="se sabe comportar"
  Creativo="aporta ideas"
  Disposicion="solo estudia"
  Responsabilidad="cumple con todo lo solicitado"
  interactivo="participa en clase"
  Sociable="hace amigos facilmente"
  Motivacion="alguien o algo lo motiva"
  intelectualidad="es inteligente"
  Solidaridad="ayuda a sus compañeros"

  #METODOS
  def proyectos(self):
    print("proyectos")
  def tareas(self):
    print("tareas")
  def organizacion(self):
    print("organizacion")
  def tiene_un_horario(self):
    print("tiene un horario")
  def realiza_examenes(self):
    print("realiza examenes")
  
  def __init__(self):
    print("metodos estudiante")


objeto_un_estudiante = Estudiante()

objeto_un_estudiante.proyectos()
objeto_un_estudiante.tareas()
objeto_un_estudiante.organizacion()
objeto_un_estudiante.tiene_un_horario()
objeto_un_estudiante.realiza_examenes()

print(objeto_un_estudiante.Metas_definidas)
print(objeto_un_estudiante.Autodiciplina)
print(objeto_un_estudiante.Creativo)
print(objeto_un_estudiante.Disposicion)
print(objeto_un_estudiante.Responsabilidad)
print(objeto_un_estudiante.interactivo)
print(objeto_un_estudiante.Sociable)
print(objeto_un_estudiante.Motivacion)
print(objeto_un_estudiante.intelectualidad)
print(objeto_un_estudiante.Solidaridad)
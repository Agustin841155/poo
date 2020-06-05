class GoogleClassroom:
  #Atributos 
  plataforma_gratuita="completamente"
  buena_organizacion="tiene buena organizacion"
  es_de_la_empresa_google="completamente"
  logotipo="pizarron y siluetas de personas"
  disponibilidad_para_distintos_dispositivos="para la mayoria de dispositivos"

  #Metodos
  def dejarTarea(self):
    print("dejar tarea")
  def comunicacionDistancia(self):
    print("comunicacion a distancia")

  def __init__(self):
    print:("metodos google classroom")

class GoogleClassroomUtec (GoogleClassroom):
  #Atributos
  facil_de_usar="facil de usar"
  almacena_informacion="en drive almacena informacion"
  multiplataforma="multiplataforma"
  proporciona_un_codigo_para_las_clases="si para mayor organizacion"
  ensenar="si mediante varios medios"

  #Metodos
  def clasesOnline(self):
    print("clases online")
  def entregarTrabajosyTareas(self):
    print("entregar trabajos y tareas")
  def dejarTarea(self):
    print("dejar tarea de acuerdo a las materias")
  def comunicacionDistancia(self):
    print("comunicacion a distancia con los maestros de la utec")

  def __init__(self):
    print("Google Classroom UTEC")

OBJETO=GoogleClassroom()
OBJETO.dejarTarea()
OBJETO.comunicacionDistancia()
print(OBJETO.plataforma_gratuita)
print(OBJETO.buena_organizacion)
print(OBJETO.es_de_la_empresa_google)
print(OBJETO.logotipo)
print(OBJETO.disponibilidad_para_distintos_dispositivos)

OBJETO_UNA_APP = GoogleClassroomUtec()
OBJETO_UNA_APP.dejarTarea()
OBJETO_UNA_APP.comunicacionDistancia()
OBJETO_UNA_APP.clasesOnline()
OBJETO_UNA_APP.entregarTrabajosyTareas()
print(OBJETO_UNA_APP.plataforma_gratuita)
print(OBJETO_UNA_APP.buena_organizacion)
print(OBJETO_UNA_APP.es_de_la_empresa_google)
print(OBJETO_UNA_APP.logotipo)
print(OBJETO_UNA_APP.disponibilidad_para_distintos_dispositivos)
print(OBJETO_UNA_APP.facil_de_usar)
print(OBJETO_UNA_APP.almacena_informacion)
print(OBJETO_UNA_APP.multiplataforma)
print(OBJETO_UNA_APP.proporciona_un_codigo_para_las_clases)
print(OBJETO_UNA_APP.ensenar)
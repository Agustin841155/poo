class googleclassroom:
  #Atributos 
  Plataforma_gratuita="completamente"
  Buena_organizacion="tiene buena organizacion"
  Es_de_la_empresa_google="completamente"
  logotipo="pizarron y siluetas de personas"
  Disponibilidad_para_distintos_dispositivos="para la mayoria de dispositivos"

  #Metodos
  def dejar_tarea(self):
    print("dejar tarea")
  def comunicacion_a_distancia(self):
    print("comunicacion a distancia")

  def __init__(self):
    print:("metodos google classroom")

class googleclassroomutec (googleclassroom):
  #Atributos
  Facil_de_usar="facil de usar"
  Almacena_informacion="en drive almacena informacion"
  Multiplataforma="multiplataforma"
  Proporciona_un_codigo_para_las_clases="si para mayor organizacion"
  Ensenar="si mediante varios medios"

  #Metodos
  def clases_online(self):
    print("clases online")
  def entregar_trabajos_y_tareas(self):
    print("entregar trabajos y tareas")

  def __init__(self):
    print("Estudiante agustin")

objeto=googleclassroom()
objeto.dejar_tarea()
objeto.comunicacion_a_distancia()
print(objeto.Plataforma_gratuita)
print(objeto.Buena_organizacion)
print(objeto.Es_de_la_empresa_google)
print(objeto.logotipo)
print(objeto.Disponibilidad_para_distintos_dispositivos)

objeto_una_app = googleclassroomutec()
objeto_una_app.dejar_tarea()
objeto_una_app.comunicacion_a_distancia()
objeto_una_app.clases_online()
objeto_una_app.entregar_trabajos_y_tareas()
print(objeto_una_app.Plataforma_gratuita)
print(objeto_una_app.Buena_organizacion)
print(objeto_una_app.Es_de_la_empresa_google)
print(objeto_una_app.logotipo)
print(objeto_una_app.Disponibilidad_para_distintos_dispositivos)
print(objeto_una_app.Facil_de_usar)
print(objeto_una_app.Almacena_informacion)
print(objeto_una_app.Multiplataforma)
print(objeto_una_app.Proporciona_un_codigo_para_las_clases)
print(objeto_una_app.Ensenar)
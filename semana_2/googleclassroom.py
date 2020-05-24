class Google_classroom:
  #ATRIBUTOS
  Plataforma_gratuita="completamente"
  Buena_organizacion="si"
  Es_de_la_empresa_google="completamente"
  logotipo="pizarron y siluetas de personas"
  Disponibilidad_para_distintos_dispositivos="para la mayoria de dispositivos"
  Facil_de_usar="si"
  Almacena_informacion="si en drive"
  Multiplataforma="si"
  Proporciona_un_codigo_para_las_clases="si para mayor organizacion"
  Ensenar="si mediante varios medios"

  #METODOS
  def dejar_tarea(self):
    print("dejar tarea")
  def comunicacion_a_distancia(self):
    print("comunicacion a distancia")
  def clases_online(self):
    print("clases online")
  def entregar_trabajos_y_tareas(self):
    print("entregar trabajos y tareas")
  def crear_documentos(self):
    print("crear documentos")
  
  def __init__(self):
    print("metodos Google_classroom")


objeto_una_app = Google_classroom()

objeto_una_app.dejar_tarea()
objeto_una_app.comunicacion_a_distancia()
objeto_una_app.clases_online()
objeto_una_app.entregar_trabajos_y_tareas()
objeto_una_app.crear_documentos()

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
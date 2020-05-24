class vacaciones:
  #ATRIBUTOS
  irrenunciable="es un derecho en el trabajo"
  Duracion="depende el viaje"
  Viajar_o_realizar_un_recorrido="ir a un lugar"
  Realizar_gastos="pagar por la actividad"
  Descansar_de_una_actividad_habitual="no trabajar durante ese periodo"
  Esta_relacionado_con_el_turismo="si se visitan lugares turisticos"
  Uso_de_maletas="para guardar el equipaje"
  Fechas_establecidas="periodo de duracion"
  Conocimiento_de_diversidad="adquirir experiencia"
  Salir_de_casa="salir a cualquier lugar"


  #METODOS
  def distraccion(self):
    print("distraccion")
  def diversion(self):
    print("diversion")
  def entretenimiento(self):
    print("entretenimiento")
  def comprar_recuerdos(self):
    print("comprar recuerdos")
  def tomar_fotografias(self):
    print("tomar fotografis")
  
  def __init__(self):
    print("metodos vacaciones")


objeto_unas_vacaciones = vacaciones()

objeto_unas_vacaciones.distraccion()
objeto_unas_vacaciones.diversion()
objeto_unas_vacaciones.entretenimiento()
objeto_unas_vacaciones.comprar_recuerdos()
objeto_unas_vacaciones.tomar_fotografias()

print(objeto_unas_vacaciones.irrenunciable)
print(objeto_unas_vacaciones.Duracion)
print(objeto_unas_vacaciones.Viajar_o_realizar_un_recorrido)
print(objeto_unas_vacaciones.Realizar_gastos)
print(objeto_unas_vacaciones.Descansar_de_una_actividad_habitual)
print(objeto_unas_vacaciones.Esta_relacionado_con_el_turismo)
print(objeto_unas_vacaciones.Uso_de_maletas)
print(objeto_unas_vacaciones.Fechas_establecidas)
print(objeto_unas_vacaciones.Conocimiento_de_diversidad)
print(objeto_unas_vacaciones.Salir_de_casa)
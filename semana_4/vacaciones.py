class Vacaciones:
  #Atributos 
  irrenunciable="es un derecho en el trabajo"
  duracion="depende el viaje"
  viajar_o_realizar_un_recorrido="ir a un lugar"
  realizar_gastos="pagar por la actividad"
  descansar_de_una_actividad_habitual="no trabajar durante ese periodo"

  #Metodos
  def distraccion(self):
    print("distraccion")
  def diversion(self):
    print("diversion")

  def __init__(self):
    print:("metodos vacaciones")

class VacacionesCancun (Vacaciones):
  #Atributos
  esta_relacionado_con_el_turismo="si se visitan lugares turisticos"
  uso_de_maletas="para guardar el equipaje"
  fechas_establecidas="periodo de duracion"
  conocimiento_de_diversidad="adquirir experiencia"
  salir_de_casa="salir a cualquier lugar"

  #Metodos
  def entretenimiento(self):
    print("entretenimiento")
  def comprarRecuerdos(self):
    print("comprar recuerdos")
  def distraccion(self):
    print("distraccion de la rutina o del trabajo")
  def diversion(self):
    print("diversion familiar o de cualquier tipo")

  def __init__(self):
    print("vacaciones cancun")

OBJETO=Vacaciones()
OBJETO.distraccion()
OBJETO.diversion()
print(OBJETO.irrenunciable)
print(OBJETO.duracion)
print(OBJETO.viajar_o_realizar_un_recorrido)
print(OBJETO.realizar_gastos)
print(OBJETO.descansar_de_una_actividad_habitual)

OBJETO_UNAS_VACACIONES = VacacionesCancun()
OBJETO_UNAS_VACACIONES.distraccion()
OBJETO_UNAS_VACACIONES.diversion()
OBJETO_UNAS_VACACIONES.entretenimiento()
OBJETO_UNAS_VACACIONES.comprarRecuerdos()
print(OBJETO_UNAS_VACACIONES.irrenunciable)
print(OBJETO_UNAS_VACACIONES.duracion)
print(OBJETO_UNAS_VACACIONES.viajar_o_realizar_un_recorrido)
print(OBJETO_UNAS_VACACIONES.realizar_gastos)
print(OBJETO_UNAS_VACACIONES.descansar_de_una_actividad_habitual)
print(OBJETO_UNAS_VACACIONES.esta_relacionado_con_el_turismo)
print(OBJETO_UNAS_VACACIONES.uso_de_maletas)
print(OBJETO_UNAS_VACACIONES.fechas_establecidas)
print(OBJETO_UNAS_VACACIONES.conocimiento_de_diversidad)
print(OBJETO_UNAS_VACACIONES.salir_de_casa)
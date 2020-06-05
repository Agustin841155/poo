class Futbolista:
  #Atributos 
  usa_uniforme="depende el equipo"
  juega_en_una_chancha_de_futbol="los partidos"
  velocidad="con la que corre"
  fuerza="con la que golpea el balon"
  agilidad="para jugar"

  #Metodos
  def funcionPosicion(self):
    print("funcion o posicion")
  def juegaDeporteEspecifico(self):
    print("juega un deporte especifico")

  def __init__(self):
    print:("metodos Futbolista")

class FutbolistaMexicano (Futbolista):
  #Atributos
  motivacion="alguna persona u objetivo"
  flexibilidad="para realizar jugadas"
  coordinacion="al jugar"
  calzado_especial="tacos"
  diciplina="saberse comportar dentro de la cancha"

  #Metodos
  def dominarOponente(self):
    print("domina al oponente")
  def habilidad(self):
    print("habilidad")
  def funcionPosicion(self):
    print("delantero o medio")
  def juegaDeporteEspecifico(self):
    print("juega futbol")

  def __init__(self):
    print("Futbolista mexicano")

OBJETO=Futbolista()
OBJETO.funcionPosicion()
OBJETO.juegaDeporteEspecifico()
print(OBJETO.usa_uniforme)
print(OBJETO.juega_en_una_chancha_de_futbol)
print(OBJETO.velocidad)
print(OBJETO.fuerza)
print(OBJETO.agilidad)

OBJETO_UN_FUTBOLISTA = FutbolistaMexicano()
OBJETO_UN_FUTBOLISTA.funcionPosicion()
OBJETO_UN_FUTBOLISTA.juegaDeporteEspecifico()
OBJETO_UN_FUTBOLISTA.dominarOponente()
OBJETO_UN_FUTBOLISTA.habilidad()
print(OBJETO_UN_FUTBOLISTA.usa_uniforme)
print(OBJETO_UN_FUTBOLISTA.juega_en_una_chancha_de_futbol)
print(OBJETO_UN_FUTBOLISTA.velocidad)
print(OBJETO_UN_FUTBOLISTA.fuerza)
print(OBJETO_UN_FUTBOLISTA.agilidad)
print(OBJETO_UN_FUTBOLISTA.motivacion)
print(OBJETO_UN_FUTBOLISTA.flexibilidad)
print(OBJETO_UN_FUTBOLISTA.coordinacion)
print(OBJETO_UN_FUTBOLISTA.calzado_especial)
print(OBJETO_UN_FUTBOLISTA.diciplina)
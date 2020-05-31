class Futbolista:
  #Atributos 
  usa_uniforme="depende el equipo"
  juega_en_una_chancha_de_futbol="los partidos"
  velocidad="con la que corre"
  Fuerza="con la que golpea el balon"
  agilidad="para jugar"

  #Metodos
  def funcion_o_posicion(self):
    print("funcion o posicion")
  def juega_un_deporte_especifico(self):
    print("juega un deporte especifico")

  def __init__(self):
    print:("metodos Futbolista")

class Futbolistamexicano (Futbolista):
  #Atributos
  Motivacion="alguna persona u objetivo"
  Flexibilidad="para realizar jugadas"
  coordinacion="al jugar"
  Calzado_especial="tacos"
  Diciplina="saberse comportar dentro de la cancha"

  #Metodos
  def dominar_el_oponente(self):
    print("domina al oponente")
  def habilidad(self):
    print("habilidad")

  def __init__(self):
    print("Futbolista mexicano")

objeto=Futbolista()
objeto.funcion_o_posicion()
objeto.juega_un_deporte_especifico()
print(objeto.usa_uniforme)
print(objeto.juega_en_una_chancha_de_futbol)
print(objeto.velocidad)
print(objeto.Fuerza)
print(objeto.agilidad)

objeto_un_futbolista = Futbolistamexicano()
objeto_un_futbolista.funcion_o_posicion()
objeto_un_futbolista.juega_un_deporte_especifico()
objeto_un_futbolista.dominar_el_oponente()
objeto_un_futbolista.habilidad()
print(objeto_un_futbolista.usa_uniforme)
print(objeto_un_futbolista.juega_en_una_chancha_de_futbol)
print(objeto_un_futbolista.velocidad)
print(objeto_un_futbolista.Fuerza)
print(objeto_un_futbolista.agilidad)
print(objeto_un_futbolista.Motivacion)
print(objeto_un_futbolista.Flexibilidad)
print(objeto_un_futbolista.coordinacion)
print(objeto_un_futbolista.Calzado_especial)
print(objeto_un_futbolista.Diciplina)
class serieTV:
  #ATRIBUTOS
  Es_transmitida_en_dispositivos_tecnologicos="telefonos,smart´s tv,tablets"
  Es_dirigida_a_un_publico_especifico="segun el tipo de serie"
  Tiene_una_duracion="temporadas"
  Es_una_obra_audiovisual="es autentica"
  Tiene_episodios="depende el numero de temporadas"
  Tiene_una_Tematica="zombies,amor."
  Horario_de_transmision="depende la plataforma"
  Cuenta_con_un_presupuesto="se invirtio dinero para realizarla"
  Tiene_un_objetivo="intenta transmitir un mensaje"
  calidad="hd"

  #METODOS
  def entretenimiento(self):
    print("entretenimiento")
  def enrriquecimiento_de_conocimientos(self):
    print("enrriquecimiento de conocimientos")
  def distraccion(self):
    print("distraccion")
  def diversion(self):
    print("diversion")
  def desata_emociones(self):
    print("desata emociones")
  
  def __init__(self):
    print("metodos serieTV")


objeto_una_serie = serieTV()

objeto_una_serie.entretenimiento()
objeto_una_serie.enrriquecimiento_de_conocimientos()
objeto_una_serie.distraccion()
objeto_una_serie.diversion()
objeto_una_serie.desata_emociones()

print(objeto_una_serie.Es_transmitida_en_dispositivos_tecnologicos)
print(objeto_una_serie.Es_dirigida_a_un_publico_especifico)
print(objeto_una_serie.Tiene_una_duracion)
print(objeto_una_serie.Es_una_obra_audiovisual)
print(objeto_una_serie.Tiene_episodios)
print(objeto_una_serie.Tiene_una_Tematica)
print(objeto_una_serie.Horario_de_transmision)
print(objeto_una_serie.Cuenta_con_un_presupuesto)
print(objeto_una_serie.Tiene_un_objetivo)
print(objeto_una_serie.calidad)
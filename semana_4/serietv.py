class SerieTV:
  #Atributos 
  es_transmitida_en_dispositivos_tecnologicos="telefonos,smart´s tv,tablets"
  es_dirigida_a_un_publico_especifico="segun el tipo de serie"
  tiene_una_duracion="temporadas"
  es_una_obra_audiovisual="es autentica"
  tiene_episodios="depende el numero de temporadas"

  #Metodos
  def entretenimiento(self):
    print("entretenimiento")
  def enrriquecimientoConocimientos(self):
    print("enrriquecimiento de conocimientos")

  def __init__(self):
    print:("metodos serieTV")

class SerietvNetflix(SerieTV):
  #Atributos
  tiene_una_Tematica="zombies,amor."
  horario_de_transmision="depende la plataforma"
  cuenta_con_un_presupuesto="se invirtio dinero para realizarla"
  tiene_un_objetivo="intenta transmitir un mensaje"
  calidad="hd"

  #Metodos
  def diversion(self):
    print("diversion")
  def desataEmociones(self):
    print("desata emociones")
  def entretenimiento(self):
    print("entretenimiento para quien cuenta con el servicio")
  def enrriquecimientoConocimientos(self):
    print("enrriquecimiento de conocimientos segun la categoria vista")

  def __init__(self):
    print("serie de netflix")

OBJETO=SerieTV()
OBJETO.entretenimiento()
OBJETO.enrriquecimientoConocimientos()
print(OBJETO.es_transmitida_en_dispositivos_tecnologicos)
print(OBJETO.es_dirigida_a_un_publico_especifico)
print(OBJETO.tiene_una_duracion)
print(OBJETO.es_una_obra_audiovisual)
print(OBJETO.tiene_episodios)

OBJETO_UNA_SERIE = SerietvNetflix()
OBJETO_UNA_SERIE.entretenimiento()
OBJETO_UNA_SERIE.enrriquecimientoConocimientos()
OBJETO_UNA_SERIE.diversion()
OBJETO_UNA_SERIE.desataEmociones()
print(OBJETO_UNA_SERIE.es_transmitida_en_dispositivos_tecnologicos)
print(OBJETO_UNA_SERIE.es_dirigida_a_un_publico_especifico)
print(OBJETO_UNA_SERIE.tiene_una_duracion)
print(OBJETO_UNA_SERIE.es_una_obra_audiovisual)
print(OBJETO_UNA_SERIE.tiene_episodios)
print(OBJETO_UNA_SERIE.tiene_una_Tematica)
print(OBJETO_UNA_SERIE.horario_de_transmision)
print(OBJETO_UNA_SERIE.cuenta_con_un_presupuesto)
print(OBJETO_UNA_SERIE.tiene_un_objetivo)
print(OBJETO_UNA_SERIE.calidad)
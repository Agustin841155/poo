class Avion:
  #Atributos 
  tipo_de_combustible="depende el tipo de avion"
  tamano="pequeño,mediano,grande"
  diseno="aerodinamico"
  velocida_maxima="600km/hra"
  color="depende la aerolinea"

  #Metodos
  def puedeVolar(self):
    print("puede volar")
  def transportaPasajeros(self):
    print("trasporta pasajeros")

  def __init__(self):
    print:("metodos avion")

class AvionYet (Avion):
  #Atributos
  capacidad="depende el tipo de avion yet"
  dos_alas_o_alerones="depende el tamaño"
  iluminacion="led o tipica"
  banos="numero de baños y ubicacion"
  tienen_pantallas="si por que es de lujo"

  #Metodos
  def puedeVolar(self):
    print("puede volar como otros aviones pero mas rapido")
  def transportaPasajeros(self):
    print("es un avion exclusivo para distintos pasajeros")
  def comodidad(self):
    print("comodidad")
  def rapidez(self):
    print("rapidez")

  def __init__(self):
    print("Avion Yet")

OBJETO=Avion()
OBJETO.puedeVolar()
OBJETO.transportaPasajeros()
print(OBJETO.tipo_de_combustible)
print(OBJETO.tamano)
print(OBJETO.diseno)
print(OBJETO.velocida_maxima)
print(OBJETO.color)

OBJETO_UN_AVION = AvionYet()
OBJETO_UN_AVION.puedeVolar()
OBJETO_UN_AVION.transportaPasajeros()
OBJETO_UN_AVION.comodidad()
OBJETO_UN_AVION.rapidez()
print(OBJETO_UN_AVION.tipo_de_combustible)
print(OBJETO_UN_AVION.tamano)
print(OBJETO_UN_AVION.diseno)
print(OBJETO_UN_AVION.velocida_maxima)
print(OBJETO_UN_AVION.color)
print(OBJETO_UN_AVION.capacidad)
print(OBJETO_UN_AVION.dos_alas_o_alerones)
print(OBJETO_UN_AVION.iluminacion)
print(OBJETO_UN_AVION.banos)
print(OBJETO_UN_AVION.tienen_pantallas)
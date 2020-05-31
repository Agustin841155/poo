class Avion:
  #Atributos 
  Tipo_de_combustible="depende el tipo de avion"
  Tamano="pequeño,mediano,grande"
  Diseno="aerodinamico"
  Velocida_maxima="600km/hra"
  Color="depende la aerolinea"

  #Metodos
  def puede_volar(self):
    print("puede volar")
  def transporta_pasajeros(self):
    print("trasporta pasajeros")

  def __init__(self):
    print:("metodos avion")

class avionyet (Avion):
  #Atributos
  Capacidad="depende el tipo de avion yet"
  Dos_alas_o_alerones="depende el tamaño"
  iluminacion="led o tipica"
  Banos="numero de baños y ubicacion"
  Tienen_pantallas="si por que es de lujo"

  #Metodos
  def comodidad(self):
    print("comodidad")
  def rapidez(self):
    print("rapidez")

  def __init__(self):
    print("Avion Yet")

objeto=Avion()
objeto.puede_volar()
objeto.transporta_pasajeros()
print(objeto.Tipo_de_combustible)
print(objeto.Tamano)
print(objeto.Diseno)
print(objeto.Velocida_maxima)
print(objeto.Color)

objeto_un_avion = avionyet()
objeto_un_avion.puede_volar()
objeto_un_avion.transporta_pasajeros()
objeto_un_avion.comodidad()
objeto_un_avion.rapidez()
print(objeto_un_avion.Tipo_de_combustible)
print(objeto_un_avion.Tamano)
print(objeto_un_avion.Diseno)
print(objeto_un_avion.Velocida_maxima)
print(objeto_un_avion.Color)
print(objeto_un_avion.Capacidad)
print(objeto_un_avion.Dos_alas_o_alerones)
print(objeto_un_avion.iluminacion)
print(objeto_un_avion.Banos)
print(objeto_un_avion.Tienen_pantallas)
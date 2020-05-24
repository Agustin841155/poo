class Avion:
  #ATRIBUTOS
  Tipo_de_combustible="depende el tipo de avion"
  Tamano="pequeño,mediano,grande"
  Diseno="aerodinamico"
  Velocida_maxima="600km/hra"
  Color="depende la aerolinea"
  Capacidad="depende el tipo de avion"
  Dos_alas_o_alerones="depende el tamaño"
  iluminacion="led o tipoca"
  Banos="numero de baños y ubicacion"
  Tienen_pantallas="depende el avion"

  #METODOS
  def puede_volar(self):
    print("puede volar")
  def transporta_pasajeros(self):
    print("trasporta pasajeros")
  def comodidad(self):
    print("comodidad")
  def rapidez(self):
    print("rapidez")
  def acelerar(self):
    print("acelerar")
  
  def __init__(self):
    print("metodos avion")


objeto_un_avion = Avion()

objeto_un_avion.puede_volar()
objeto_un_avion.transporta_pasajeros()
objeto_un_avion.comodidad()
objeto_un_avion.rapidez()
objeto_un_avion.acelerar()

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
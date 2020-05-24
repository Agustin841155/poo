class Coche:
  #ATRIBUTOS
  Color="rojo"
  Tipo_de_combustible="gasolina"
  Velocidad_maxima="200km"
  Diseno="familiar"
  Tamano="mediano"
  Marca="volkswagen"
  Modelo="2010"
  puertas="4"
  Capacidad="4 personas"
  Automatico_o_Estandar="estandar"

  #METODOS
  def encender(self):
    print("encender")
  def acelerar(self):
    print("acelerar")
  def frenar(self):
    print("frenar")
  def apagar(self):
    print("apagar")
  def reproducir_musica(self):
    print("reproducir musica")
  
  def __init__(self):
    print("metodos coche")


objeto_un_coche = Coche()

objeto_un_coche.encender()
objeto_un_coche.acelerar()
objeto_un_coche.frenar()
objeto_un_coche.apagar()
objeto_un_coche.reproducir_musica()

print(objeto_un_coche.Color)
print(objeto_un_coche.Tipo_de_combustible)
print(objeto_un_coche.Velocidad_maxima)
print(objeto_un_coche.Diseno)
print(objeto_un_coche.Tamano)
print(objeto_un_coche.Marca)
print(objeto_un_coche.Modelo)
print(objeto_un_coche.puertas)
print(objeto_un_coche.Capacidad)
print(objeto_un_coche.Automatico_o_Estandar)
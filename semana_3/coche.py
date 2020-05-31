class coche:
  #Atributos 
  Color="rojo"
  Tipo_de_combustible="gasolina"
  Velocidad_maxima="depende el coche "
  Diseno="familiar o deportivo"
  Tamano="estandar"

  #Metodos
  def encender(self):
    print("encender")
  def acelerar(self):
    print("acelerar")

  def __init__(self):
    print:("metodos coche")

class cochedeportivo (coche):
  #Atributos
  Marca="volkswagen"
  Modelo="2010"
  puertas="2"
  Capacidad="2 personas"
  Automatico_o_Estandar="estandar"

  #Metodos
  def apagar(self):
    print("apagar")
  def reproducir_musica(self):
    print("reproducir musica")

  def __init__(self):
    print("coche deportivo")

objeto=coche()
objeto.encender()
objeto.acelerar()
print(objeto.Color)
print(objeto.Tipo_de_combustible)
print(objeto.Velocidad_maxima)
print(objeto.Diseno)
print(objeto.Tamano)

objeto_un_coche = cochedeportivo()
objeto_un_coche.encender()
objeto_un_coche.acelerar()
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
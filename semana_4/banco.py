class Banco:
  #Atributos 
  nombre="Banamex"
  Tamano="100 metros cuadrados"
  Logo="nombre del banco y una flor roja"
  Eslogan="el banco fuerte de mexico"
  Diseno="rectangulo azul"

  #Metodos
  def retirar(self):
    print("Retirar")
  def pagar(self):
    print("pagar")

  def __init__(self):
    print:("metodos banco")

class BancoBanamex (Banco):
  #Atributos
  Horario="8:00a.m-4:00p.m"
  color="azul"
  servicios="depositos.retiros.pretamos"
  cajeros="10"
  Estacionamiento="a la vuelta de la esquina"

  #Metodos
  def retirar(self):
    print("retirar en cajero automatico")
  def pagar(self):
    print("pagar en cajeros automaticos")
  def cobrar(self):
    print("cobrar distintos servicios")
  def depositar(self):
    print("depositar")

  def __init__(self):
    print("Banco Banamex")

OBJETO=Banco()
OBJETO.retirar()
OBJETO.pagar()
print(OBJETO.nombre)
print(OBJETO.Tamano)
print(OBJETO.Logo)
print(OBJETO.Eslogan)
print(OBJETO.Diseno)

OBJETO_UN_BANCO = BancoBanamex()
OBJETO_UN_BANCO.retirar()
OBJETO_UN_BANCO.pagar()
OBJETO_UN_BANCO.cobrar()
OBJETO_UN_BANCO.depositar()
print(OBJETO_UN_BANCO.nombre)
print(OBJETO_UN_BANCO.Tamano)
print(OBJETO_UN_BANCO.Logo)
print(OBJETO_UN_BANCO.Eslogan)
print(OBJETO_UN_BANCO.Diseno)
print(OBJETO_UN_BANCO.Horario)
print(OBJETO_UN_BANCO.color)
print(OBJETO_UN_BANCO.servicios)
print(OBJETO_UN_BANCO.cajeros)
print(OBJETO_UN_BANCO.Estacionamiento)
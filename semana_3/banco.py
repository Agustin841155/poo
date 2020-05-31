class Banco:
  #Atributos 
  nombre="Banamex"
  Tamano="100metros cuadrados"
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
  def cobrar(self):
    print("cobrar")
  def depositar(self):
    print("depositar")

  def __init__(self):
    print("Banco Banamex")

objeto=Banco()
objeto.retirar()
objeto.pagar()
print(objeto.nombre)
print(objeto.Tamano)
print(objeto.Logo)
print(objeto.Eslogan)
print(objeto.Diseno)

objeto_un_banco = BancoBanamex()
objeto_un_banco.retirar()
objeto_un_banco.pagar()
objeto_un_banco.cobrar()
objeto_un_banco.depositar()
print(objeto_un_banco.nombre)
print(objeto_un_banco.Tamano)
print(objeto_un_banco.Logo)
print(objeto_un_banco.Eslogan)
print(objeto_un_banco.Diseno)
print(objeto_un_banco.Horario)
print(objeto_un_banco.color)
print(objeto_un_banco.servicios)
print(objeto_un_banco.cajeros)
print(objeto_un_banco.Estacionamiento)
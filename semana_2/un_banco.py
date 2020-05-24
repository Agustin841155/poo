class Banco:
  #ATRIBUTOS
  nombre="Banamex"
  Tamano="100metros cuadrados"
  Logo="nombre del banco y una flor roja"
  Eslogan="el banco fuerte de mexico"
  Diseno="rectangulo azul"
  Horario="8:00a.m-4:00p.m"
  color="azul"
  servicios="depositos.retiros.pretamos"
  cajeros="10"
  Estacionamiento="a la vuelta de la esquina"
  #METODOS
  def retirar(self):
    print("Retirar")
  def pagar(self):
    print("pagar")
  def cobrar(self):
    print("cobrar")
  def depositar(self):
    print("depositar")
  def prestar_dinero(self):
    print("prestar dinero")
  
  def __init__(self):
    print("metodos banco")


objeto_un_banco = Banco()

objeto_un_banco.retirar()
objeto_un_banco.pagar()
objeto_un_banco.cobrar()
objeto_un_banco.depositar()
objeto_un_banco.prestar_dinero()

print(objeto_un_banco.nombre)
print(objeto_un_banco.Tamano)
print(objeto_un_banco.Logo)
print(objeto_un_banco.Eslogan)
print(objeto_un_banco.Diseno)
print(objeto_un_banco.Horario)
print(objeto_un_banco.color)
print(objeto_un_banco.Servicios)
print(objeto_un_banco.cajeros)
print(objeto_un_banco.estacionamientos)
class Calculadora:
  #Atributos 
  aparato_portatil="la mayoria lo son"
  tamano="chico, mediano y grande"
  diseno="mucha variedad"
  aparato_electronico="si es un aparato electronico"
  tiene_numeros="si tiene numeros"

  #Metodos
  def realizarCalculos(self):
    print("realizar calculos")
  def encender(self):
    print("encender")

  def __init__(self):
    print:("metodos calculadora")

class CalculadoraPortatil (Calculadora):
  #Atributos
  color="variedad"
  numeros="del 0 al 9"
  signos_matematicos="si tiene signos matematicos"
  las_operaciones_aritmeticas="si las 4 operaciones basicas"
  el_signo_igual="si tiene signo de igual"

  #Metodos
  def botonCancelar(self):
    print("boton para cancelar")
  def muestraResultados(self):
    print("muestra resultados")
  def realizarCalculos(self):
    print("realizar calculos matematicos")
  def encender(self):
    print("encender con el boton")

  def __init__(self):
    print("Calculadora Portatil")

OBJETO=Calculadora()
OBJETO.realizarCalculos()
OBJETO.encender()
print(OBJETO.aparato_portatil)
print(OBJETO.tamano)
print(OBJETO.diseno)
print(OBJETO.aparato_electronico)
print(OBJETO.tiene_numeros)

OBJETO_UNA_CALCULADORA = CalculadoraPortatil()
OBJETO_UNA_CALCULADORA.realizarCalculos()
OBJETO_UNA_CALCULADORA.encender()
OBJETO_UNA_CALCULADORA.botonCancelar()
OBJETO_UNA_CALCULADORA.muestraResultados()
print(OBJETO_UNA_CALCULADORA.aparato_portatil)
print(OBJETO_UNA_CALCULADORA.tamano)
print(OBJETO_UNA_CALCULADORA.diseno)
print(OBJETO_UNA_CALCULADORA.aparato_electronico)
print(OBJETO_UNA_CALCULADORA.tiene_numeros)
print(OBJETO_UNA_CALCULADORA.color)
print(OBJETO_UNA_CALCULADORA.numeros)
print(OBJETO_UNA_CALCULADORA.signos_matematicos)
print(OBJETO_UNA_CALCULADORA.las_operaciones_aritmeticas)
print(OBJETO_UNA_CALCULADORA.el_signo_igual)
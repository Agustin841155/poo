class Calculadora:
  #ATRIBUTOS
  Aparato_portatil="la mayoria lo son"
  Tamano="chico, mediano y grande"
  Diseno="mucha variedad"
  Aparato_electronico="si"
  Tiene_numeros="si"
  Color="variedad"
  numeros="del 0 al 9"
  Signos_matematicos="si"
  Las_operaciones_aritmeticas="si las 4 basicas"
  El_signo_igual="si"


  #METODOS
  def realizar_calculos(self):
    print("realizar calculosr")
  def encender(self):
    print("encender")
  def apagar(self):
    print("apagar")
  def boton_para_cancelar(self):
    print("boton para cancelar")
  def muestra_resultados(self):
    print("muestra resultados")
  
  def __init__(self):
    print("metodos calculadora")


objeto_una_calculadora = Calculadora()

objeto_una_calculadora.realizar_calculos()
objeto_una_calculadora.encender()
objeto_una_calculadora.apagar()
objeto_una_calculadora.boton_para_cancelar()
objeto_una_calculadora.muestra_resultados()

print(objeto_una_calculadora.Aparato_portatil)
print(objeto_una_calculadora.Tamano)
print(objeto_una_calculadora.Diseno)
print(objeto_una_calculadora.Aparato_electronico)
print(objeto_una_calculadora.Tiene_numeros)
print(objeto_una_calculadora.Color)
print(objeto_una_calculadora.numeros)
print(objeto_una_calculadora.Signos_matematicos)
print(objeto_una_calculadora.Las_operaciones_aritmeticas)
print(objeto_una_calculadora.El_signo_igual)
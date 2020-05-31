class calculadora:
  #Atributos 
  Aparato_portatil="la mayoria lo son"
  Tamano="chico, mediano y grande"
  Diseno="mucha variedad"
  Aparato_electronico="si es un aparato electronico"
  Tiene_numeros="si tiene numeros"

  #Metodos
  def realizar_calculos(self):
    print("realizar calculos")
  def encender(self):
    print("encender")

  def __init__(self):
    print:("metodos calculadora")

class calculadoraportatil (calculadora):
  #Atributos
  Color="variedad"
  numeros="del 0 al 9"
  Signos_matematicos="si tiene signos matematicos"
  Las_operaciones_aritmeticas="si las 4 operaciones basicas"
  El_signo_igual="si tiene signo de igual"

  #Metodos
  def boton_para_cancelar(self):
    print("boton para cancelar")
  def muestra_resultados(self):
    print("muestra resultados")

  def __init__(self):
    print("calculadora portatil")

objeto=calculadora()
objeto.realizar_calculos()
objeto.encender()
print(objeto.Aparato_portatil)
print(objeto.Tamano)
print(objeto.Diseno)
print(objeto.Aparato_electronico)
print(objeto.Tiene_numeros)

objeto_una_calculadora = calculadoraportatil()
objeto_una_calculadora.realizar_calculos()
objeto_una_calculadora.encender()
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
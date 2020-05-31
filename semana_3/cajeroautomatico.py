class cajeroautomatico:
  #Atributos 
  Disponibilidad="las 24 horas"
  Escaner_para_reconocer_tarjetas="si escanea tarjetas"
  Teclado_Numerico="tiene teclado numerico"
  Pantallas_touch="la mayoria"
  Una_computadora="si tiene una computadora"

  #Metodos
  def retirar_dinero(self):
    print("retirar dinero")
  def consultar_tu_saldo(self):
    print("consultar tu saldo")

  def __init__(self):
    print:("metodos cajero automatico")

class cajeroautomaticoBanamex (cajeroautomatico):
  #Atributos
  Tamano="estandar"
  color="depende el banco"
  Diseno="estandar"
  lo_ofrece_una_institucion_bancaria="lo ofrece banamex"
  Imprime_comprobantes="imprime comprobantes"

  #Metodos
  def realizar_pagos_de_servicios(self):
    print("realizar pagos de servicios")
  def reconocer_y_validar_billetes(self):
    print("reconocer y validar billetes")

  def __init__(self):
    print("cajero automatico banamex")

objeto=cajeroautomatico()
objeto.retirar_dinero()
objeto.consultar_tu_saldo()
print(objeto.Disponibilidad)
print(objeto.Escaner_para_reconocer_tarjetas)
print(objeto.Teclado_Numerico)
print(objeto.Pantallas_touch)
print(objeto.Una_computadora)

objeto_un_cajero_automatico = cajeroautomaticoBanamex()
objeto_un_cajero_automatico.retirar_dinero()
objeto_un_cajero_automatico.consultar_tu_saldo()
objeto_un_cajero_automatico.realizar_pagos_de_servicios()
objeto_un_cajero_automatico.reconocer_y_validar_billetes()
print(objeto_un_cajero_automatico.Disponibilidad)
print(objeto_un_cajero_automatico.Escaner_para_reconocer_tarjetas)
print(objeto_un_cajero_automatico.Teclado_Numerico)
print(objeto_un_cajero_automatico.Pantallas_touch)
print(objeto_un_cajero_automatico.Una_computadora)
print(objeto_un_cajero_automatico.Tamano)
print(objeto_un_cajero_automatico.color)
print(objeto_un_cajero_automatico.Diseno)
print(objeto_un_cajero_automatico.lo_ofrece_una_institucion_bancaria)
print(objeto_un_cajero_automatico.Imprime_comprobantes)
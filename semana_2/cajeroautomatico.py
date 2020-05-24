class Cajero_automatico:
  #ATRIBUTOS
  Disponibilidad="las 24 horas"
  Escaner_para_reconocer_tarjetas="si"
  Teclado_Numerico="si"
  Pantallas_touch="la maoyoria"
  Una_computadora="si"
  Tamaño="estandar"
  color="depende el banco"
  Diseno="estandar"
  lo_ofrece_una_institucion_bancaria="si"
  Imprime_comprobantes="si"


  #METODOS
  def retirar_dinero(self):
    print("retirar dinero")
  def consultar_tu_saldo(self):
    print("consultar tu saldo")
  def realizar_pagos_de_servicios(self):
    print("realizar pagos de servicios")
  def reconocer_y_validar_billetes(self):
    print("reconocer y validar billetes")
  def transferencia_de_fondos(self):
    print("transferencia de fondos")
  
  def __init__(self):
    print("metodos Cajero_automatico")


objeto_un_cajero_automatico = Cajero_automatico()

objeto_un_cajero_automatico.retirar_dinero()
objeto_un_cajero_automatico.consultar_tu_saldo()
objeto_un_cajero_automatico.realizar_pagos_de_servicios()
objeto_un_cajero_automatico.reconocer_y_validar_billetes()
objeto_un_cajero_automatico.transferencia_de_fondos()

print(objeto_un_cajero_automatico.Disponibilidad)
print(objeto_un_cajero_automatico.Escaner_para_reconocer_tarjetas)
print(objeto_un_cajero_automatico.Teclado_Numerico)
print(objeto_un_cajero_automatico.Pantallas_touch)
print(objeto_un_cajero_automatico.Una_computadora)
print(objeto_un_cajero_automatico.Tamaño)
print(objeto_un_cajero_automatico.color)
print(objeto_un_cajero_automatico.Diseno)
print(objeto_un_cajero_automatico.lo_ofrece_una_institucion_bancaria)
print(objeto_un_cajero_automatico.Imprime_comprobantes)
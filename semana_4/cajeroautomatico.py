class CajeroAutomatico:
  #Atributos 
  disponibilidad="las 24 horas"
  escaner_para_reconocer_tarjetas="si escanea tarjetas"
  teclado_numerico="tiene teclado numerico"
  pantallas_touch="la mayoria"
  una_computadora="si tiene una computadora"

  #Metodos
  def retirarDinero(self):
    print("retirar dinero")
  def consultarSaldo(self):
    print("consultar tu saldo")

  def __init__(self):
    print:("metodos cajero automatico")

class CajeroautomaticoBanamex (CajeroAutomatico):
  #Atributos
  tamano="estandar"
  color="depende el banco"
  diseno="estandar"
  lo_ofrece_una_institucion_bancaria="lo ofrece banamex"
  imprime_comprobantes="imprime comprobantes"

  #Metodos
  def realizarPagosServicios(self):
    print("realizar pagos de servicios")
  def reconocerValidarBilletes(self):
    print("reconocer y validar billetes")
  def retirarDinero(self):
    print("retirar dinero en cajeros banamex")
  def consultarSaldo(self):
    print("consultar tu saldo en cajeros banamex")

  def __init__(self):
    print("Cajero Automatico Banamex")

OBJETO=CajeroAutomatico()
OBJETO.retirarDinero()
OBJETO.consultarSaldo()
print(OBJETO.disponibilidad)
print(OBJETO.escaner_para_reconocer_tarjetas)
print(OBJETO.teclado_numerico)
print(OBJETO.pantallas_touch)
print(OBJETO.una_computadora)

OBJETO_UN_CAJERO_AUTOMATICO = CajeroautomaticoBanamex()
OBJETO_UN_CAJERO_AUTOMATICO.retirarDinero()
OBJETO_UN_CAJERO_AUTOMATICO.consultarSaldo()
OBJETO_UN_CAJERO_AUTOMATICO.realizarPagosServicios()
OBJETO_UN_CAJERO_AUTOMATICO.reconocerValidarBilletes()
print(OBJETO_UN_CAJERO_AUTOMATICO.disponibilidad)
print(OBJETO_UN_CAJERO_AUTOMATICO.escaner_para_reconocer_tarjetas)
print(OBJETO_UN_CAJERO_AUTOMATICO.teclado_numerico)
print(OBJETO_UN_CAJERO_AUTOMATICO.pantallas_touch)
print(OBJETO_UN_CAJERO_AUTOMATICO.una_computadora)
print(OBJETO_UN_CAJERO_AUTOMATICO.tamano)
print(OBJETO_UN_CAJERO_AUTOMATICO.color)
print(OBJETO_UN_CAJERO_AUTOMATICO.diseno)
print(OBJETO_UN_CAJERO_AUTOMATICO.lo_ofrece_una_institucion_bancaria)
print(OBJETO_UN_CAJERO_AUTOMATICO.imprime_comprobantes)
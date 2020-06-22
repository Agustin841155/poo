repetir = 's' #para repetir las veces que el usuario lo requiera
while repetir == 's' or repetir == 'S' :
  class cesarClase:#la clase cesar

    def _init_(self):
      pass
      
    def MensajeTraducidoMetodo(self):
      des = input("Desea codificar? (c)\nDesea descodificar?(d)\nR:")#para conocer que quiere realizar
      mensaje = input('\n introdusca un  texto: ')
      clave = int(input('\ningrese el valor de dezplazamiento 1-26\nValor: '))#numero de desplazamientos segun el abecedario
      if  des == 'd':     
        clave= -clave
        print('\n el mensaje descofrado es: ')#el resultado del mensaje descifrado
        for i in mensaje:#para traducir el mensaje
          traduccion = ('')
          if i.isalpha():
            num = ord(i)
            num += clave
            if i.isupper():
              if num > ord('Z'):
                num -= 26
              elif num < ord('A'):
                num += 26
            elif i.islower():
              if num > ord('z'):
                num -= 26
              elif num < ord('a'):
                num += 26            
              traduccion += chr(num)
              print(' ',traduccion)            
      elif des == 'c': 
        print('\nel mensaje cifrado es: \n')#resultado del mensaje cifrado
        for i in mensaje:
          traduccion = ('')
          if i.isalpha():
            num = ord(i)
            num += clave
            if i.isupper():
              if num > ord('Z'):
                num -= 26
              elif num < ord('A'):
                num += 26
            elif i.islower():
              if num > ord('z'):
                num -= 26
              elif num < ord('a'):
                num += 26            
              traduccion += chr(num)
              print(' ',traduccion)
  
  objeto=cesarClase()
  objeto.MensajeTraducidoMetodo()

  repetir = str(input("\n¿Desea analizar otra cadena s/n?: "))#pregunta si se quiere repetir el proceso

  if repetir == 'n' or repetir == 'N':#en caso de que no se quiera repetir
    print('\nFin del programa')
class Palindromo:#la clase palindromo recibe la cadena y la voltea para ver si es un palindromo
  def pali(string):
    string= string.replace(" ","")
    palindrom = ""
    for i in string:
      palindrom = i + palindrom 
    if (string == palindrom):
      print("es un palindromo")
    else:
      print("No es un palindromo")

class Contador:#es la clase que ceunta las vocales y espacios
  def vocales(string):#cuenta las vocales que tiene la frase
    a = string.count("a")
    e = string.count("e")
    i = string.count("i")
    o = string.count("o")
    u = string.count("u")
    count = a +e +i+o+u
    print ("La palabra cuenta con :", count, " vocales")#imprime el resultado de las vocales
  def spaces(string):
    count = string.count(" ")
    print ("La palabra cuenta con :",count, " espacios")#imprime el resultado de los espacios

respuesta = "S"
while (respuesta == "S" or respuesta == "s"):#es para repetir el proceso si asi se desea
  string = []
  string = input("Igresa una palabra: ")
  s = Contador 
  s.vocales(string)
  s.spaces(string)
  st = Palindromo
  st.pali(string)
  respuesta = input ("¿Desea analizar otra cadena s/n?: ")#lee la entrada si se quiere repetir el proceso
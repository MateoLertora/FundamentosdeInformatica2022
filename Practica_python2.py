#PRACTICA PYTHON 2
#punto 1
def maymin(palabra):
    if palabra[0] == str.upper(palabra[0]):
        return "Mayúscula"
    elif palabra[0] == str.lower(palabra[0]):
        return "Minuscula"      

print(maymin("oma"))    

#punto 2
def clasificar(numero):
  resultado = ""
  if numero > 0:
      resultado += "Positivo"
  elif numero < 0:
      resultado += "Negativo"
  else:
      resultado += "Cero"
  return resultado + "-" + impar_o_par(numero)    

def impar_o_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"    
print(clasificar(-3))

#punto 3
def cara_opuesta(numero):
    if 1 <= numero <= 6:
        return 7 - numero
    else:
        return "Numero incorrecto"  
print(cara_opuesta(5))              

#punto 4
def cobro_paquete(ubicación, peso):
    if peso > 5000:
        return "Entrega rechazada"
    elif ubicación == "América del sur":
        return peso * 10.00
    elif ubicación == "América central":
        return peso * 15.00
    elif ubicación == "América del norte":
        return peso * 18.00 
    elif ubicación == "Europa":
        return peso * 24.00 
    elif ubicación == "Asia":
        return peso * 30.00
print(cobro_paquete("Asia", 6000)) 

#punto 5
def dia_semana(numero):
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    if 1 <= numero <= 7:
        return dias[numero - 1]
    else:
        return "Numero incorrecto"
print(dia_semana(0))            

#punto 6 
lista1 = ["h", "o", "l", "a"]
lista2 = list(reversed(lista1))
print(lista2)

#punto 7
numeros = [input("num1: "), input("num2: "), input("num3: "), input("num4: ")]
lista = [] 
for numero in numeros:
    if int(numero) >= 0:
        lista += numero
    if int(numero) < 0:
        print(lista) 
            


#punto 8
def suma(lista1, lista2):
  lista3 = []
  for i in lista1:
    list.append(lista3, lista1[i - 1] + lista2[i - 1])
  return lista3
print(suma([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))

#punto 9

#programa = [input("N1: "), input("N2: "), input("N3: ")]
#edad_maxima = max("E1: ", "E2: ", "E3: ")

#punto 10
def apariciones(palabra):
    dic = {}
    for letra in palabra:
        if letra not in dic:
          dic[letra] = 1
        elif letra in dic:
          dic[letra] += 1
    return dic 
print(apariciones("holala"))
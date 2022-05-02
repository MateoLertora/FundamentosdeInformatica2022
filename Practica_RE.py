
import re
#1 
def caracter_permitido(string):
    return bool(re.findall("\w", string))

print(caracter_permitido(".h"))   

#2
def caracter_permitido2(string):
    resultado = True
    for caracter in string:
        if not bool(re.findall("\w", caracter)):
            return False
    return resultado

print(caracter_permitido2("hola..¿")) 


#3
def condicion_ninguna_o_mas(string):
    return bool(re.findall("he*", string))
     
print(condicion_ninguna_o_mas("hole"))    


def condicion_1_o_mas(string):
    return bool(re.findall("he+", string))
       
print(condicion_1_o_mas("heeole"))


def condicion_2_o_3(string):
    return bool(re.findall("he{2,3}", string))
     

#print(condicion_2_o_3("heole"))

#4
def unida_con_guion(string_sin_espacios):
    if bool(re.findall("\s", string_sin_espacios)) == True:
        return "string no permitido"
    else:
        return re.findall("\D\w*_\D\w*", string_sin_espacios)

#print(unida_con_guion("hola_hola"))

#5
def empieza_con(string, numero):
    return bool(re.findall(numero, string[0:len(numero)]))

#print(empieza_con("5690", "54"))

#6
def estan_enFrase(lista_strings, frase):
    for string in lista_strings:
        resultado =  bool(re.findall(string, frase))
    return resultado    

#print(estan_enFrase(["hola", "como", "te"], "hola como va"))


#7
def solamente(string):
    resultado = ""
    lista = re.findall("[\w\s]", string)
    for caracter in lista:
        resultado += caracter
    return resultado

#print(solamente("trggf gggg##"))

#8
def separar_caracs_numericos(string):
    return re.findall("\d", string)

#print(separar_caracs_numericos("gdolfdn3456kdf"))

#9
def separar_caracs_conGuiones(string):
    return re.findall("-(.*?)-", string)

#print(separar_caracs_conGuiones("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))

#10
def ejer10(string):
    return re.search("(@|&)(.*?)(@|&)", string)

#print(ejer10("tutelertora&gmail@.com"))    

#11
def ejer11(lista_strings):
    for elemento in lista_strings:
        resultado = re.match("(P\w*)(P\w*)", elemento)
    return resultado

#print(ejer11(["Práctica Python", "Práctica C++", "Práctica Fortran"]))

#12
def ejer12(string):
    return re.sub("[\s_:]", "|", string)

#print(ejer12("Nombre: Mateo"))

#13
def ejer13(string):
    return re.sub("\W", "_", string,2)

#print(ejer13("Tute#lertora#sepu#estono"))

#14
def ejer14(string):
    return re.sub("[\s\t]", ";", string)
#print(ejer14("hola como     teva")) 

#15
def ejer15(mail):
    return bool(re.findall("[\w]+[\.-_/]*[\w]+@[a-z]{1,9}(\.[a-z]){1,4}(\.[a-z]){0,1}", mail))

#print(ejer15("tutelertora@@gmail.com"))
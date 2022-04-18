#PRACTICA PYTHON 1

def ejer1(string):
    return len(string)
print(ejer1("hola"))

def ejer2(palabra):
    return str.upper(palabra[4]) + str.upper(palabra[5])
print(ejer2("holasa"))    

def ejer3(nombre, apellido):
    return "Hola " + nombre + " " + apellido
print(ejer3("Leo", "Messi"))

def ejer4(nombre, apellido, segundo_apellido):
    return str.upper(nombre[0]) + "." + str.upper(apellido[0]) + "." + str.upper(segundo_apellido[0])
print(ejer4("Tomas", "Toto", "Lanzini"))

def ejer5(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3) / 3
print(ejer5(1, 2, 3))  

def ejer6(minutos):
    return str(minutos // 60) + " horas" + " " + str(minutos % 60) + " minutos"
print(ejer6(150))

def ejer7(sueldo_base):
    comision = 0.1 * sueldo_base * 4
    return "Extra:" + str(comision) + " Total:" + str(comision + sueldo_base)
print(ejer7(100))

#8
respuestas = [input("respuesta1: "), input("respuesta2: "), input("respuesta3: ")]
nota = 0
for respuesta in respuestas:
    if respuesta == "Correcta":
        nota += 4
    if respuesta == "Incorrecta":
        nota -= 1
    if respuesta == "":
        nota += 0
print(nota)

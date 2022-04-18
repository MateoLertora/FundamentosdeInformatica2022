#PRACTICA MANIPULACION DE ARCHIVOS
#1 
def CuantasNO(archivo, letra):
    suma = 0
    with open(archivo, "r") as f:
        for linea in f.read().split("\n"):
            if linea[0] != letra:
                suma += 1
    print(suma)
print(CuantasNO("bio.txt", "m"))    

#2
def imprimir_arch(archivo, lineas):
  contador = lineas - 1
  with open(archivo, "r") as f:
    listas = f.readlines()
    print(listas[:contador + 1])

print(imprimir_arch("bio.txt", 1))

#3
def guardar(archivo, lineas):
    lista = []
    with open(archivo, "r") as f:
        for i in f:
            lista.append(i)
    print(lista[-lineas:])

#4
def contar(archivo):
    with open(archivo, "r") as f:
        lista_palabras = f.read().split()
        print(len(lista_palabras))

#5
def reemplazar(archivo1, archivo2):
    with open(archivo1, "r") as f, open(archivo2, "w") as a:
        for palabra in f.read():
            for letra in palabra:
                a.write(letra.replace(letra, letra + "\n"))

#6 
def eliminar(archivo1, archivo2):
    with open(archivo1, "r") as f, open(archivo2, "w") as a:
        for linea in f.read():
            a.write(linea.strip("\n"))

#7
def palabra_larga(archivo):
    caracteres = 0
    palabra = ""
    with open(archivo, "r") as f:
        lista_palabras = f.read().split()
        for word in lista_palabras:
            if len(word) > caracteres:
                caracteres = len(word)
                palabra = word
    return palabra, caracteres

#8
#def juntar_archivos(archivo1, archivo2, archivo3):
    #with open(archivo1, "r") as f, open(archivo2, "r") as a, open(archivo3, "a") as af:
        #for palabra in f.read():
            #af.write(palabra.replace(archivo1, archivo3))
        #for palabra in a.read():
            #af.write(palabra.replace(archivo2, archivo3))

def juntar_archivos(arch1, arch2, arch3):
  with open(arch1, "r") as f, open(arch2, "r") as a, open(arch3, "a") as af:
    for palabra in f.read():
      af.write(palabra)
    for palabra in a.read():
      af.write(palabra) 

print(juntar_archivos("butaneta.txt", "bio.txt", "hola.txt"))

#9
def frecuencia(archivo):
  frecuencias = {}
  with open(archivo, "r") as f:
    separacion = f.read().split()
    for palabra in separacion:
      if palabra in frecuencias:
        frecuencias[palabra] += 1
      else:
        frecuencias[palabra] = 1
    for palabra in frecuencias.keys():
      frecuencias[palabra] = round(frecuencias[palabra] / len(separacion),3)
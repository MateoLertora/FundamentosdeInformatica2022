#Practica POO
class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

#INTERFAZ (mensajes que entiende): comer y acariciar
#ESTADO (ej energía): energia

#2)
    def volar(self, kms):
        if self.energia > 0:
            self.energia -= 10 + kms        
        else:
            pass

#3)
class Notebook:
    def __init__(self):
        self._marca = "Lenovo"
        self._modelo = "ThinkPad"
        self._precio = 20000

    def descuento(self, porcentaje):
        return self._precio * (1 - porcentaje/100)


notebook = Notebook()
print(notebook._marca)
print(notebook._modelo)
print(notebook._precio)
print(notebook.descuento(30))

#4)
class Contador:
    def __init__(self, numero):
        self.numero = numero

    def inc(self):
        self.numero += 1

    def dis(self):
        self.numero -= 1

    def reset(self):
        self.numero = 0

    def valorActual(self):
        return self.numero

    def valorNuevo(self, nuevoValor):
        self.numero = nuevoValor
   

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
print(contador.valorActual())
contador.valorNuevo(27)
contador.dis()
contador.dis()
print(contador.valorActual())
print(contador.ultimoComando())
#5) 
#def ultimoComando(self):
    #for comandos in contador:
        #return contador[0]

#print(contador.ultimoComando())

#6)
class Calculadora:
    def __init__(self):
        self.numero = 0

    def cargar(self, numero):
        self.numero = numero

    def sumar(self, numero):
        self.numero += numero

    def restar(self, numero):
        self.numero -= numero

    def multiplicar(self, numero):
        self.numero *= numero

    def valor_actual(self):
        return self.numero    

calculadora = Calculadora()
print(calculadora.cargar(0))
print(calculadora.sumar(4))
print(calculadora.multiplicar(5))
print(calculadora.restar(8))
print(calculadora.multiplicar(2))
print(calculadora.valor_actual())

#7)
class Gorriones:
    def __init__(self):
        self.alimento = 0
        self.gramos = 0
        self.vuelo = 0
        self.kilometros = 0

    def volar(self, kms):
        self.vuelo += 1
        self.kilometros += kms

    def comer(self, gramos):
        self.alimento += 1
        self.gramos += gramos

    def CSS(self):
        return self.kilometros / self.gramos
    
                    



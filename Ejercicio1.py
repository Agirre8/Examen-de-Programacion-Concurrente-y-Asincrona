import threading

class Banco:
    def __init__():
        self.cuenta=100
        self.semaforo = threading.Semaphore(1)#solo se permite solo se permite un hilo a la vez al acceder al recurso compartido, en este caso, la cuenta bancaria
        self.saldo = saldo

    def ingresar(self, cantidad):
        semaforo.acquire()  #accedemos al semaforo para acceder a la cuenta
        self.saldo += cantidad  
        semaforo.release()  #nos salimos del semaforo, lo dejamos libre 

    def retirar(self, cantidad):
        semaforo.acquire()
        self.saldo -=cantidad
        semaforo.release()
def ingresar_1(cuenta, cantidad):
    for i in range(0, cantidad):
        banco.ingresar(cantidad)


def retirar_1(cuenta, cantidad):
    for i in range(0, cantidad):
        banco.retirar(cantidad)





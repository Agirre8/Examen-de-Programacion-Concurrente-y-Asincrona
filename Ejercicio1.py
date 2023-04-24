import threading

class Banco:
    def __init__():
        self.cuenta=100
        self.semaforo = threading.Semaphore(1)#solo se permite solo se permite un hilo a la vez al acceder al recurso compartido, en este caso, la cuenta bancaria
        
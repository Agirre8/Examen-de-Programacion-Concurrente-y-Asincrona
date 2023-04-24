from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
#Bueno, para utilizar executors y actualizar el saldo de los jugadores, debemos modificar la clase Jugador 
# y la clase Banco para utilizar el patrón Observer y asegurarnos de que el saldo de cada jugador se actualice 
# correctamente después de cada ronda.

class Observer(ABC):
    @abstractmethod
    def update(self, saldo):
        pass


class Jugador(Observer):
    def __init__(self, saldo_inicial, num_juegos, observador):
        self.saldo = saldo_inicial
        self.num_juegos = num_juegos
        self.observador = observador
        self.num_ganados_num = 0
        self.num_ganados_par = 0
        self.num_ganados_impar = 0
        self.num_ganados_martingala = 0

    def update(self, saldo):
        self.saldo = saldo

    def jugar_numero(self, numero, saldo, banco):
        apuesta = 10
        if saldo < apuesta:
            return saldo
        saldo -= apuesta
        resultado = random.randint(0, 36)
        if resultado == numero:
            saldo += 360
            banco -= 360
            self.num_ganados_num += 1
        else:
            banco += apuesta
        return saldo

    def jugar_par_impar(self, par, saldo, banco):
        apuesta = 10
        if saldo < apuesta:
            return saldo
        saldo -= apuesta
        resultado = random.randint(0, 36)
        if resultado == 0:
            banco += apuesta
        elif resultado % 2 == 0 and par == "par":
            saldo += 20
            banco -= 20
            self.num_ganados_par += 1
        elif resultado % 2 != 0 and par == "impar":
            saldo += 20
            banco -= 20
            self.num_ganados_impar += 1
        else:
            banco += apuesta
        return saldo

    def jugar_martingala(self, numero, saldo, banco):
        apuesta = 10
        if saldo < apuesta:
            return saldo
        saldo -= apuesta
        resultado = random.randint(0, 36)
        if resultado == numero:
            saldo += 360
            banco -= 360
            self.num_ganados_martingala += 1
        else:
            saldo = self.jugar_martingala(numero, saldo * 2, banco)
        return saldo

    def jugar(self, banco):
        # Jugando con número específico
        with ThreadPoolExecutor(max_workers=4) as executor:
            resultados = executor.map(self.jugar_numero, [random.randint(1, 36) for _ in range(4)], [self.saldo] * 4, [banco] * 4)
        self.saldo = sum(resultados)
        print(resultados)

        # Jugando par/impar
        with ThreadPoolExecutor(max_workers=4) as executor:
            resultados = executor.map(self.jugar_par_impar, ["par"] * 2 + ["impar"] * 2, [self.saldo] * 4, [banco] * 4)
        self.saldo = sum(resultados)
        print(resultados)

        # Jugando con martingala
        with ThreadPoolExecutor(max_workers=4) as executor:
            resultados = executor.map(self.jugar_martingala, [random.randint(1, 36) for _ in range(4)], [self.saldo] * 4, [banco] * 4)
        self.saldo = sum(resultados)
        print(resultados)
    

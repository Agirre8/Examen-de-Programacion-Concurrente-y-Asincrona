import random
from threading import Thread
from multiprocessing import Pool, Manager


def jugar_numero(numero, saldo, banco):
    apuesta = 10
    if saldo < apuesta:
        return saldo
    saldo -= apuesta
    resultado = random.randint(0, 36)
    if resultado == numero:
        saldo += 360
        banco.value -= 360
    else:
        banco.value += apuesta
    return saldo


def jugar_par_impar(par, saldo, banco):
    apuesta = 10
    if saldo < apuesta:
        return saldo
    saldo -= apuesta
    resultado = random.randint(0, 36)
    if resultado == 0:
        banco.value += apuesta
    elif resultado % 2 == 0 and par == "par":
        saldo += 20
        banco.value -= 20
    elif resultado % 2 != 0 and par == "impar":
        saldo += 20
        banco.value -= 20
    else:
        banco.value += apuesta
    return saldo


def jugar_martingala(numero, saldo, banco):
    apuesta = 10
    if saldo < apuesta:
        return saldo
    saldo -= apuesta
    resultado = random.randint(0, 36)
    if resultado == numero:
        saldo += 360
        banco.value -= 360
    else:
        saldo = jugar_martingala(numero, saldo*2, banco)
    return saldo


def jugar(saldo, banco, num_juegos):
    num_ganados_num = 0
    num_ganados_par = 0
    num_ganados_impar = 0
    num_ganados_martingala = 0

    # Jugando con número específico
    with Pool(4) as p:
        resultados = p.starmap(jugar_numero, [(random.randint(1, 36), saldo, banco) for _ in range(4)])
    saldo = sum(resultados)
    num_ganados_num = resultados.count(370)

    # Jugando par/impar
    with Pool(4) as p:
        resultados = p.starmap(jugar_par_impar, [("par", saldo, banco) for _ in range(2)] + [("impar", saldo, banco) for _ in range(2)])
    saldo = sum(resultados)
    num_ganados_par = resultados.count(saldo+20)

    # Jugando con martingala
    with Pool(4) as p:
        resultados = p.starmap(jugar_martingala, [(random.randint(1, 36), saldo, banco) for _ in range(4)])
    saldo = sum(resultados)
    num_ganados_martingala = resultados.count(370)

    num_ganados_impar = num_juegos - num_ganados_num - num_ganados_par - num_ganados_martingala

    return saldo, num_ganados_num, num_ganados_par, num_ganados_impar, num_ganados_martingala


def main():
    num_juegos = 1000
    saldo_inicial = 1000
    banco = Manager().Value("i", 50000)
    jugadores = [Thread(target=jugar, args=(saldo_inicial, banco, num_juegos)) for _ in range(10)]
    saldos_finales = []

    for jugador in jugadores:
        jugador.start()

    for jugador in jugadores:
        jugador.join()
        saldo_final = jugador._target[0] # Obtenemos el saldo final del jugador
        saldos_finales.append(saldo_final)

    print("Saldos finales de los jugadores:", saldos_finales)

main()
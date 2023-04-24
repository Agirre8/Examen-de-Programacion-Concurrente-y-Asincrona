import multiprocessing as mp

#funcion que añade una cantidad dada a la cuenta
def proceso_ingreso(cuenta, cantidad):
    cuenta.deposit(cantidad)

#funcion que saca una cantidad dada a la cuenta
def proceso_retirada(cuenta, cantidad):
    cuenta.withdraw(cantidad)


if __name__ == '__main__':
    # inicializa el manager y la cuenta con 100 euros
    with mp.Manager() as manager:
        cuenta = manager.Value('i', 100)

        ingresos = [(cuenta, 100)] * 40 + [(cuenta, 50)] * 20 + [(cuenta, 20)] * 60
        retiradas = [(cuenta, 100)] * 40 + [(cuenta, 50)] * 20 + [(cuenta, 20)] * 60

        #una lista para almacenar procesos
        procesos = []
        for ingreso in ingresos:
            p = mp.Process(target=proceso_ingreso, args=ingreso)
            procesos.append(p)
            p.start()
        for retirada in retiradas:
            p = mp.Process(target=proceso_retirada, args=retirada)
            procesos.append(p)
            p.start()
        for proceso in procesos:
            proceso.join()

        if cuenta.value == 100:
            print("La cuenta tiene 100 euros de saldo")
        else:
            print("la cantidad de dinero no es correcta!!!!")

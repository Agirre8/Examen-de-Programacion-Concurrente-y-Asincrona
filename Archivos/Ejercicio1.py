from multiprocessing import Pool, Manager

def ingreso(saldo, cantidad):
    saldo.value += cantidad

def retiro(saldo, cantidad):
    saldo.value -= cantidad

def main():
    saldo = Manager().Value('i', 100)

    # Procesos que ingresan dinero
    with Pool() as p:
        p.starmap(ingreso, [(saldo, 100)]*40)
        p.starmap(ingreso, [(saldo, 50)]*20)
        p.starmap(ingreso, [(saldo, 20)]*60)

    # Procesos que retiran dinero
    with Pool() as p:
        p.starmap(retiro, [(saldo, 100)]*40)
        p.starmap(retiro, [(saldo, 50)]*20)
        p.starmap(retiro, [(saldo, 20)]*60)

    # Comprobar si el saldo final es el esperado
    assert saldo.value == 100, f'El saldo final es {saldo.value}, se esperaba 100'
    print('El saldo final es el esperado (100 euros)')

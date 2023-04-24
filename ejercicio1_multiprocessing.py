import multiprocessing as mp

#funcion que añade una cantidad dada a la cuenta
def proceso_ingreso(cuenta, cantidad):
    cuenta.deposit(cantidad)

#funcion que saca una cantidad dada a la cuenta
def proceso_retirada(cuenta, cantidad):
    cuenta.withdraw(cantidad)


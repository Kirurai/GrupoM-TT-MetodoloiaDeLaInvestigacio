def pedirCantidadNumeros():
    """Devuelve un entero positivo pedido por teclado"""
    while True:
        cantidadIngresada = input("Ingrese la cantidad de numeros a los que desee comprobar: ")
        if esCantidadValida(cantidadIngresada):
            break

    return int(cantidadIngresada)


def esCantidadValida(cantidad):
    try:
        if int(cantidad) > 0:
            return True
        else:
            print("Intente nuevamente (el numero debe ser un entero positivo)")
            return False
    except ValueError:
        print("Intente nuevamente (el numero debe ser un entero positivo)")
        return False


def pedirListaNumeros(tamaño):
    """Devuelve una lista de números enteros positivos de 4 dígitos máximo ingresados por teclado"""
    listaNumeros = []
    for x in range(tamaño):
        print("--------Número #{}--------".format(x+1))
        listaNumeros.append(pedirNumero())

    return listaNumeros


def pedirNumero():
    """Devuelve un entero positivo ingresado por teclado"""
    while True:
        numero = input("Ingrese un número positivo de 4 dígitos máximo:")
        if esNumeroValido(numero):
            break
    return int(numero)


def esNumeroValido(numero):
    try:
        if 0 < int(numero) < 10000:
            return True
        else:
            print("Intente nuevamente")
            return False
    except ValueError:
        print("Intente nuevamente")
        return False


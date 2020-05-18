from ordenar import ordenarDescendente, ordenarAscendente
def calcularCantidadDeVueltas(numero):
    constanteKaprekar = 6174
    vueltas = 0
    operador = numero
    for x in range(10):
        if operador == constanteKaprekar:
            return x
        if x == 8:
            return x
        operador = rutinaKaprekar(operador)
        vueltas+=1


def rutinaKaprekar(numero):
    digitos = "{:04d}".format(numero)   # transforma el int en un str y agrega 0 al inicio si es necesario hasta llegar a los 4 dígitos
    menor = ordenarAscendente(digitos)
    mayor = ordenarDescendente(digitos)
    return mayor - menor







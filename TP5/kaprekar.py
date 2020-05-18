from ordenar import ordenar_ascendente, ordenar_descendente

CONSTANTE_KAPREKAR = 6174


def calcular_cantidad_vueltas(numero):
    """Devuelve un entero, la cantidad de ciclos de la rutina de Kaprekar para llegar a la constante

    Toma un entero por parametro, le aplica la rutina de Kaprekar y devuelve la cantidad de ciclos necesarios para
    llegar a la constante de Kaprekar(6174), un entero de 0 a 8.
    """
    operador = numero
    for ciclo in range(7):                      # Cantidad máxima de iteraciones para llegar a la constante de Kaprekar
        if operador == CONSTANTE_KAPREKAR:
            return ciclo

        operador = rutina_kaprekar(operador)
    else:                                       # En caso de números con todas sus cifras iguales
        return 8


def rutina_kaprekar(numero):
    """Devuelve un entero luego de aplicar un ciclo de la rutina de Kaprekar

    Toma un entero por parámetro, lo transforma en str para ordenar sus dígitos, devuelve la resta de los numeros
    ordenados.
    """
    digitos = "{:04d}".format(numero)           # Para compensar la falta de dígitos

    menor = ordenar_ascendente(digitos)
    mayor = ordenar_descendente(digitos)

    return mayor - menor

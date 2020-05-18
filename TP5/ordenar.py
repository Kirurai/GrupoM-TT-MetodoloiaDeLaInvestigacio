def ordenar_ascendente(numero):
    """Devuelve un numero entero, ingresado por parámetro, con dígitos ordenados ascendentemente"""
    ascendente = "".join(sorted(str(numero)))

    return int(ascendente)


def ordenar_descendente(numero):
    """Devuelve un numero entero, ingresado por parámetro, con dígitos ordenados descendentemente"""
    descendente = "".join(sorted(str(numero), reverse=True))

    return int(descendente)

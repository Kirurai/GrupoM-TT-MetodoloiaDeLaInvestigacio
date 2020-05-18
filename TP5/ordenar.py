def ordenarAscendente(numero):
    ascendente = "".join(sorted(numero))    # genera una lista con todos los caracteres que forman el número ordenados en forma ascendente y los concatena en un str.
    return int(ascendente)


def ordenarDescendente(numero):
    descendente = "".join(sorted(numero, reverse=True))     # genera una lista con todos los caracteres que forman el número ordenados en forma descendente y los concatena en un str.
    return int(descendente)
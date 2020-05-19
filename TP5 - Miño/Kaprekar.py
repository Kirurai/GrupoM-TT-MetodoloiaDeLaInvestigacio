while True:
    cantidad = input("Ingrese la cantidad de números que quiere ingresar: ")
    if cantidad.isdigit() and (int(cantidad) > 0):
        break
    print("El valor ingresado es invalido. Vuelva a intentarlo")

respuestas = []
for x in range(0, int(cantidad)):

    while True:
        numero = input("Ingrese un numero natural de hasta 4 digitos, con al menos uno diferente: ")
        if (numero.isdigit()) and (len(numero) <= 4) and """(int(numero) % 1111 != 0)""":
            break
        print("Ha ingresado un número invalido. Por favor vu2elta a intentarlo")


    for i in range(0,9):
        if (numero == "6174") or (i == 8):
            respuestas.append(i)

            break
        while len(numero) != 4:
            numero += "0"
        ascendente = []
        descendente = []
        for j in range(0, 4):
            ascendente.append(numero[j])
            descendente.append(numero[j])


        ascendente = sorted(ascendente)
        descendente = sorted(descendente, reverse=True)
        numero = str((abs(int("".join(ascendente)) - int("".join(descendente)))))


for x in range(0, len(respuestas)):
    print(respuestas[x])
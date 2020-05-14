while True:
    numero = input("Ingrese un numero natural de hasta 4 digitos, con al menos uno diferente: ")
    if (numero.isdigit()) and (len(numero) <= 4) and (int(numero) % 1111 != 0):
        break
    print("Ha ingresado un número invalido. Por favor vuelta a intentarlo")

if numero == "6174":
    "Ha ingresado la constante de Kaprekar. Felicidades lo resolvió en 0 iteraciones"

for x in range(0, 4 - len(numero)):
    numero += "0"

k = 0
# Una vez llegado a la cte de Kaprekar o superado las 7 iteraciones. El while finalizará
print("{} es el tipo de numero".format(type(numero)))
while (numero != "6174") and (k < 8):
    ascendente = []
    descendente = []
    for x in range(0, 4):
        ascendente.append(numero[x])
        descendente.append(numero[x])

    sorted(ascendente)
    sorted(descendente, reverse=True)

    k += 1
    numero = (abs(int("".join(ascendente)) - int("".join(descendente))))
    print(numero)

if k == 8:
    print("Exceso de iteraciones. Ha ocurrido un error al validar los datos. Contactesé con su diosito de turno")
else:
    print("Felicidades ha alcanzado la constante de Kaprekar, 6174, en {} iteraciones".format(k))

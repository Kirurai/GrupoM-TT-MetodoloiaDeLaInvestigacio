while True: #Se pide el ingreso y que el mismo sea válido para utilizar a futuro
    cantidad = input("Ingrese la cantidad de números que quiere ingresar: ")
    if cantidad.isdigit() and (int(cantidad) > 0):
        break
    print("El valor ingresado es invalido. Vuelva a intentarlo")

respuestas = [] #Inicialización del array de respuestas. 
for x in range(0, int(cantidad)): #Se se pedira un número y se realizará la rutina de Kaprekar las veces que se ha dicho anteriormente

    while True: #Ingreso del número de 4 digitos, no puede ser mayor, y deben ser números
        numero = input("Ingrese un numero natural de hasta 4 digitos, con al menos uno diferente: ")
        if (numero.isdigit()) and (len(numero) <= 4) and """(int(numero) % 1111 != 0)""":
            break
        print("Ha ingresado un número invalido. Por favor vu2elta a intentarlo")


    for i in range(0,9): #Se realizará la rutina un total de 8 veces (en la octava, entra en el siguiente if y sale del programa) ya que por definición 7 es el máxim para llegar a dicha constante
        if (numero == "6174") or (i == 8): #Se empieza comprobando si el número es la constante o es la octava itearación
            respuestas.append(i)            #en el caso de que se ingrese el número efectivamente, ingresará 0 como respuesta
            break
            
        while len(numero) != 4: #Completa el número ingresado por si tiene menos de 4 digitos. i.e ingresó "34" lo completa como "3400". 
            numero += "0"           #Donde complete los ceros, es irrelevante
        #Creando listas donde estarán los dígitos de manera ascendentes y descendentes
        ascendente = []
        descendente = [] 
        for j in range(0, 4):
            ascendente.append(numero[j])
            descendente.append(numero[j])

        #Se ordenan los digitos de las listas
        ascendente = sorted(ascendente)
        descendente = sorted(descendente, reverse=True)
        #Se unen las componentes de los array y se transforman en int, para realizar la resta y volver al tipo original
        numero = str((abs(int("".join(ascendente)) - int("".join(descendente)))))

#Se imprimen las respuestas por consola
for x in range(0, len(respuestas)): 
    print(respuestas[x])

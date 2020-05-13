def ordenarMayorMenor(num): #recibe un numero, devuelve el numero con las cifras ordenadas de mayor a menor

    # obtiene cada cifra del numero
    unidad = int(num) % 10
    decena = int(int(num) / 10) % 10
    centena = int(int(num) / 100) % 10
    unidadmil = int(int(num) / 1000)

    numeroAOrdenar = [unidad, decena, centena, unidadmil]   #coloca las cifras en un vector
    menorAMayor = sorted(numeroAOrdenar)    #ordena las cifras de menor a mayor
    mayorAMenor = menorAMayor[::-1]     #invierte el orden de los valores para dejarlos de mayor a menor
    numeroOrdenado = str(mayorAMenor[0]) + str(mayorAMenor[1]) + str(mayorAMenor[2]) + str(mayorAMenor[3])  #coloca cada cifra para armar el nuevo numero

    return numeroOrdenado   #devuelve el numero ordenado de mayor a menor


def ordenarMenorMayor(num): #funcion que recibe un numero y ordena sus cifras de mayor a menor, retorna el numero ordenado

    #obtiene cada cifra del numero
    unidad = int(num) % 10
    decena = int(int(num) / 10) % 10
    centena = int(int(num) / 100) % 10
    unidadmil = int(int(num) / 1000)

    numeroAOrdenar = [unidad, decena, centena, unidadmil]   #coloca las cifras en un vector
    menorAMayor = sorted(numeroAOrdenar)    #ordena las cifras de menor a mayor
    numeroOrdenado = str(menorAMayor[0]) + str(menorAMayor[1]) + str(menorAMayor[2]) + str(menorAMayor[3])  #coloca cada cifra para armar el nuevo numero

    return numeroOrdenado   #devuelve el numero ordenado de menor a mayor

def  rutinaKaprekar(vectorNum):  #funcion para ejecutar la rutina de Kaprekar

    CONSTANTE_KAPREKAR = 6174   #constante

    for x in vectorNum: #recorre el listado de numeros

        if x == CONSTANTE_KAPREKAR: #si el numero es igual a la constante
            print("Repeticiones: 0")
        else:   #si el numero es diferente a la constante
            repeticiones = 1    #asigna la primer repeticion
            print("Numero: "+str(x))    #imprime el numero
            numeroParaOrdenar = x   #numero a ordenar
            menor=ordenarMenorMayor(numeroParaOrdenar)  #numero ordenado de menor a mayor
            mayor=ordenarMayorMenor(numeroParaOrdenar)  #numero ordenado de mayor a menor

            while (int(mayor) - int(menor)) != CONSTANTE_KAPREKAR:  #si la resta entre el mayor y el menor es diferente a la constante, vuelve a realizar el proceso anterior
                numeroParaOrdenar = int(mayor) - int(menor)
                menor = ordenarMenorMayor(numeroParaOrdenar)
                mayor = ordenarMayorMenor(numeroParaOrdenar)
                repeticiones = repeticiones+1   #agrega una repeticion

            print("Repeticiones: "+str(repeticiones))   #imprime el numero de repeticiones necesarias para llegar a la constante


def ingresaNumeroValido(casos):   #funcion para ingresar los numeros a comprobar

    numeros=[]  #vector de numeros

    while len(numeros)<int(casos):   #mientras falten numeros

        numNuevo = input("Ingrese un numero de 4 cifras, que tenga al menos 2 diferentes: ") #pide un numero

        if len(numNuevo) == 4:  #si el numero es menor de 4 cifras
            #revisa que por lo menos haya un numero diferente entre las 4 cifras
            unidad = int(numNuevo) % 10
            decena = int(int(numNuevo) / 10) % 10
            centena = int(int(numNuevo) / 100) % 10
            unidadmil = int(int(numNuevo) / 1000)

            if unidad == decena == centena == unidadmil:
                print("Numero erroneo. No se hallaron 2 cifras diferentes.")

            else:   #el numero cumple con todas las condiciones
                numeros.append(numNuevo)    #se agrega el numero al vector de numeros

        else:
            print("Número erroneo. No tiene 4 cifras.")
    #fin del while
    return numeros  #regresa el vector numeros una vez lleno


#main
casosDePrueba = "0"
while casosDePrueba == str(0):
    casosDePrueba = input("Ingrese el numero de casos de prueba: ") #solicita numero de caso de pruebas, no puede ser 0

numeros = ingresaNumeroValido(casosDePrueba)    #ejecuta funcion de carga de numeros

rutinaKaprekar(numeros) #ejecuta la rutina de Kaprekar


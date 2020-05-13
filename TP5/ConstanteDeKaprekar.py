def ordenarMayorMenor(num): #recibe un numero, devuelve el numero con las cifras ordenadas de mayor a menor

    unidad = int(num) % 10
    decena = int(num / 10) % 10
    centena = int(num / 100) % 10
    unidadmil = int(num / 1000)

    numeroAOrdenar = [unidad, decena, centena, unidadmil]
    menorAMayor = sorted(numeroAOrdenar)
    mayorAMenor = menorAMayor[::-1]
    numeroOrdenado = str(mayorAMenor[0]) + str(mayorAMenor[1]) + str(mayorAMenor[2]) + str(mayorAMenor[3])

    return numeroOrdenado


def ordenarMenorMayor(num): #funcion que recibe un numero y ordena sus cifras de mayor a menor, retorna el numero ordenado

    unidad = int(num) % 10
    decena = int(num / 10) % 10
    centena = int(num / 100) % 10
    unidadmil = int(num / 1000)

    numeroAOrdenar = [unidad, decena, centena, unidadmil]
    menorAMayor = sorted(numeroAOrdenar)
    numeroOrdenado = str(menorAMayor[0]) + str(menorAMayor[1]) + str(menorAMayor[2]) + str(menorAMayor[3])

    return numeroOrdenado

def  rutinaKaprekar(casos, vectorNum):  #funcion para ejecutar la rutina de Kaprekar

    CONSTANTE_KAPREKAR = 6174

    for x in vectorNum:


        numeroParaOrdenar = x






def ingresaNumeroValido(casos):   #funcion para ingresar los numeros a comprobar

    numeros=[]  #vector de numeros

    while len(numeros)<casos:   #mientras falten numeros

        numNuevo = input("Ingrese un numero de 4 cifras, que tenga al menos 2 diferentes: ") #pide un numero

        if len(numNuevo) < 4:  #si el numero es menor de 4 cifras
            #revisa que por lo menos haya un numero diferente entre las 4 cifras
            unidad = numNuevo % 10
            decena = int(numNuevo / 10) % 10
            centena = int(numNuevo / 100) % 10
            unidadmil = int(numNuevo / 1000)

            if unidad == decena == centena == unidadmil:
                print("Numero erroneo. No se hallaron 2 cifras diferentes.")

            else:   #el numero cumple con todas las condiciones
                numeros.append(numNuevo)    #se agrega el numero al vector de numeros

        else:
            print("Número erroneo. No tiene 4 cifras.")
    #fin del while
    return numeros  #regresa el vector numeros una vez lleno

#Inicio del main

casosDePrueba = input("Ingrese el numero de casos de prueba: ") #solicita numero de caso de pruebas

numeros = ingresaNumeroValido(casosDePrueba)    #ejecuta funcion de carga de numeros

rutinaKaprekar(casosDePrueba, numeros)


def  rutinaKaprekar(casos, vectorNum):  #funcion para ejecutar la rutina de Kaprekar

    for x in vectorNum:
        unidad = x % 10
        decena = int(x / 10) % 10
        centena = int(x / 100) % 10
        unidadmil = int(x / 1000)

        numMayor =



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


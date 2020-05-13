from TP5.funciones.ordenar import *

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





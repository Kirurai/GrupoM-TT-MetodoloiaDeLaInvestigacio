from datos import pedirCantidadNumeros, pedirListaNumeros
from kaprekar import calcularCantidadDeVueltas

# Programa que calcula la cantidad de veces que un numero debe transormarse en la rutina de Kaprekar para llegar al numero 6174

rango = pedirCantidadNumeros()
listaIngresada = pedirListaNumeros(rango)

for numero in listaIngresada:
    vueltas = calcularCantidadDeVueltas(numero)
    print("La cantidad de vueltas para el numero {} es: {}".format(numero, vueltas))

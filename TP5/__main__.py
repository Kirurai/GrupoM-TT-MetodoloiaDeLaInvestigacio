from datos import pedirCantidadNumeros, pedirListaNumeros
from kaprekar import calcular_cantidad_vueltas

"""Programa que calcula la cantidad de veces que cada número de una lista de números positivos de 4 dígitos
debe transormarse en la rutina de Kaprekar para llegar al numero 6174.
 
"""
rango = pedirCantidadNumeros()
listaIngresada = pedirListaNumeros(rango)

for numero in listaIngresada:
    vueltas_necesarias = calcular_cantidad_vueltas(numero)
    print("La cantidad de vueltas para el numero {} es: {}".format(numero, vueltas_necesarias))

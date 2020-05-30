import numpy as np
from CalculadoraDiferenciales import Euler
import csv
import time


# S'(t) = - beta*S*I
# I'(t) = beta*S*I - mu*I
# R'(t) = mu*I

class SIR:

    def __init__(self, mu, beta, S0, I0, R0):

        #mu y beta son parametros de las diferenciales
        #mu es la probabilidad de un infectado de ser removido
        #beta es la probabilidad de infectar a un susceptible
        #S0, I0, R0 son los valores iniciales

        if isinstance(mu, (float, int)):
            #es numero?
            self.mu = lambda t: mu
        elif callable(mu):
            self.mu = mu

        if isinstance(beta, (float, int)):
            #es numero?
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        self.valores_iniciales = [S0, I0, R0]

    def __call__(self, u, t):
        S, I, R = u

        return np.asarray([
            -self.beta(t)*S*I, #Susceptibles
            self.beta(t)*S*I - self.mu(t)*I,    #Infectados
            self.mu(t)*I    #Removidos
        ])

if __name__ == "__main__":

    #SOLUCION MODELO SIR
    mu = 0.1       #probabilidad de ser removido (cura) de 0.0 a 20.0, valores mas altos hacen graficos divertidos y rompen el programa
    # beta = 0.001   #probabilidad de ser infectado (tasa de infeccion) de 0.0 a 0.01, valores mas grandes producen demasiados extremos
    s0 = 1500      #poblacion susceptible inicial
    i0 = 1         #poblacion infectada inicial
    r0 = 0         #poblacion recuperada inicial

    #QUE PASA SI LA TASA DE INFECCION DISMINUYE CON EL TIEMPO DEBIDO A MEDIDAS PREVENTIVAS? (comentar el beta de arriba)
    beta = lambda t: 0.001 if t <=10 else 0.0001    #en este caso decimos que a partir de los 10 dias se comienzan a aplicar medidas preventivas

    sir = SIR(mu, beta, s0, i0, r0)
    solucion = Euler(sir)
    solucion.definir_condiciones_iniciales(sir.valores_iniciales)

    saltos = 1001   #n° de saltos que genera
    dias = 60       #dias totales
    saltos_de_tiempo = np.linspace(0, dias, saltos) #De 0 a 60 dias
    u, t = solucion.resolver(saltos_de_tiempo)


    #EXTRAER DATOS A CSV

    #valores iniciales
    i = 0
    tiempo = t[0]
    sg = u[0, 0]
    ig = u[0, 1]
    rg = u[0, 2]


    fieldnames = ["tiempo", "S", "I", "R"]  # cabeceras de las columnas del csv

    with open('ValoresExperimento.csv', 'w') as csv_file:  # abre el archivo en modo write y escribe los headers
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while i<saltos-1:

        with open('ValoresExperimento.csv', 'a') as csv_file:  # abre el archivo en modo append
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)  # creamos un dictionary writer

            info = {  # escribimos el valor de cada columna
                "tiempo": tiempo,
                "S": sg,
                "I": ig,
                "R": rg
            }

            csv_writer.writerow(info)  # lo escribimos en cada columna
            # print(tiempo, sg, ig, rg)  # imprimimos en consola para tener feedback

            # finalmente actualizamos los valores
            i = i + 1
            tiempo = t[i]
            sg = u[i, 0]
            ig = u[i, 1]
            rg = u[i, 2]

        time.sleep(0.05)    #tocar para actualizar datos más rápido



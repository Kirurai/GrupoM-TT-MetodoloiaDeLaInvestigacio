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

            # Susceptibles
            -self.beta(t)*S*I,

            # Infectados
            self.beta(t)*S*I - self.mu(t)*I,

            # Removidos
            self.mu(t)*I
        ])

if __name__ == "__main__":

    #SOLUCION MODELO SIR
    # probabilidad de ser removido (cura) de 0.0 a 20.0, valores mas altos hacen graficos divertidos y rompen el programa
    mu = 0.1

    # probabilidad de ser infectado (tasa de infeccion) de 0.0 a 0.01, valores mas grandes producen demasiados extremos
    # beta = 0.001

    # QUE PASA SI LA TASA DE INFECCION DISMINUYE CON EL TIEMPO DEBIDO A MEDIDAS PREVENTIVAS? (comentar el beta de arriba)
    beta = lambda t: 0.001 if t <= 5 else 0.000001
    # en este caso decimos que a partir de los 10 dias se comienzan a aplicar medidas preventivas

    # poblacion susceptible inicial
    s0 = 1500

    # poblacion infectada inicial
    i0 = 1

    # poblacion recuperada inicial
    r0 = 0

    #seteo inicial
    sir = SIR(mu, beta, s0, i0, r0)
    solucion = Euler(sir)
    solucion.definir_condiciones_iniciales(sir.valores_iniciales)

    # n° de saltos que genera, 1000 es una buena cantidad
    saltos = 1001

    # dias totales
    dias = 60

    # Saltos de 0 a 60 dias
    saltos_de_tiempo = np.linspace(0, dias, saltos)

    #A RESOLVER!
    u, t = solucion.resolver(saltos_de_tiempo)


    #EXTRAER DATOS A CSV

    #valores iniciales
    i = 0
    tiempo = t[0]
    sg = u[0, 0]
    ig = u[0, 1]
    rg = u[0, 2]

    # cabeceras de las columnas del csv
    fieldnames = ["tiempo", "S", "I", "R"]

    # abre el archivo en modo write y escribe los headers
    with open('ValoresExperimento.csv', 'w') as csv_file:

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while i<saltos-1:

        # abre el archivo en modo append
        with open('ValoresExperimento.csv', 'a') as csv_file:

            # creamos un dictionary writer
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # escribimos el valor de cada columna
            info = {
                "tiempo": tiempo,
                "S": sg,
                "I": ig,
                "R": rg
            }

            # lo escribimos en cada columna
            csv_writer.writerow(info)

            # imprimimos en consola para tener feedback
            # print(tiempo, sg, ig, rg)

            # finalmente actualizamos los valores
            i = i + 1
            tiempo = t[i]
            sg = u[i, 0]
            ig = u[i, 1]
            rg = u[i, 2]

        time.sleep(0.05)    #tocar para actualizar datos más rápido



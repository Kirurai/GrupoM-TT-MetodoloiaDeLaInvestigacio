import numpy as np
from CalculadoraDiferenciales import Euler
import csv
import time
from datetime import datetime

'''
S'(t) = - beta*S*I
I'(t) = beta*S*I - mu*I
R'(t) = mu*I
'''


class SIR:

    def __init__(self, mu, beta, S0, I0, R0):

        """

        :param mu: parametro de la diferencial, probabilidad de ser removido
        :param beta: parametro de la diferencial, probabilidad de infectar a un susceptible
        :param S0: valor de susceptibles inicial
        :param I0: valor de infectados inicial
        :param R0: valor de removidos inicial
        """

        # ambos is instance nos permiten variar valores de beta y mu en funcion del tiempo
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


def modeloSIR(  mu_inicial,
                mu_final,
                mu_dias_cambio,
                beta_inicial,
                beta_final,
                beta_dias_cambio,
                s0,
                i0,
                r0,
                dias
                ):

    """
    :param mu_inicial: posibilidad incicial de curarse
    :param mu_final: posibilidad final de curarse
    :param mu_dias_cambio: dias para que se produzca el cambio de mu
    :param beta_inicial: posibilidad inicial de infectarse
    :param beta_final: posibilidad final de infectarse
    :param beta_dias_cambio: dias para que se produzca el cambio de beta
    :param s0: numero de susceptibles inicial
    :param i0: numero de infectados inicial
    :param r0: numero de removidos inicial
    :param dias: numero de dias del experimento
    :return:
    """

    #SOLUCION MODELO SIR

    # probabilidad de ser removido (cura) de 0.0 a 20.0, valores mas altos hacen graficos divertidos y rompen el programa
    # dejar comentado
    #mu = 0.1

    #SI APARECE UNA CURA E INCREMENTAN LAS POSIBILIDADES DE CURARSE (O SE INCREMENTA LA TASA DE MORTALIDAD)
    # mu_inicial = 0.1
    # mu_final = 0.1
    # mu_dias_cambio = 30
    mu = lambda t: mu_inicial if t <= mu_dias_cambio else mu_final

    # probabilidad de ser infectado (tasa de infeccion) de 0.0 a 0.01, valores mas grandes producen demasiados extremos
    # dejar comentado
    #beta = 0.001

    # QUE PASA SI LA TASA DE INFECCION DISMINUYE CON EL TIEMPO DEBIDO A MEDIDAS PREVENTIVAS?
    # beta_inicial = 0.00001
    # beta_final = 0.001
    # beta_dias_cambio = 10
    beta = lambda t: beta_inicial if t <= beta_dias_cambio else beta_final
    # en este caso decimos que a partir de los 10 dias se comienzan a aplicar medidas preventivas

    '''
    ATENCION, ENTRE LAS 3 INICIALES NO SUPERAR LOS 20000 DE POBLACION! EL CALCULO SE ROMPE!!!!!
    '''

    # poblacion susceptible inicial
    # s0 = 3000

    # poblacion infectada inicial
    # i0 = 1

    # poblacion recuperada inicial
    # r0 = 0

    #seteo inicial
    sir = SIR(mu, beta, s0, i0, r0)
    solucion = Euler(sir)
    solucion.definir_condiciones_iniciales(sir.valores_iniciales)

    # n° de saltos que genera, 1000 es una buena cantidad
    saltos = 1001

    # dias totales
    # dias = 60

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


            # escribimos el valor de cada columna, los valores SIR están redondeados, ya que al ser una integral, los
            # valores generados poseen muchos decimales, lo cual sería incorrecto para nuestro modelo, ya que no podemos
            # tener, por ejemplo, 20,324261212 pesonas infectadas.
            # el unico "defecto" de esto se produce si la población es muy pequeña, el grafico va a los saltos, pero
            # aunque se vea "feo" el gráfico es correcto...

            info = {
                "tiempo": tiempo,
                "S": round(sg, 0),
                "I": round(ig, 0),
                "R": round(rg, 0)
            }

            #registramos los datos finales del experimento
            if (i==saltos-2):
                datos = info

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

        # tocar para actualizar datos más rápido (OBSOLETO)
        #time.sleep(0.01)

    #almacenamos las variables del modelo en un diccionario
    variables_del_modelo = {
        "fecha_del_experimento": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "mu_inicial": mu_inicial,
        "mu_final": mu_final,
        "mu_dias_cambio": mu_dias_cambio,
        "beta_inicial": beta_inicial,
        "beta_final": beta_final,
        "beta_dias_cambio": beta_dias_cambio,
        "S0": s0,
        "I0": i0,
        "R0": r0
    }

    #unimos los diccionarios de variables y datos para obtener un diccionario de resultados del experimento actual
    resultados = {**variables_del_modelo, **datos}

    #registramos los datos del experimento actual en un csv donde se encuentra el histórico de los experimentos
    with open(r'Experimentos.csv', 'a', newline='') as csvfile:

        fieldnames = ["fecha_del_experimento",
                      "mu_inicial",
                      "mu_final",
                      "mu_dias_cambio",
                      "beta_inicial",
                      "beta_final",
                      "beta_dias_cambio",
                      "S0",
                      "I0",
                      "R0",
                      "tiempo",
                      "S",
                      "I",
                      "R"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow(resultados)


import numpy as np


class CalculadoraDiferenciales:

    def __init__(self, f):
        self.f = f

    def avanzar(self):  #Abstracta, hay que implementarla

        # Avanza en un paso
        raise NotImplementedError

    def definir_condiciones_iniciales(self, U0):

        if isinstance(U0, (int, float)):

            # ecuacion diferencial escalar
            self.numero_de_ecuaciones = 1
            U0 = float(U0)

        else:

            # sistema de ecuaciones
            U0 = np.asarray(U0)
            self.numero_de_ecuaciones = U0.size

        self.U0 = U0

    def resolver(self, saltos_de_tiempo):

        # almacena en arreglo t los saltos de tiempo
        self.t = np.asarray(saltos_de_tiempo)
        # n es el tamaño del vector, osea la cantidad de saltos
        n = self.t.size

        # almacena en u un arreglo de cantidad de saltos de tiempo por el numero de ecuaciones
        self.u = np.zeros((n, self.numero_de_ecuaciones))

        # establece los valores iniciales en el vector respuesta u
        self.u[0, :] = self.U0

        # Se resuelve la integral y devuelve los resultados obtenidos al vector u y al vector t
        for i in range(n - 1):
            self.i = i
            self.u[i + 1] = self.avanzar()

        return self.u[:i + 2], self.t[:i + 2]

class Euler(CalculadoraDiferenciales):  #resolver diferencial mediante Euler

    def avanzar(self):
        # soluciones
        u = self.u

        # funcion
        f = self.f

        # salto tiempo
        i = self.i

        # rango de tiempo completo
        t = self.t

        #diferencial tiempo
        dt = t[i + 1] - t[i]

        # para todas las ecuaciones en i, queremos multiplicar la funcion por un dt, que es un pequeño salto en el
        # tiempo
        return u[i, :] + dt * f(u[i, :], t[i])

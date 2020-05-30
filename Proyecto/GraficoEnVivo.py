import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")


def animar(i):
    data = pd.read_csv('ValoresExperimento.csv')
    t = data['tiempo']
    s = data['S']
    i = data['I']
    r = data['R']

    plt.cla()

    # plt.plot(t, u[:, 0], label="Susceptibles")
    # plt.plot(t, u[:, 1], label="Infectados")
    # plt.plot(t, u[:, 2], label="Removidos")

    plt.plot(t, s, label="Susceptibles")
    plt.plot(t, i, label="Infectados")
    plt.plot(t, r, label="Removidos")

    plt.legend(loc="best")

    plt.title('Modelo SIR')
    plt.xlabel('Dias')
    plt.ylabel('Población')

    plt.tight_layout()

# GRAFICO


ani = FuncAnimation(plt.gcf(),
                    animar,
                    interval=50,    #velocidad de actualizacion del grafico
                    #frames=100,    #cantidad de frames que dura la actualizacion del grafico, no es necesario, pero
                    # sino sigue reproduciendose por lo que no se puede hacer zoom, consume recursos y si intentas
                    # mover la ventana se lagguea horrendamente
                    repeat=False)

plt.tight_layout()

plt.show()
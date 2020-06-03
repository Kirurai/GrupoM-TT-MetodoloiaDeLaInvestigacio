import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

#podemos definir diferentes estilos de gráficos, se pueden ver todos en este link
# https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html
plt.style.use("fivethirtyeight")


def animar(i):

    #csv del cual leer los datos
    data = pd.read_csv('ValoresExperimento.csv')

    #asignamos a una variable los valores de cada columna
    #valores de tiempo
    t = data['tiempo']

    #valores de Susceptibles
    s = data['S']

    #valores de Infectados
    i = data['I']

    #valores de Removidos
    r = data['R']

    #limpia el gráfico en cada actualización para evitar errores gráficos
    plt.cla()

    #creamos el plot del gráfico de Susceptibles
    plt.plot(t, s, label="Susceptibles")

    # creamos el plot del gráfico de Infectados
    plt.plot(t, i, label="Infectados")

    # creamos el plot del gráfico de Removidos
    plt.plot(t, r, label="Removidos")

    #colocamos el cuadro con los nombres de cada curva, se acomoda automáticamenete a la mejor posición disponible,
    #se puede colocar en un lugar fijo, pero funciona mejor así
    plt.legend(loc="best")


    #titulo del gráfico
    plt.title('Modelo SIR')

    #nombre del eje x
    plt.xlabel('Dias')

    #nombre del eje y
    plt.ylabel('Población')

    #tight layout aumenta la compatibilidad con monitores de menores resoluciones, para que no se produzcan glitches
    #gráficos ni errores, es una buena práctica incluírlo
    plt.tight_layout()

# GRAFICO


ani = FuncAnimation(plt.gcf(),
                    animar,
                    #velocidad de actualizacion del grafico
                    interval=100,
                    #cantidad de frames que dura la actualizacion del grafico, no es necesario, pero
                    # sino sigue reproduciendose por lo que no se puede hacer zoom, consume recursos y si intentas
                    # mover la ventana se lagguea horrendamente
                    #frames=100,
                    repeat=False)

#volvemos a llamar a tight layout solo por si acaso
plt.tight_layout()

#mostramos el gráfico
plt.show()
#import serial
from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


root = Tk()
root.geometry('1000x400')
root.title('This is my root window')
#root.state('zoomed')
root.config(background='#fafafa')

xar = []
yar = []

style.use('ggplot')
fig = plt.figure(figsize=(10, 3.2), dpi=100)
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylim(0, 100)
line, = ax1.plot(xar, yar, 'r', marker='o')

def animar(j):

    #csv del cual leer los datos
    data = pd.read_csv('ValoresExperimento.csv')

    #asignamos a una variable los valores de cada columna
    #valores de tiempo, suceptibles, infectados y removidos
    t = data['tiempo']
    s = data['S']
    i = data['I']
    r = data['R']

    #limpia el gráfico en cada actualización para evitar errores gráficos
    plt.cla()

    #creamos los plots de los gráficos
    plt.plot(t, s, label="Susceptibles")
    plt.plot(t, i, label="Infectados")
    plt.plot(t, r, label="Removidos")

    #colocamos el cuadro con los nombres de cada curva, se acomoda automáticamenete a la mejor posición disponible,
    #se puede colocar en un lugar fijo, pero funciona mejor así
    plt.legend(loc="best")


    #titulo del gráfico, y nombre de ejes
    plt.title('Modelo SIR')
    plt.xlabel('Dias')
    plt.ylabel('Población')

    #tight layout aumenta la compatibilidad con monitores de menores resoluciones, para que no se produzcan glitches
    #gráficos ni errores, es una buena práctica incluírlo
    plt.tight_layout()

    #Con esto rellenamos el area entre los gráficos, para este gráfico vamos a rellenar el área entre los infectados
    #y los susceptibles, en caso que los susceptibles sean más que los infectados, la zona va a ser azul, de lo
    #contrario va a ser roja

    plt.fill_between(t,  # eje x
                     s,  # eje y
                     i,  # es el segundo eje y
                     where=(s > i),  # esto determina desde donde hasta donde se hace el relleno
                     interpolate=True,
                     # esto evita q ciertas intersecciones se cruzen, y que todas las regiones se rellenen correctamente
                     alpha=0.25,
                     color="blue",
                     label="Mayoría de población sana")  # alpha nos permite hacer transparente el relleno

    plt.fill_between(t,  # eje x
                     s,  # eje y
                     i,  # es el segundo eje y
                     where=(s <= i),  # esto determina desde donde hasta donde se hace el relleno
                     interpolate=True,
                     # esto evita q ciertas intersecciones se cruzen, y que todas las regiones se rellenen correctamente
                     alpha=0.25,
                     color="red",
                     label="Mayoría de población infectada")  # alpha nos permite hacer transparente el relleno


    plt.legend()


plotcanvas = FigureCanvasTkAgg(fig, root)
plotcanvas.get_tk_widget().grid(column=1, row=1)
ani = animation.FuncAnimation(fig, animar, interval=10, blit=False)

root.mainloop()
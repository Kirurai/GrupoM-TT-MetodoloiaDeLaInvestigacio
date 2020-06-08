import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

#podemos definir diferentes estilos de gráficos, se pueden ver todos en este link
# https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html

def ejecutarGrafico():
    plt.style.use("fivethirtyeight")
    data = pd.read_csv('ValoresExperimento.csv')

    tData = data['tiempo']
    sData = data['S']
    iData = data['I']
    rData = data['R']

    t = []
    s = []
    i = []
    r = []

    def animar(j):

        # #csv del cual leer los datos
        # data = pd.read_csv('ValoresExperimento.csv')
        #
        # #asignamos a una variable los valores de cada columna
        # #valores de tiempo, suceptibles, infectados y removidos
        # t = data['tiempo']
        # s = data['S']
        # i = data['I']
        # r = data['R']
        for x in range(0, 10):
             t.append(tData[j*10+x])
             s.append(sData[j*10+x])
             i.append(iData[j*10+x])
             r.append(rData[j*10+x])

        # t.append(tData[j])
        # s.append(sData[j])
        # i.append(iData[j])
        # r.append(rData[j])
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

    # GRAFICO


    ani = FuncAnimation(plt.gcf(),
                        animar,
                        #velocidad de actualizacion del grafico
                        interval=1,
                        #cantidad de frames que dura la actualizacion del grafico, no es necesario, pero
                        # sino sigue reproduciendose por lo que no se puede hacer zoom, consume recursos y si intentas
                        # mover la ventana se lagguea horrendamente
                        frames=100,
                        repeat=False)

    #volvemos a llamar a tight layout solo por si acaso
    plt.tight_layout()

    #mostramos el gráfico
    plt.show()
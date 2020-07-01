import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

from subprocess import Popen
from tkinter.messagebox import showinfo

from GraficoEnVivo import ejecutarGrafico
from SIR import modeloSIR

LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 8)


class VentanaPrincipal(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Proyecto Grupo M - TT")
        self.iconphoto(True, tk.PhotoImage(file='imagenes/SIR.png'))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = EditarParametros(container, self)
        self.frames[EditarParametros] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(EditarParametros)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class EditarParametros(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Edicion de parametros", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        # label.grid(column=1, row=0, padx=10, pady=10)

        labelframe = tk.LabelFrame(self)
        labelframe.pack(fill="both", expand="yes")
        labelInicial = tk.Label(labelframe, text="Valor Inicial", font=SMALL_FONT)
        labelInicial.grid(column=1, row=1, padx=20, pady=10)
        labelFinal = tk.Label(labelframe, text="Valor Final", font=SMALL_FONT)
        labelFinal.grid(column=2, row=1, padx=20, pady=10)
        labelDiasDeCambio = tk.Label(labelframe, text="Dias de Cambio", font=SMALL_FONT)
        labelDiasDeCambio.grid(column=3, row=1, padx=20, pady=10)

        labelmu = tk.Label(labelframe, text="Probabilidad de Remocion", font=SMALL_FONT)
        labelmu.grid(column=0, row=2, padx=20, pady=10)
        sbMuInicial = ttk.Spinbox(labelframe, from_=0.001, to=1, increment=0.01, width=10, state='readonly')
        sbMuInicial.set(0.1)
        sbMuInicial.grid(column=1, row=2, padx=20, pady=10)
        sbMuFinal = ttk.Spinbox(labelframe, from_=0.001, to=1, increment=0.01, width=10, state='readonly')
        sbMuFinal.set(0.1)
        sbMuFinal.grid(column=2, row=2, padx=20, pady=10)
        sbMuDiasDeCambio = ttk.Spinbox(labelframe, from_=0, to=60, increment=1, width=10, state='readonly')
        sbMuDiasDeCambio.set(30)
        sbMuDiasDeCambio.grid(column=3, row=2, padx=20, pady=10)

        labelBeta = tk.Label(labelframe, text="Probabilidad de Infeccion", font=SMALL_FONT)
        labelBeta.grid(column=0, row=3, padx=20, pady=10)
        sbBetaInicial = ttk.Spinbox(labelframe, from_=0.0001, to=0.001, increment=0.0001, width=10, state='readonly')
        sbBetaInicial.set(0.00001)
        sbBetaInicial.grid(column=1, row=3, padx=20, pady=10)
        sbBetaFinal = ttk.Spinbox(labelframe, from_=0.0001, to=0.001, increment=0.0001, width=10, state='readonly')
        sbBetaFinal.set(0.001)
        sbBetaFinal.grid(column=2, row=3, padx=20, pady=10)
        sbBetaDiasDeCambio = ttk.Spinbox(labelframe, from_=0, to=60, increment=1, width=10, state='readonly')
        sbBetaDiasDeCambio.set(10)
        sbBetaDiasDeCambio.grid(column=3, row=3, padx=20, pady=10)

        labelPoblacion = tk.Label(labelframe, text="Poblacion Inicial", font=SMALL_FONT)
        labelPoblacion.grid(column=0, row=5, padx=20, pady=10)

        labelS = tk.Label(labelframe, text="Suceptibles", font=SMALL_FONT)
        labelS.grid(column=1, row=4, padx=20, pady=10)
        sbS = ttk.Spinbox(labelframe, from_=1, to=15000, increment=10, width=10, state='readonly')
        sbS.set(3000)
        sbS.grid(column=1, row=5, padx=20, pady=10)

        labelI = tk.Label(labelframe, text="Infectados", font=SMALL_FONT)
        labelI.grid(column=2, row=4, padx=20, pady=10)
        sbI = ttk.Spinbox(labelframe, from_=1, to=1000, increment=1, width=10, state='readonly')
        sbI.set(1)
        sbI.grid(column=2, row=5, padx=20, pady=10)
        ''' #Quitados los recuperados, para darl emas jeugo a los otros dos
        labelR = tk.Label(labelframe, text="Recuperados", font=SMALL_FONT)
        labelR.grid(column=3, row=4, padx=20, pady=10)
        sbR = ttk.Spinbox(labelframe, from_=0, to=20000, increment=1, width=10, state='readonly')
        sbR.set(0)
        sbR.grid(column=3, row=5, padx=20, pady=10)
        '''
        button = ttk.Button(self, text="Cargar parametros",
                            command=lambda: cargarParametros(float(sbMuInicial.get()), float(sbMuFinal.get()),
                                                      float(sbMuDiasDeCambio.get()), float(sbBetaInicial.get()),
                                                      float(sbBetaFinal.get()), float(sbBetaDiasDeCambio.get()),
                                                      float(sbS.get()), float(sbI.get())))


        button.pack()

        button2 = ttk.Button(self, text="Graficar!",
                             command=lambda: ejecutarGrafico())
        button2.pack()

        button3 = ttk.Button(self, text="Valores por defecto",
                             command=lambda: valoresDefecto(sbMuInicial, sbMuFinal, sbMuDiasDeCambio, sbBetaInicial,
                                                            sbBetaFinal, sbBetaDiasDeCambio, sbS, sbI, 0))
        button3.pack()

        button4 = ttk.Button(self, text="Mas detalles",
                             command=lambda: abrir_csv('ValoresExperimento.csv'))
        button4.pack()

        button5 = ttk.Button(self, text="Historico",
                             command=lambda: abrir_csv('Experimentos.csv'))
        button5.pack()

def valoresDefecto(sbMuInicial, sbMuFinal, sbMuDiasDeCambio, sbBetaInicial, sbBetaFinal, sbBetaDiasDeCambio, sbS, sbI,
                   sbR):
    sbMuInicial.set(0.1)
    sbMuFinal.set(0.1)
    sbMuDiasDeCambio.set(30)
    sbBetaInicial.set(0.00001)
    sbBetaFinal.set(0.001)
    sbBetaDiasDeCambio.set(10)
    sbS.set(3000)
    sbI.set(1)
    #sbR.set(0)

def abrir_csv(csv):
    p = Popen(csv, shell=True)

def cargarParametros(sbMuInicial, sbMuFinal, sbMuDiasDeCambio, sbBetaInicial, sbBetaFinal, sbBetaDiasDeCambio, sbS, sbI):
    modeloSIR(sbMuInicial, sbMuFinal, sbMuDiasDeCambio, sbBetaInicial, sbBetaFinal, sbBetaDiasDeCambio, sbS, sbI, 0, 60)
    showinfo("Exito!", "Parametros cargados!")

app = VentanaPrincipal()
app.mainloop()


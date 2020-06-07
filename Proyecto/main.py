import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

from GraficoEnVivo import ejecutarGrafico
from SIR import modeloSIR

LARGE_FONT = ("Verdana", 12)


class VentanaPrincipal(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Proyecto Grupo M - TT")

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
        label = tk.Label(self, text="Edición de parametros", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Cargar parametros",
                            command=lambda: controller.show_frame(EditParameters))
        button.pack()

        button2 = ttk.Button(self, text="Graficar!",
                             command=lambda: ejecutarGrafico())
        button2.pack()






app = VentanaPrincipal()
app.mainloop()



#modeloSIR(0.1, 0.1, 30, 0.00001, 0.001, 10, 3000, 1, 0, 60)
# mu_inicial = 0.1
# mu_final = 0.1
# mu_dias_cambio = 30
# beta_inicial = 0.00001
# beta_final = 0.001
# beta_dias_cambio = 10
######Poblaciones iniciales
# s0 = 3000
# i0 = 1
# r0 = 0
# dias = 60
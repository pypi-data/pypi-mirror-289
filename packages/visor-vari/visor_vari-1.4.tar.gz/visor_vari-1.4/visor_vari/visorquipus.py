
""" Ventana principal del visor de variables """


"========================================================"

import tkinter as tk
#visor_vari
from visor_vari.mas_bajo_nivel.variables_valores import ini
from visor_vari.control import ver_registro

"========================================================"

class E_lenguaje_quipus:

    "......... Inicializando .........."

    def __init__(self):
        
        self.iniciotekinte()

    def iniciotekinte(self):

        self.edit_text= tk.Tk()
        ini.objeto_tk= self.edit_text
        self.edit_text.geometry("200x25")
        self.edit_text.title ("diseñemos programas")

        self.primer_marco= tk.LabelFrame(self.edit_text, bd= 0)
        self.primer_marco.pack(expand= True, fill= tk.BOTH)

        self.boton_muestra()

        self.edit_text.mainloop()
    
    def boton_muestra (self):
        
        self.panel_control= tk.LabelFrame(self.primer_marco)
        self.panel_control.pack(anchor= "w")

        boton_para_crear_nuevo_carapter= tk.Button (self.panel_control, text= "mostrar carapteres", command= ver_registro)
        boton_para_crear_nuevo_carapter.config(padx= 24)
        boton_para_crear_nuevo_carapter.pack ()

def gentil():
    E_lenguaje_quipus()


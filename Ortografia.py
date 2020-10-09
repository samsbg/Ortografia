#Autor: Samantha Bautista
#Matricula: A01284462
#Campus: Monterrey
#Fecha: 28 de septiembre de 2020
#Actividad: Proyecto final PISA: ortografia

from tkinter import *
import tkinter as tk
from random import randint
import os

ort = tk.Tk()
ort.title("Ortografía")
ort.geometry("900x500")
ort.resizable(width=False, height=False)
ort.configure(bg="#E4ADBC")


def segundaPagina(b, listaCorrecta, listaIncorrecta):

    global intPuntaje

    titulo.grid(column=2, row=0, columnspan=16, sticky="WNS")

    opcion1 = tk.Button(font=("Avenir Next LT Pro Light (Headings)", 20))
    opcion2 = tk.Button(font=("Avenir Next LT Pro Light (Headings)", 20))

    def comandoSiguiente():
        global intPuntaje
        if intPuntaje == 500:
            regresar()
        else:
            opcion1.grid_forget()
            opcion2.grid_forget()
            creacionDeBotones()

    siguiente = tk.Button(text="Siguiente", bg="#B13B5B", command=comandoSiguiente, font=("Avenir Next LT Pro Light (Headings)", 20), state=DISABLED)
    siguiente.grid(column=14, row=9, columnspan=4, sticky="NSWE", padx=10, pady=10)

    puntaje = tk.Label(text="{}/150".format(intPuntaje),
                       bg="#E4ADBC", font=(None, 20))
    puntaje.grid(column=14, row=2, sticky="E", columnspan=4, padx=10)

    instruccion = tk.Label(text="Selecciona la manera correcta \n de escribir la palabra",
                           bg="#E4ADBC", font=("Avenir Next LT Pro Light (Headings)", 20))
    instruccion.grid(column=4, row=4, columnspan=10, rowspan=2, sticky="NSWE")

    def creacionDeBotones():

        intPalabra = randint(0, (len(listaCorrecta)-1)//2)
        intPosicion = randint(0, 1)

        if (intPosicion == 0):
            opcionPalabra1 = listaCorrecta[intPalabra*2+1]
            opcionPalabra2 = listaIncorrecta[intPalabra*2+1]
        elif (intPosicion == 1):
            opcionPalabra1 = listaIncorrecta[intPalabra*2+1]
            opcionPalabra2 = listaCorrecta[intPalabra*2+1]

        def comandoOpcion(boton):

            global intPuntaje

            if(intPosicion == 0 and boton == 1) or (intPosicion == 1 and boton == 2):
                if(boton == 1):
                    opcion1.configure(bg="green")
                    opcion2.configure(state=DISABLED)

                elif(boton == 2):
                    opcion2.configure(bg="green")
                    opcion1.configure(state=DISABLED)
                intPuntaje = intPuntaje + 10
                listaCorrecta.pop(intPalabra*2)
                listaCorrecta.pop(intPalabra*2)
                listaIncorrecta.pop(intPalabra*2)
                listaIncorrecta.pop(intPalabra*2)
            else:
                if(boton == 1):
                    opcion1.configure(bg="red")
                    opcion2.configure(state=DISABLED)
                elif(boton == 2):
                    opcion2.configure(bg="red")
                    opcion1.configure(state=DISABLED)
                intPuntaje = intPuntaje - 10
                listaCorrecta.append(listaCorrecta[intPalabra*2])
                listaCorrecta.append(listaCorrecta[intPalabra*2+1])
                listaIncorrecta.append(listaIncorrecta[intPalabra*2])
                listaIncorrecta.append(listaIncorrecta[intPalabra*2+1])

            string_Correcto = ""
            string_Incorrecto = ""

            for n in range(len(listaCorrecta)):
                string_Correcto = string_Correcto + listaCorrecta[n] + " "
                string_Incorrecto = string_Incorrecto + \
                    listaIncorrecta[n] + " "

            puntaje.grid_forget()
            puntaje.configure(text="{}/500".format(intPuntaje))
            puntaje.grid(column=14, row=2, sticky="E", columnspan=4, padx=10)
            siguiente.configure(state=NORMAL)

            with open(os.path.abspath("OrtografiaTexto.txt"), 'r',  encoding='utf-8-sig') as f:
                listaDeLineas = f.readlines()
                listaDeLineas[b] = string_Correcto + "\n"
                listaDeLineas[b+8] = string_Incorrecto + "\n"
                puntajesTexto = listaDeLineas[16].split()
                puntajesTexto[b] = str(intPuntaje)


            stringCambio = ""

            for k in puntajesTexto:
                stringCambio = stringCambio + k + " "
            
            listaDeLineas[16] = stringCambio

            with open(os.path.abspath("OrtografiaTexto.txt"), 'w',  encoding='utf-8-sig') as f:
                f.writelines(listaDeLineas)

        opcion1.configure(text=opcionPalabra1, bg="#B13B5B",
                          command=lambda: comandoOpcion(1), state=NORMAL)
        opcion1.grid(column=4, row=7, columnspan=4, sticky="NSWE")

        opcion2.configure(text=opcionPalabra2, bg="#B13B5B",
                          command=lambda: comandoOpcion(2), state=NORMAL)
        opcion2.grid(column=10, row=7, columnspan=4, sticky="NSWE")

        siguiente.configure(state=DISABLED)

    creacionDeBotones()

    def regresar():
        opcion1.grid_forget()
        opcion2.grid_forget()
        puntaje.grid_forget()
        instruccion.grid_forget()
        siguiente.grid_forget()
        primeraPagina()

    regreso.grid(column=0, row=0, columnspan=2, sticky="NSWE")
    regreso.configure(command=regresar)

    for y in range(10):
        ort.grid_rowconfigure(y, weight=1)

    for x in range(18):
        ort.grid_columnconfigure(x, weight=1)


def primeraPagina():
    global boton
    global listaCorrecta
    global listaIncorrecta
    global intPuntaje

    titulo.grid(column=1, row=0, columnspan=5, sticky="WNS")

    def regresar():
        print("Pagina principal")
        ort.destroy()

    regreso.grid(column=0, row=0, sticky="NSWE")
    regreso.configure(command=regresar)

    setLabel = tk.Label(text="Sets", bg="#E4ADBC", font=(None, 20))
    setLabel.grid(column = 2, row =2, columnspan = 2, rowspan = 2)

    def opciones(i):

        global intPuntaje

        for x in range(8):
            listaOpciones[x].grid_forget()
            puntajesLabels[x].grid_forget()
            setLabel.grid_forget()

        correctoString = []
        incorrectoString = []

        with open(os.path.abspath("OrtografiaTexto.txt"), 'r',  encoding='utf-8-sig') as f:
            for x in range(8):
                correctoString.append(f.readline())
            for x in range(8):
                incorrectoString.append(f.readline())

        listaCorrecta = correctoString[i].split()
        listaIncorrecta = incorrectoString[i].split()

        intPuntaje = int(puntajes[i])

        segundaPagina(i, listaCorrecta, listaIncorrecta)

    listaOpciones = []
    puntajesLabels = []

    with open(os.path.abspath("OrtografiaTexto.txt"), 'r',  encoding='utf-8-sig') as f:
        for i in range(16):
            f.readline()
        puntajes = f.readline().split()
    
    for i in range(8):
        listaOpciones.append(tk.Button(text=("Opción", i+1), font=(None, 15), bg="#B13B5B", fg="white", command=lambda i=i: opciones(i)))
        listaOpciones[i].grid(column=(1 + (i % 2)*2), row=(4 + (i//2)*2))

        puntajesLabels.append(
            tk.Label(text="{}/500".format(puntajes[i]), font=(None, 15), bg="#E4ADBC"))
        puntajesLabels[i].grid(column=(2 + (i % 2)*2), row=(4 + (i//2)*2), sticky="EW")

        if(puntajes[i] == 500):
            listaOpciones.configure(state = DISABLED)

    for y in range(11):
        ort.grid_rowconfigure(y, weight=1)

    for x in range(6):
        ort.grid_columnconfigure(x, weight=1)


regreso = tk.Button(text=" 🡄 ", bg="#B13B5B", fg="white", font=(None, 20))
titulo = tk.Label(text="Ortografía", bg="#B13B5B", fg="white", font=(None, 20), width=60)

intPuntaje = 0
boton = 0
listaCorrecta = []
listaIncorrecta = []

primeraPagina()

ort.mainloop()

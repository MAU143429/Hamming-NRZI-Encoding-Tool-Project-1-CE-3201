from cgitb import text
from tkinter import *
from tkinter import messagebox
from conversiones import *
from GUI import *


# Ventana


class inter_usuario:
    def __init__(self):  # El self se usa para hacen mención de los atributos
        self.interfaz = Tk()  # interfaz es el objeto tipo tkinter
# Parámetro de la interfaz
        self.interfaz.title("Interfaz de usuario")
        self.interfaz.geometry("800x500")

        self.binario = ""
        self.decimal = ""
        self.hexadecimal = ""
        self.paridad = ""

# Datos de usuario
        # Mensaje al usuario
        self.label1 = Label(
            self.interfaz, text="Ingrese un numero octal entre 0000 y 7777")
        self.label1.place(x=20, y=20)
        # Cuadro para ingresar el numero octal
        self.text1 = Entry(self.interfaz)
        self.text1.place(x=250, y=20)

        self.lparidad = Label(
            self.interfaz, text="Ingrese la paridad (par o impar)")
        self.lparidad.place(x=20, y=50)
        # Cuadro para ingresar la paridad
        self.tparidad = Entry(self.interfaz)
        self.tparidad.place(x=250, y=50)


# Opciones para el usuario
        # Texto de eleccion de botones
        self.label2 = Label(self.interfaz, text="Resultado de Conversiones")
        self.label2.place(x=175, y=90)

        self.frame1 = Frame(self.interfaz)
        self.frame1.pack()
        # Botones
        self.btn0 = Button(self.interfaz, text="Aceptar",command=self.leerDato)
        self.btn0.place(x=400, y=45)

        self.lbinario = Label(self.interfaz, text="Binario")
        self.lbinario.place(x=100, y=120)

        self.l2binario = Label(self.interfaz, text="")
        self.l2binario.place(x=100, y=140)

        self.ldecimal = Label(self.interfaz, text="Decimal")
        self.ldecimal.place(x=200, y=120)

        self.l2decimal = Label(self.interfaz, text="")
        self.l2decimal.place(x=200, y=140)

        self.lhexadecimal = Label(self.interfaz, text="Hexadecimal")
        self.lhexadecimal.place(x=300, y=120)

        self.l2hexadecimal = Label(self.interfaz, textvariable="")
        self.l2hexadecimal.place(x=300, y=140)

        self.btn3 = Button(
            self.interfaz, text="Generar Tablas Hamming", command=self.generateHamming)
        self.btn3.place(x=20, y=200)

        self.btn4 = Button(self.interfaz, text="NRZI",command=self.generateNRZI)
        self.btn4.place(x=20, y=250)

        self.interfaz.mainloop()

    def leerDato(self):

        octal = self.text1.get()
        paridad = self.tparidad.get()
        self.paridad = paridad
        resultado = recibeoctal(int(octal))
        self.binario = resultado[0]
        self.decimal = resultado[1]
        self.hexadecimal = resultado[2]
        self.l2binario.config(text=resultado[0])
        self.l2decimal.config(text=resultado[1])
        self.l2hexadecimal.config(text=resultado[2])

    def generateHamming(self):
        hamming = hammingTables(5, self.binario, self.paridad)

    def generateNRZI(self):
        nrziDisplay(self.binario)


objeto_interfaz = inter_usuario()

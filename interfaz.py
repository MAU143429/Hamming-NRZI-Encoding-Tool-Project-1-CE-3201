from tkinter import *
from tkinter import messagebox

#Ventana

class inter_usuario:
    def  __init__ (self): #El self se usa para hacen mención de los atributos
        interfaz = Tk() #interfaz es el objeto tipo tkinter
#Parámetro de la interfaz
        interfaz.title("Interfaz de usuario")
        interfaz.geometry("500x250")

#Datos de usuario
        #Mensaje al usuario
        self.label1 = Label(interfaz, text = "Ingrese un numero octal entre 0000 y 7777")
        self.label1.place(x=20, y=20)
        #Cuadro para ingresar el numero octal
        self.text1 = Entry(interfaz)
        self.text1.place(x=255, y=20)
        
        
#Opciones para el usuario
        #Texto de eleccion de botones        
        self.label2 = Label(interfaz, text = "Menu de opciones")
        self.label2.place(x=175, y=55)
        
        #Botones
        self.btn0 = Button(interfaz, text = "Aceptar")
        self.btn0.place(x=400, y=20)
        
        self.bt1 = Button(interfaz, text = "Conversion a Binaria")
        self.bt1.place(x=20, y=80)
       
        self.btn2 = Button(interfaz, text = "Conversion a Decimal")
        self.btn2.place(x=20, y=110)
        
        self.btn3 = Button(interfaz, text = "Conersion a Hexadecimal" )
        self.btn3.place(x=20, y=140)
        
        self.btn4 = Button(interfaz, text = "NRZI")
        self.btn4.place(x=20, y=170)

        interfaz.mainloop() 


objeto_interfaz = inter_usuario()


import matplotlib.pyplot as plt
import numpy as np

#solicitar los datos
def recibeoctal():
    try:
        octal = int(input("Ingrese un número octal entre 0000 y 7777: "))
        #paridad =str(input("Ingrese el tipo de paridad que desea: par o impar. ")).lower()

        if 0 <= octal < 7778: 

            Decimal = octal_decimal(str(octal))
            Binario = decimal_binario(octal_decimal(str(octal)))
            Hexadecimal = decimal_hex(octal_decimal(str(octal)))

            print(Decimal, Binario, Hexadecimal)

            data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(len(Binario)):
                data[13 - len(Binario) + i] = int(Binario[i])

            nrz_I(data)
            
        else:
           print("Datos inválidos, favor intentelo nuevamente")
        recibeoctal() 

    except:
        print("Ha ocurrido un error, favor intentelo nuevamente")
        recibeoctal()
        
#realizar las conversiones 
#Decimal 
def octal_decimal(octal):
    decimal = 0 
    posicion = 0
    octal = octal[::-1]
    for i in octal:
        valor_int = int(i)
        numero_elevado = int(8** posicion)
        equivalencia = int(numero_elevado * valor_int)
        decimal += equivalencia
        posicion += 1
    return decimal

#Binario 
def decimal_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while int(decimal)>0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario 

#Hexadecimal:
def caracteres_hex(valor):
    dato = str(valor)
    lista = {"10":"A", "11":"B", "12":"C","13":"D", "14":"E", "15":"F", "16":"F"}
    if dato in lista:
        return lista[dato]
    else:
        return dato 

def decimal_hex(decimal):
    hex = ""
    while decimal > 0:
        residuo = decimal % 16
        caracter = caracteres_hex(residuo)
        hex= caracter + hex
        decimal = int(decimal/16)
    return hex
  
#crear función nrz-i
def nrz_I(data):
    data_nrz_i = []
    estado = False
    for i in range(len(data)):
        x = None
        if data[i] == 1 and estado == False:
            x = -1
            estado = True
        elif data[i] == 1 and estado == True:
            x = 1
            estado = False
        elif data[i] == 0 and estado == True:
            x = -1
        elif data[i] == 0 and estado == False:
            x = 1
        data_nrz_i.append(x)

    if data_nrz_i[0] == 0:
        data_nrz_i[0] = 1
    data_nrz_i.append(1)
    xs = np.repeat(range(len(data_nrz_i)), 2)
    ys = np.repeat(data_nrz_i,2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.title("NRZI")
    plt.xlabel(str(data))
    plt.plot(xs,ys)
    plt.ylim(-1.5,1.5)
    plt.xlim(0,14)
    plt.show()


recibeoctal()

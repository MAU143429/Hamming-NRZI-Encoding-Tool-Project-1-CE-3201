#Proyecto 1
#solicitar los datos 


def recibeoctal():
    try:
        octal = int(input("Ingrese un número octal entre 0000 y 777: "))
        paridad =str(input("Ingrese el tipo de paridad que desea: par o impar. ")).lower()

        if 0 <= octal < 777: 
            print("Octal: ", octal)
            print("Decimal", octal_decimal(str(octal)))

            #De aquí se puede tomar el binario 
            print("Binario", decimal_binario(octal_decimal(str(octal))))

            print("Hexadecimal", decimal_hex(octal_decimal(str(octal))))

            print(paridad)
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

recibeoctal()
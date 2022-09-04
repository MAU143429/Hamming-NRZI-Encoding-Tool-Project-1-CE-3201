# Imports
import numpy as np


# Functions of hamming code-------------------------------------------
def emitterConverter(sizePar, data, paridad):
    """
    :param sizePar: how many parity bits the message must have
    :param data:  information bits
    :return: message to be transmitted by unreliable medium
            - bits of information merged with parity bits

    >>> emitterConverter(4, "101010111111")
    ['1', '1', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '1', '1']
    """
    if sizePar + len(data) <= 2 ** (sizePar-1) - (len(data) - 1):
        print("ERROR - size of parity don't match with size of data")
        exit(0)

    dataOut = []
    parity = []
    binPos = [bin(x)[2:] for x in range(1, sizePar + len(data) + 1)]

    # sorted information data for the size of the output data
    dataOrd = []
    # data position template + parity
    dataOutGab = []
    # parity bit counter
    qtdBP = 0
    # counter position of data bits
    contData = 0

    for x in range(1, sizePar + len(data) + 1):
        # Performs a template of bit positions - who should be given,
        # and who should be parity
        if qtdBP < sizePar:
            if (np.log(x) / np.log(2)).is_integer():
                dataOutGab.append("P")
                qtdBP = qtdBP + 1
            else:
                dataOutGab.append("D")
        else:
            dataOutGab.append("D")

        # Sorts the data to the new output size
        if dataOutGab[-1] == "D":
            dataOrd.append(data[contData])
            contData += 1
        else:
            dataOrd.append(None)

    # print(dataOutGab)
    # Calculates parity
    qtdBP = 0  # parity bit counter
    for bp in range(1, sizePar + 1):
        # Bit counter one for a given parity
        contBO = 0
        # counter to control the loop reading
        contLoop = 0
        for x in dataOrd:
            if x is not None:
                try:
                    aux = (binPos[contLoop])[-1 * (bp)]

                except IndexError:
                    aux = "0"
                if aux == "1":
                    if x == "1":
                        contBO += 1
            contLoop += 1
        parity.append(contBO % 2)

        qtdBP += 1

    if paridad == "impar":
        nuevaparidad = []
        for bit in parity:
            if bit == 1:
                nuevaparidad.append(0)
            else:
                nuevaparidad.append(1)
        parity = nuevaparidad

    print(parity)
    # Mount the message
    ContBP = 0  # parity bit counter
    for x in range(0, sizePar + len(data)):
        if dataOrd[x] is None:
            dataOut.append(str(parity[ContBP]))
            ContBP += 1
        else:
            dataOut.append(dataOrd[x])

    return dataOut


'''
binaryText = '101010101010'
print("\n --Message exchange--")
print("Data to send ------------> " + binaryText)
dataOut = emitterConverter(5, binaryText, "par")
print("Data converted ----------> " + "".join(dataOut))
print(dataOut)
'''

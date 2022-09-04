from GUI import *


def execute():
    noparity = 5
    binary = "100101011000"
    parity = "par"
    hamming = hammingTables(noparity, binary, parity)


execute()

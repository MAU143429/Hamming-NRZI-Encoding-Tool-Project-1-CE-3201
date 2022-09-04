import time
from tkinter import *
from tkinter import ttk
from turtle import onclick
from hamming import *


class hammingTables:
    def __init__(self, sizePar, data, paridad):

        self.sizePar = sizePar
        self.data = data
        self.paridad = paridad
        self.veredict = ""
        self.paridades1 = []
        self.paridades2 = []

        self.gui = Tk()
        self.gui.geometry("1300x950")
        self.gui.title("Sistemas Numéricos Posicionales y Códigos")
        self.gui.configure(bg='silver')

        self.tv = ttk.Treeview(self.gui, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7",
                                                  "col8", "col9", "col10", "col11", "col12", "col13", "col14", "col15", "col16", "col17"))

        self.tv2 = ttk.Treeview(self.gui, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7",
                                                   "col8", "col9", "col10", "col11", "col12", "col13", "col14", "col15", "col16", "col17", "col18", "col19", "col20"))

        self.s = ttk.Style(self.gui)
        self.s.theme_use("clam")
        self.s.configure('Treeview', background="silver",
                         foreground="black",
                         rowheight=40,
                         fieldbackground="silver",
                         font=('Calibri', 11)
                         )
        self.s.configure("Treeview.Heading", font=('Calibri', 11, 'bold'))

        self.tv.column("#0", width=145)
        self.tv.column("col1", width=45, anchor=CENTER)
        self.tv.column("col2", width=45, anchor=CENTER)
        self.tv.column("col3", width=45, anchor=CENTER)
        self.tv.column("col4", width=45, anchor=CENTER)
        self.tv.column("col5", width=45, anchor=CENTER)
        self.tv.column("col6", width=45, anchor=CENTER)
        self.tv.column("col7", width=45, anchor=CENTER)
        self.tv.column("col8", width=45, anchor=CENTER)
        self.tv.column("col9", width=45, anchor=CENTER)
        self.tv.column("col10", width=45, anchor=CENTER)
        self.tv.column("col11", width=45, anchor=CENTER)
        self.tv.column("col12", width=45, anchor=CENTER)
        self.tv.column("col13", width=45, anchor=CENTER)
        self.tv.column("col14", width=45, anchor=CENTER)
        self.tv.column("col15", width=45, anchor=CENTER)
        self.tv.column("col16", width=45, anchor=CENTER)
        self.tv.column("col17", width=45, anchor=CENTER)

        self.tv2.column("#0", width=145)
        self.tv2.column("col1", width=45, anchor=CENTER)
        self.tv2.column("col2", width=45, anchor=CENTER)
        self.tv2.column("col3", width=45, anchor=CENTER)
        self.tv2.column("col4", width=45, anchor=CENTER)
        self.tv2.column("col5", width=45, anchor=CENTER)
        self.tv2.column("col6", width=45, anchor=CENTER)
        self.tv2.column("col7", width=45, anchor=CENTER)
        self.tv2.column("col8", width=45, anchor=CENTER)
        self.tv2.column("col9", width=45, anchor=CENTER)
        self.tv2.column("col10", width=45, anchor=CENTER)
        self.tv2.column("col11", width=45, anchor=CENTER)
        self.tv2.column("col12", width=45, anchor=CENTER)
        self.tv2.column("col13", width=45, anchor=CENTER)
        self.tv2.column("col14", width=45, anchor=CENTER)
        self.tv2.column("col15", width=45, anchor=CENTER)
        self.tv2.column("col16", width=45, anchor=CENTER)
        self.tv2.column("col17", width=45, anchor=CENTER)
        self.tv2.column("col18", width=100, anchor=CENTER)
        self.tv2.column("col19", width=135, anchor=CENTER)
        self.tv2.column("col20", width=110, anchor=CENTER)

        self.tv.heading("#0", text="Código Hamming", anchor=CENTER)
        self.tv.heading("col1", text="P1", anchor=CENTER)  # 1
        self.tv.heading("col2", text="P2", anchor=CENTER)  # 2
        self.tv.heading("col3", text="D1", anchor=CENTER)  # 3
        self.tv.heading("col4", text="P3", anchor=CENTER)  # 4
        self.tv.heading("col5", text="D2", anchor=CENTER)  # 5
        self.tv.heading("col6", text="D3", anchor=CENTER)  # 6
        self.tv.heading("col7", text="D4", anchor=CENTER)  # 7
        self.tv.heading("col8", text="P4", anchor=CENTER)  # 8
        self.tv.heading("col9", text="D5", anchor=CENTER)  # 9
        self.tv.heading("col10", text="D6", anchor=CENTER)  # 10
        self.tv.heading("col11", text="D7", anchor=CENTER)  # 11
        self.tv.heading("col12", text="D8", anchor=CENTER)  # 12
        self.tv.heading("col13", text="D9", anchor=CENTER)  # 13
        self.tv.heading("col14", text="D10", anchor=CENTER)  # 14
        self.tv.heading("col15", text="D11", anchor=CENTER)  # 15
        self.tv.heading("col16", text="P5", anchor=CENTER)  # 16
        self.tv.heading("col17", text="D12", anchor=CENTER)  # 17

        self.tv2.heading("#0", text="Código Hamming", anchor=CENTER)
        self.tv2.heading("col1", text="P1", anchor=CENTER)  # 1
        self.tv2.heading("col2", text="P2", anchor=CENTER)  # 2
        self.tv2.heading("col3", text="D1", anchor=CENTER)  # 3
        self.tv2.heading("col4", text="P3", anchor=CENTER)  # 4
        self.tv2.heading("col5", text="D2", anchor=CENTER)  # 5
        self.tv2.heading("col6", text="D3", anchor=CENTER)  # 6
        self.tv2.heading("col7", text="D4", anchor=CENTER)  # 7
        self.tv2.heading("col8", text="P4", anchor=CENTER)  # 8
        self.tv2.heading("col9", text="D5", anchor=CENTER)  # 9
        self.tv2.heading("col10", text="D6", anchor=CENTER)  # 10
        self.tv2.heading("col11", text="D7", anchor=CENTER)  # 11
        self.tv2.heading("col12", text="D8", anchor=CENTER)  # 12
        self.tv2.heading("col13", text="D9", anchor=CENTER)  # 13
        self.tv2.heading("col14", text="D10", anchor=CENTER)  # 14
        self.tv2.heading("col15", text="D11", anchor=CENTER)  # 15
        self.tv2.heading("col16", text="P5", anchor=CENTER)  # 16
        self.tv2.heading("col17", text="D12", anchor=CENTER)
        self.tv2.heading("col18", text="Paridad Nueva",
                         anchor=CENTER)  # 16
        self.tv2.heading("col19", text="Paridad Almacenada", anchor=CENTER)
        self.tv2.heading("col20", text="Comprobación", anchor=CENTER)
        # Create Frame
        self.frame1 = Frame(self.gui, bg="silver")
        self.tv.pack(pady=15)
        self.frame1.pack()
        self.tv2.pack(pady=15)
        label2 = Label(self.frame1, text="Cambio de bit")
        label2.grid(row=0, column=0, padx=10, pady=10)
        label2.configure(bg="silver")
        self.entry_text = StringVar()
        self.entry_text = self.data
        print("SOY EL ENTRY" + self.entry_text)
        self.entry = Entry(self.frame1, textvariable=self.data)
        self.entry.grid(row=0, column=1, padx=10, pady=10)
        button1 = Button(self.frame1, text="Calcular",
                         command=self.executeError)
        button1.grid(row=0, column=2, padx=10, pady=10)
        self.generateTable()
        self.entry.insert(0, self.entry_text)

        self.gui.mainloop()

    def consulta(self):
        result = self.entry.get()
        return result

    def generateTable(self):
        hamming = emitterConverter(self.sizePar, self.data, self.paridad)
        self.tv.insert("", END, text="Posición", values=("00001 \n   (1)", "00010\n  (2)", "00011\n  (3)", "00100\n  (4)", "00101\n  (5)", "00110\n  (6)", "00111\n  (7)",
                                                         "01000\n  (8)", "01001\n  (9)", "01010\n  (10)", "01011\n  (11)", "01100\n  (12)", "01101\n  (13)", "01110\n  (14)", "01111\n  (15)", "10000\n  (16)", "10001\n  (17)"))
        self.tv.insert("", END, text="Palabra Original", values=("", "", hamming[2], "", hamming[4], hamming[5], hamming[6],
                                                                 "", hamming[8], hamming[9], hamming[10], hamming[11], hamming[12], hamming[13], hamming[14], "", hamming[16]))
        self.tv.insert("", END, text="P1", values=(hamming[0], "", hamming[2], "", hamming[4], "", hamming[6],
                                                   "", hamming[8], "", hamming[10], "", hamming[12], "", hamming[14], "", hamming[16]))
        self.tv.insert("", END, text="P2", values=("", hamming[1], hamming[2], "", "", hamming[5], hamming[6],
                                                   "", "", hamming[9], hamming[10], "", "", hamming[13], hamming[14], "", ""))
        self.tv.insert("", END, text="P3", values=("", "", "",
                                                   hamming[3], hamming[4], hamming[5], hamming[6], "", "", "", "", hamming[11], hamming[12], hamming[13], hamming[14], "", ""))
        self.tv.insert("", END, text="P4", values=("", "", "", "", "", "", "",
                                                   hamming[7], hamming[8], hamming[9], hamming[10], hamming[11], hamming[12], hamming[13], hamming[14], "", ""))
        self.tv.insert("", END, text="P5", values=("", "", "", "", "", "", "", "",
                                                   "", "", "", "", "", "", "", hamming[15], hamming[16]))
        self.tv.insert("", END, text="Palabra con paridad",
                       values=(hamming[0], hamming[1], hamming[2], hamming[3], hamming[4], hamming[5], hamming[6], hamming[7], hamming[8], hamming[9], hamming[10], hamming[11], hamming[12], hamming[13], hamming[14], hamming[15], hamming[16]))

        self.paridades1.append(hamming[15])
        self.paridades1.append(hamming[7])
        self.paridades1.append(hamming[3])
        self.paridades1.append(hamming[1])
        self.paridades1.append(hamming[0])

        return hamming

    def errorVerification(self, modifydata):
        print("EL NUEVO CODIGO A UTILIZAR ES: " + modifydata)
        print(len(modifydata))
        newHamming = emitterConverter(self.sizePar, modifydata, self.paridad)

        self.paridades2.append(newHamming[15])
        self.paridades2.append(newHamming[7])
        self.paridades2.append(newHamming[3])
        self.paridades2.append(newHamming[1])
        self.paridades2.append(newHamming[0])

        comparation = self.verifyData()

        self.tv2.insert("", END, text="Posición", values=("00001 \n   (1)", "00010\n  (2)", "00011\n  (3)", "00100\n  (4)", "00101\n  (5)", "00110\n  (6)", "00111\n  (7)",
                                                          "01000\n  (8)", "01001\n  (9)", "01010\n  (10)", "01011\n  (11)", "01100\n  (12)", "01101\n  (13)", "01110\n  (14)", "01111\n  (15)", "10000\n  (16)", "10001\n  (17)"))
        self.tv2.insert("", END, text="Palabra Original", values=("", "", newHamming[2], "", newHamming[4], newHamming[5], newHamming[6],
                                                                  "", newHamming[8], newHamming[9], newHamming[10], newHamming[11], newHamming[12], newHamming[13], newHamming[14], "", newHamming[16]))
        self.tv2.insert("", END, text="P1", values=(newHamming[0], "", newHamming[2], "", newHamming[4], "", newHamming[6],
                                                    "", newHamming[8], "", newHamming[10], "", newHamming[12], "", newHamming[14], "", newHamming[16], newHamming[0], self.paridades1[0], comparation[0]))
        self.tv2.insert("", END, text="P2", values=("", newHamming[1], newHamming[2], "", "", newHamming[5], newHamming[6],
                                                    "", "", newHamming[9], newHamming[10], "", "", newHamming[13], newHamming[14], "", "", newHamming[1], self.paridades1[1], comparation[1]))
        self.tv2.insert("", END, text="P3", values=("", "", "",
                                                    newHamming[3], newHamming[4], newHamming[5], newHamming[6], "", "", "", "", newHamming[11], newHamming[12], newHamming[13], newHamming[14], "", "", newHamming[3], self.paridades1[2], comparation[2]))
        self.tv2.insert("", END, text="P4", values=("", "", "", "", "", "", "",
                                                    newHamming[7], newHamming[8], newHamming[9], newHamming[10], newHamming[11], newHamming[12], newHamming[13], newHamming[14], "", "", newHamming[7], self.paridades1[3], comparation[3]))
        self.tv2.insert("", END, text="P5", values=("", "", "", "", "", "", "", "",
                                                    "", "", "", "", "", "", "", newHamming[15], newHamming[16], newHamming[15], self.paridades1[4], comparation[4]))
        self.tv2.insert("", END, text="Palabra con paridad",
                        values=(newHamming[0], newHamming[1], newHamming[2], newHamming[3], newHamming[4], newHamming[5], newHamming[6], newHamming[7], newHamming[8], newHamming[9], newHamming[10], newHamming[11], newHamming[12], newHamming[13], newHamming[14], newHamming[15], newHamming[16], "", "", self.veredict))

    def executeError(self):
        print("EJECUTANDO CORRECION")
        return self.errorVerification(self.consulta())

    def binToDec(self, bin):
        pos = 0
        dec = 0
        bin = bin[::-1]
        for digit in bin:
            mult = 2**pos
            dec += int(digit) * mult
            pos += 1
        return dec

    def verifyData(self):
        final = []
        binNumber = []
        cont = 0
        while cont < len(self.paridades1):
            if self.paridades1[cont] == self.paridades2[cont]:
                final.append("Ok(0)")
                binNumber.append(0)
            else:
                final.append("Error (1)")
                binNumber.append(1)
            cont += 1
        bitError = self.binToDec(binNumber)
        if bitError != 0:
            self.veredict = (
                "ERROR EN BIT " + str(bitError))
        else:
            self.veredict = "NINGUN ERROR"
        return final

from tkinter import *
from tkinter import ttk
from hamming import *

gui = Tk()
gui.geometry("1200x950")
gui.title("Sistemas Numéricos Posicionales y Códigos")
gui.configure(bg='silver')

tv = ttk.Treeview(gui, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7",
                                "col8", "col9", "col10", "col11", "col12", "col13", "col14", "col15", "col16", "col17"))

tv2 = ttk.Treeview(gui, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7",
                                 "col8", "col9", "col10", "col11", "col12", "col13", "col14", "col15", "col16", "col17", "col18", "col19"))
s = ttk.Style(gui)
s.theme_use("clam")
s.configure('Treeview', background="silver",
            foreground="black",
            rowheight=40,
            fieldbackground="silver",
            font=('Calibri', 11)
            )
s.configure("Treeview.Heading", font=('Calibri', 11, 'bold'))

tv.column("#0", width=145)
tv.column("col1", width=45, anchor=CENTER)
tv.column("col2", width=45, anchor=CENTER)
tv.column("col3", width=45, anchor=CENTER)
tv.column("col4", width=45, anchor=CENTER)
tv.column("col5", width=45, anchor=CENTER)
tv.column("col6", width=45, anchor=CENTER)
tv.column("col7", width=45, anchor=CENTER)
tv.column("col8", width=45, anchor=CENTER)
tv.column("col9", width=45, anchor=CENTER)
tv.column("col10", width=45, anchor=CENTER)
tv.column("col11", width=45, anchor=CENTER)
tv.column("col12", width=45, anchor=CENTER)
tv.column("col13", width=45, anchor=CENTER)
tv.column("col14", width=45, anchor=CENTER)
tv.column("col15", width=45, anchor=CENTER)
tv.column("col16", width=45, anchor=CENTER)
tv.column("col17", width=45, anchor=CENTER)

tv2.column("#0", width=145)
tv2.column("col1", width=45, anchor=CENTER)
tv2.column("col2", width=45, anchor=CENTER)
tv2.column("col3", width=45, anchor=CENTER)
tv2.column("col4", width=45, anchor=CENTER)
tv2.column("col5", width=45, anchor=CENTER)
tv2.column("col6", width=45, anchor=CENTER)
tv2.column("col7", width=45, anchor=CENTER)
tv2.column("col8", width=45, anchor=CENTER)
tv2.column("col9", width=45, anchor=CENTER)
tv2.column("col10", width=45, anchor=CENTER)
tv2.column("col11", width=45, anchor=CENTER)
tv2.column("col12", width=45, anchor=CENTER)
tv2.column("col13", width=45, anchor=CENTER)
tv2.column("col14", width=45, anchor=CENTER)
tv2.column("col15", width=45, anchor=CENTER)
tv2.column("col16", width=45, anchor=CENTER)
tv2.column("col17", width=45, anchor=CENTER)
tv2.column("col18", width=120, anchor=CENTER)
tv2.column("col19", width=95, anchor=CENTER)

tv.heading("#0", text="Código Hamming", anchor=CENTER)
tv.heading("col1", text="P1", anchor=CENTER)  # 1
tv.heading("col2", text="P2", anchor=CENTER)  # 2
tv.heading("col3", text="D1", anchor=CENTER)  # 3
tv.heading("col4", text="P3", anchor=CENTER)  # 4
tv.heading("col5", text="D2", anchor=CENTER)  # 5
tv.heading("col6", text="D3", anchor=CENTER)  # 6
tv.heading("col7", text="D4", anchor=CENTER)  # 7
tv.heading("col8", text="P4", anchor=CENTER)  # 8
tv.heading("col9", text="D5", anchor=CENTER)  # 9
tv.heading("col10", text="D6", anchor=CENTER)  # 10
tv.heading("col11", text="D7", anchor=CENTER)  # 11
tv.heading("col12", text="D8", anchor=CENTER)  # 12
tv.heading("col13", text="D9", anchor=CENTER)  # 13
tv.heading("col14", text="D10", anchor=CENTER)  # 14
tv.heading("col15", text="D11", anchor=CENTER)  # 15
tv.heading("col16", text="P5", anchor=CENTER)  # 16
tv.heading("col17", text="D12", anchor=CENTER)  # 17

tv2.heading("#0", text="Código Hamming", anchor=CENTER)
tv2.heading("col1", text="P1", anchor=CENTER)  # 1
tv2.heading("col2", text="P2", anchor=CENTER)  # 2
tv2.heading("col3", text="D1", anchor=CENTER)  # 3
tv2.heading("col4", text="P3", anchor=CENTER)  # 4
tv2.heading("col5", text="D2", anchor=CENTER)  # 5
tv2.heading("col6", text="D3", anchor=CENTER)  # 6
tv2.heading("col7", text="D4", anchor=CENTER)  # 7
tv2.heading("col8", text="P4", anchor=CENTER)  # 8
tv2.heading("col9", text="D5", anchor=CENTER)  # 9
tv2.heading("col10", text="D6", anchor=CENTER)  # 10
tv2.heading("col11", text="D7", anchor=CENTER)  # 11
tv2.heading("col12", text="D8", anchor=CENTER)  # 12
tv2.heading("col13", text="D9", anchor=CENTER)  # 13
tv2.heading("col14", text="D10", anchor=CENTER)  # 14
tv2.heading("col15", text="D11", anchor=CENTER)  # 15
tv2.heading("col16", text="P5", anchor=CENTER)  # 16
tv2.heading("col17", text="D12", anchor=CENTER)  # 17
tv2.heading("col18", text="Prueba de paridad",
            anchor=CENTER)  # 16
tv2.heading("col19", text="Bit de Paridad", anchor=CENTER)  # 17

# Create Frame
frame1 = Frame(gui, bg="silver")
tv.pack(pady=15)
frame1.pack()
tv2.pack(pady=15)
label2 = Label(frame1, text="Cambio de bit")
label2.grid(row=0, column=0, padx=10, pady=10)
label2.configure(bg="silver")
entry = Entry(frame1)
entry.grid(row=0, column=1, padx=10, pady=10)
button1 = Button(frame1, text="Calcular")
button1.grid(row=0, column=2, padx=10, pady=10)


def generateTable(self):
    hamming = emitterConverter(sizePar, data, paridad)
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


def errorVerification(self, modifydata):

    newHamming = emitterConverter(this.sizePar, modifydata, this.paridad)
    self.tv2.insert("", END, text="Posición", values=("00001 \n   (1)", "00010\n  (2)", "00011\n  (3)", "00100\n  (4)", "00101\n  (5)", "00110\n  (6)", "00111\n  (7)",
                                                      "01000\n  (8)", "01001\n  (9)", "01010\n  (10)", "01011\n  (11)", "01100\n  (12)", "01101\n  (13)", "01110\n  (14)", "01111\n  (15)", "10000\n  (16)", "10001\n  (17)"))
    self.tv2.insert("", END, text="Palabra Original", values=("", "", newHamming[2], "", newHamming[4], newHamming[5], newHamming[6],
                                                              "", newHamming[8], newHamming[9], newHamming[10], newHamming[11], newHamming[12], newHamming[13], newHamming[14], "", newHamming[16]))
    self.tv2.insert("", END, text="P1", values=(newHamming[0], "", newHamming[2], "", newHamming[4], "", newHamming[6],
                                                "", newHamming[8], "", newHamming[10], "", newHamming[12], "", newHamming[14], "", newHamming[16]))
    self.tv2.insert("", END, text="P2", values=("", newHamming[1], newHamming[2], "", "", newHamming[5], newHamming[6],
                                                "", "", newHamming[9], newHamming[10], "", "", newHamming[13], newHamming[14], "", ""))
    self.tv2.insert("", END, text="P3", values=("", "", "",
                                                newHamming[3], newHamming[4], newHamming[5], newHamming[6], "", "", "", "", newHamming[11], newHamming[12], newHamming[13], newHamming[14], "", ""))
    self.tv2.insert("", END, text="P4", values=("", "", "", "", "", "", "",
                                                newHamming[7], newHamming[8], newHamming[9], newHamming[10], newHamming[11], newHamming[12], newHamming[13], newHamming[14], "", ""))
    self.tv2.insert("", END, text="P5", values=("", "", "", "", "", "", "", "",
                                                "", "", "", "", "", "", "", newHamming[15], newHamming[16]))
    self.tv2.insert("", END, text="Palabra con paridad",
                    values=(newHamming[0], newHamming[1], newHamming[2], newHamming[3], newHamming[4], newHamming[5], newHamming[6], newHamming[7], newHamming[8], newHamming[9], newHamming[10], newHamming[11], newHamming[12], newHamming[13], newHamming[14], newHamming[15], newHamming[16]))


gui.mainloop()

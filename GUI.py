from tkinter import *
from tkinter import ttk

gui = Tk()
gui.geometry("1200x950")
gui.title("Sistemas Numéricos Posicionales y Códigos")

tv = ttk.Treeview(gui, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7",
                  "col8", "col9", "col10", "col11", "col12", "col13", "col14", "col15", "col16", "col17"))

tv2 = ttk.Treeview(gui, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7",
                                 "col8", "col9", "col10", "col11", "col12", "col13", "col14", "col15", "col16", "col17", "col18", "col19"))

s = ttk.Style(gui)
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
tv.heading("col5", text="P2", anchor=CENTER)  # 5
tv.heading("col6", text="P3", anchor=CENTER)  # 6
tv.heading("col7", text="P4", anchor=CENTER)  # 7
tv.heading("col8", text="P4", anchor=CENTER)  # 8
tv.heading("col9", text="P5", anchor=CENTER)  # 9
tv.heading("col10", text="P6", anchor=CENTER)  # 10
tv.heading("col11", text="P7", anchor=CENTER)  # 11
tv.heading("col12", text="P8", anchor=CENTER)  # 12
tv.heading("col13", text="P9", anchor=CENTER)  # 13
tv.heading("col14", text="P10", anchor=CENTER)  # 14
tv.heading("col15", text="P11", anchor=CENTER)  # 15
tv.heading("col16", text="P4", anchor=CENTER)  # 16
tv.heading("col17", text="P12", anchor=CENTER)  # 17


tv2.heading("#0", text="Código Hamming", anchor=CENTER)
tv2.heading("col1", text="P1", anchor=CENTER)  # 1
tv2.heading("col2", text="P2", anchor=CENTER)  # 2
tv2.heading("col3", text="D1", anchor=CENTER)  # 3
tv2.heading("col4", text="P3", anchor=CENTER)  # 4
tv2.heading("col5", text="P2", anchor=CENTER)  # 5
tv2.heading("col6", text="P3", anchor=CENTER)  # 6
tv2.heading("col7", text="P4", anchor=CENTER)  # 7
tv2.heading("col8", text="P4", anchor=CENTER)  # 8
tv2.heading("col9", text="P5", anchor=CENTER)  # 9
tv2.heading("col10", text="P6", anchor=CENTER)  # 10
tv2.heading("col11", text="P7", anchor=CENTER)  # 11
tv2.heading("col12", text="P8", anchor=CENTER)  # 12
tv2.heading("col13", text="P9", anchor=CENTER)  # 13
tv2.heading("col14", text="P10", anchor=CENTER)  # 14
tv2.heading("col15", text="P11", anchor=CENTER)  # 15
tv2.heading("col16", text="P4", anchor=CENTER)  # 16
tv2.heading("col17", text="P12", anchor=CENTER)  # 17
tv2.heading("col18", text="Prueba de paridad", anchor=CENTER)  # 16
tv2.heading("col19", text="Bit de Paridad", anchor=CENTER)  # 17


tv.insert("", END, text="Posición", values=("00001 \n   (1)", "00010\n  (2)", "00011\n  (3)", "00100\n  (4)", "00101\n  (5)", "00110\n  (6)", "00111\n  (7)",
          "01000\n  (8)", "01001\n  (9)", "01010\n  (10)", "01011\n  (11)", "01100\n  (12)", "01101\n  (13)", "01110\n  (14)", "01111\n  (15)", "10000\n  (16)", "10001\n  (17)"))
tv.insert("", END, text="Palabra Original", values=("", ""))
tv.insert("", END, text="P1", values=("", ""))
tv.insert("", END, text="P2", values=("", ""))
tv.insert("", END, text="P3", values=("", ""))
tv.insert("", END, text="P4", values=("", ""))
tv.insert("", END, text="P5", values=("", ""))
tv.insert("", END, text="Palabra con paridad", values=("", ""))

tv2.insert("", END, text="Posición", values=("00001 \n   (1)", "00010\n  (2)", "00011\n  (3)", "00100\n  (4)", "00101\n  (5)", "00110\n  (6)", "00111\n  (7)",
                                             "01000\n  (8)", "01001\n  (9)", "01010\n  (10)", "01011\n  (11)", "01100\n  (12)", "01101\n  (13)", "01110\n  (14)", "01111\n  (15)", "10000\n  (16)", "10001\n  (17)"))
tv2.insert("", END, text="Palabra Original", values=("", ""))
tv2.insert("", END, text="P1", values=("", ""))
tv2.insert("", END, text="P2", values=("", ""))
tv2.insert("", END, text="P3", values=("", ""))
tv2.insert("", END, text="P4", values=("", ""))
tv2.insert("", END, text="P5", values=("", ""))
tv2.insert("", END, text="Palabra con paridad", values=("", ""))

# Create Frame
frame1 = Frame(gui)
tv.pack(pady=15)
frame1.pack()
tv2.pack(pady=15)
label2 = Label(frame1, text="Cambio de bit")
label2.grid(row=0, column=0, padx=10, pady=10)
entry = Entry(frame1, text="101010101011")
entry.grid(row=0, column=1, padx=10, pady=10)
button1 = Button(frame1, text="Calcular")
button1.grid(row=0, column=2, padx=10, pady=10)

gui.mainloop()

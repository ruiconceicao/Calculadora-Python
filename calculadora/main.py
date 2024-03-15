'''
Este programa tem como funções todas as comuns
operações matemáticas servindo então como calculadora.

Programa criado a 13/03/24 às 13:00
Rui Conceição
'''



from tkinter import ANCHOR
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.maxsize(500, 500)

        self.buttonFrame = MyButtonFrame(self)
        self.buttonFrame.pack(pady=10, padx=10, fill='both',expand=True)

class MyButtonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.resLabel = ctk.CTkLabel(self, text="0", font=("", 40), anchor="se")
        self.resLabel.grid(row=5, column=0, columnspan=4, sticky="new")
        
        self.btnAC = ctk.CTkButton(self, text="AC", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btnAC.grid(row=0, column=0, sticky="new")
        self.btnNeg = ctk.CTkButton(self, text="+/-", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(1))
        self.btnNeg.grid(row=0, column=1, sticky="new")
        self.btnPerc = ctk.CTkButton(self, text="%", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(2))
        self.btnPerc.grid(row=0, column=2, sticky="new")
        self.btndivide = ctk.CTkButton(self, text="/", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btndivide.grid(row=0, column=3, sticky="new")

        self.btn7 = ctk.CTkButton(self, text="7", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btn7.grid(row=1, column=0, sticky="new")
        self.btn8 = ctk.CTkButton(self, text="8", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(1))
        self.btn8.grid(row=1, column=1, sticky="new")
        self.btn9 = ctk.CTkButton(self, text="9", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(2))
        self.btn9.grid(row=1, column=2, sticky="new")
        self.btntimes = ctk.CTkButton(self, text="x", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btntimes.grid(row=1, column=3, sticky="new")

        self.btn4 = ctk.CTkButton(self, text="4", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btn4.grid(row=2, column=0, sticky="new")
        self.btn5 = ctk.CTkButton(self, text="5", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(1))
        self.btn5.grid(row=2, column=1, sticky="new")
        self.btn6 = ctk.CTkButton(self, text="6", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(2))
        self.btn6.grid(row=2, column=2, sticky="new")
        self.btnminus = ctk.CTkButton(self, text="-", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btnminus.grid(row=2, column=3, sticky="new")

        self.btn1 = ctk.CTkButton(self, text="1", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(1))
        self.btn1.grid(row=3, column=0, sticky="new")
        self.btn2 = ctk.CTkButton(self, text="2", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(2))
        self.btn2.grid(row=3, column=1, sticky="new")
        self.btn3 = ctk.CTkButton(self, text="3", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btn3.grid(row=3, column=2, sticky="new")
        self.btnplus = ctk.CTkButton(self, text="+", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btnplus.grid(row=3, column=3, sticky="new")

        self.btn0 = ctk.CTkButton(self, text="0", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btn0.grid(row=4, column=0, sticky="new", columnspan=2)
        self.btndot = ctk.CTkButton(self, text=".", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btndot.grid(row=4, column=2, sticky="new")
        self.btnequal = ctk.CTkButton(self, text="=", font=("", 40), corner_radius=40, width=60, height=40, command=lambda: self.button_callback(0))
        self.btnequal.grid(row=4, column=3, sticky="new")


            
    def button_callback(self, btn_number):
            print("{}".format(btn_number))

app = App()
app.mainloop()

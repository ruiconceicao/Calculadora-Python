'''
Este programa tem como funções todas as comuns
operações matemáticas servindo então como calculadora.

Programa criado a 13/03/24 às 13:00
Rui Conceição
'''

import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")

        self.resFrame = MyResFrame(self)
        self.resFrame.grid(row=0, column=0, sticky="nwe")
        self.grid_columnconfigure(0, weight=1)


        self.buttonFrame = MyButtonFrame(self)
        self.buttonFrame.grid(row=1, column=0, sticky="nw")
        self.grid_columnconfigure(1, weight=1, pad=10)


class MyResFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.resLabel = ctk.CTkLabel(self, text="0", font=("Console", 50))
        self.resLabel.pack(expand=True, anchor="se")

class MyButtonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.btn7 = ctk.CTkButton(self, text="7", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(0))
        self.btn7.grid(row=0, column=0, sticky="new")
        self.btn8 = ctk.CTkButton(self, text="8", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(1))
        self.btn8.grid(row=0, column=1, sticky="new")
        self.btn9 = ctk.CTkButton(self, text="9", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(2))
        self.btn9.grid(row=0, column=2, sticky="new")

        self.btn4 = ctk.CTkButton(self, text="4", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(0))
        self.btn4.grid(row=1, column=0, sticky="new")
        self.btn5 = ctk.CTkButton(self, text="5", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(1))
        self.btn5.grid(row=1, column=1, sticky="new")
        self.btn6 = ctk.CTkButton(self, text="6", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(2))
        self.btn6.grid(row=1, column=2, sticky="new")

        self.btn0 = ctk.CTkButton(self, text="0", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(0))
        self.btn0.grid(row=2, column=0, sticky="new")
        self.btn1 = ctk.CTkButton(self, text="1", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(1))
        self.btn1.grid(row=2, column=1, sticky="new")
        self.btn2 = ctk.CTkButton(self, text="2", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(2))
        self.btn2.grid(row=2, column=2, sticky="new")
            
    def button_callback(self, btn_number):
            print("{}".format(btn_number))

app = App()
app.mainloop()

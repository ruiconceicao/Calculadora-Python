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
        self.grid_columnconfigure(1, weight=1)


class MyResFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.resLabel = ctk.CTkLabel(self, text="0", font=("Console", 50))
        self.resLabel.pack(expand=True, anchor="se")

class MyButtonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.btn0 = ctk.CTkButton(self, text="0", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(0))
        self.btn0.grid(row=3, column=0, sticky="new")
        self.btn1 = ctk.CTkButton(self, text="1", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(1))
        self.btn1.grid(row=3, column=1, sticky="new")
        self.btn2 = ctk.CTkButton(self, text="2", corner_radius=100, width=50, height=35, command=lambda: self.button_callback(2))
        self.btn2.grid(row=3, column=2, sticky="new")
            
    def button_callback(self, btn_number):
            print("{}".format(btn_number))

app = App()
app.mainloop()

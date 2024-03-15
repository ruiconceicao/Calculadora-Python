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

        self.title("my app")
        self.geometry("400x180")
        

        self.resFrame = MyResFrame(self)
        self.resFrame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.buttonFrame = MyButtonFrame(self)
        self.buttonFrame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="new")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)


class MyResFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.resLabel = ctk.CTkLabel(self, text="0")
        self.resLabel.pack(self, expand=True, pady=20, padx=20)

class MyButtonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.btn0 = ctk.CTkButton(self, text="0", command=lambda: self.button_callback(0))
        self.btn0.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.btn1 = ctk.CTkButton(self, text="1", command=lambda: self.button_callback(1))
        self.btn1.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.btn2 = ctk.CTkButton(self, text="2", command=lambda: self.button_callback(2))
        self.btn2.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
            
    def button_callback(self, btn_number):
            print("{}".format(btn_number))

app = App()
app.mainloop()
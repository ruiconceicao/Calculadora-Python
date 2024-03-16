'''
Este programa tem como funções todas as comuns
operações matemáticas servindo então como calculadora.

Programa criado a 13/03/24 às 13:00
Rui Conceição
'''
import customtkinter as ctk
ctk.deactivate_automatic_dpi_awareness()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self._set_appearance_mode("dark")

        self.buttonFrame = MyButtonFrame(self)
        self.buttonFrame.pack(pady=10, padx=10, anchor="nw")

class MyButtonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.contaLabel = ctk.CTkLabel(self, text="", font=("Roboto", 30), anchor="se")
        self.resLabel = ctk.CTkLabel(self, text="0", font=("Roboto", 30), anchor="se")
        
        self.btnAC = ctk.CTkButton(self, text="AC", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="grey", text_color="black", border_color="black", border_width=1)
        self.btn7 = ctk.CTkButton(self, text="7", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(7))
        self.btn4 = ctk.CTkButton(self, text="4", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(4))
        self.btn1 = ctk.CTkButton(self, text="1", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(1))
        self.btn0 = ctk.CTkButton(self, text="0", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(0))
        
        self.btnNeg = ctk.CTkButton(self, text="+/-", font=("Roboto", 30), corner_radius=100, width=80, height=40, fg_color="grey", text_color="black", border_color="black", border_width=1)
        self.btn8 = ctk.CTkButton(self, text="8", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(8))
        self.btn5 = ctk.CTkButton(self, text="5", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(5))
        self.btn2 = ctk.CTkButton(self, text="2", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(2))
        
        self.btnPerc = ctk.CTkButton(self, text="%", font=("Roboto", 30), corner_radius=100, width=80, height=40, fg_color="grey", text_color="black", border_color="black", border_width=1)
        self.btn9 = ctk.CTkButton(self, text="9", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(9))
        self.btn6 = ctk.CTkButton(self, text="6", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(6))
        self.btn3 = ctk.CTkButton(self, text="3", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback(3))
        self.btndot = ctk.CTkButton(self, text=".", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1,
        command=lambda: self.button_callback("."))
        
        self.btndivide = ctk.CTkButton(self, text="/", font=("Roboto", 30), corner_radius=100, width=80, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1)
        self.btntimes = ctk.CTkButton(self, text="x", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1)
        self.btnminus = ctk.CTkButton(self, text="-", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1)
        self.btnplus = ctk.CTkButton(self, text="+", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1)
        self.btnequal = ctk.CTkButton(self, text="=", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1)





        #
        self.contaLabel.grid(row=0, column=0, columnspan=4, sticky="new", pady=1)
        self.resLabel.grid(row=1, column=0, columnspan=4, sticky="new")
        #
        self.btnAC.grid(row=3, column=0, sticky="new", padx=1, pady=1)
        self.btnNeg.grid(row=3, column=1, sticky="new", padx=1, pady=1)
        self.btnPerc.grid(row=3, column=2, sticky="new", padx=1, pady=1)
        self.btndivide.grid(row=3, column=3, sticky="new", padx=1, pady=1)
        #
        self.btn7.grid(row=4, column=0, sticky="new", padx=1, pady=1)
        self.btn8.grid(row=4, column=1, sticky="new", padx=1, pady=1)
        self.btn9.grid(row=4, column=2, sticky="new", padx=1, pady=1)
        self.btntimes.grid(row=4, column=3, sticky="new", padx=1, pady=1)
        #
        self.btn4.grid(row=5, column=0, sticky="new", padx=1, pady=1)
        self.btn5.grid(row=5, column=1, sticky="new", padx=1, pady=1)
        self.btn6.grid(row=5, column=2, sticky="new", padx=1, pady=1)
        self.btnminus.grid(row=5, column=3, sticky="new", padx=1, pady=1)
        #
        self.btn1.grid(row=6, column=0, sticky="new", padx=1, pady=1)
        self.btn2.grid(row=6, column=1, sticky="new", padx=1, pady=1)
        self.btn3.grid(row=6, column=2, sticky="new", padx=1, pady=1)
        self.btnplus.grid(row=6, column=3, sticky="new", padx=1, pady=1)
        #
        self.btn0.grid(row=7, column=0, sticky="new", columnspan=2, padx=1, pady=1)
        self.btndot.grid(row=7, column=2, sticky="new", padx=1, pady=1)
        self.btnequal.grid(row=7, column=3, sticky="new", padx=1, pady=1)
            
    def button_callback(self, btn_number):
            print("{}".format(btn_number))


app = App()
app.mainloop()

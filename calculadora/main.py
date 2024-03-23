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
        self._set_appearance_mode("dark")
        self.minsize
        self.maxsize

        self.buttonFrame = MyFrame(self)
        self.buttonFrame.pack(pady=10, padx=10, anchor="nw")
        
class MyFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Label for result and for last math operation in rows 0 and 1
        self.contaLabel = ctk.CTkLabel(self, text="", font=("Roboto", 30), anchor="se")
        self.resLabel = ctk.CTkLabel(self, text="", font=("Roboto", 30), anchor="se")
        
        # Buttons in column 0
        self.btnAC = ctk.CTkButton(self, text="AC", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="#808080", text_color="black", border_color="black", border_width=1, hover_color="#a6a6a6", 
            command=lambda: self.btn_AC())
        self.btn7 = ctk.CTkButton(self, text="7", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn7.cget("text")))
        self.btn4 = ctk.CTkButton(self, text="4", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn4.cget("text")))
        self.btn1 = ctk.CTkButton(self, text="1", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn1.cget("text")))
        self.btn0 = ctk.CTkButton(self, text="0", font=("Roboto", 30), corner_radius=100, width=0, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn0.cget("text")))
        
        # Buttons in column 1
        self.btnneg = ctk.CTkButton(self, text="±", font=("Roboto", 30), corner_radius=100, width=80, height=40, fg_color="#808080", text_color="black", border_color="black", border_width=1, hover_color="#a6a6a6",
            command=lambda: self.btn_neg(self.resLabel.cget("text")))
        self.btn8 = ctk.CTkButton(self, text="8", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn8.cget("text")))
        self.btn5 = ctk.CTkButton(self, text="5", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn5.cget("text")))
        self.btn2 = ctk.CTkButton(self, text="2", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn2.cget("text"))) 
        
        # Buttons in column 2
        self.btnperc = ctk.CTkButton(self, text="%", font=("Roboto", 30), corner_radius=100, width=80, height=40, fg_color="#808080", text_color="black", border_color="black", border_width=1, hover_color="#a6a6a6",
            command=lambda: self.btn_perc(self.resLabel.cget("text")))
        self.btn9 = ctk.CTkButton(self, text="9", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn9.cget("text")))
        self.btn6 = ctk.CTkButton(self, text="6", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn6.cget("text")))
        self.btn3 = ctk.CTkButton(self, text="3", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btn3.cget("text")))
        self.btndot = ctk.CTkButton(self, text=".", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#424242", text_color="white", border_color="black", border_width=1, hover_color="#666666",
            command=lambda: self.btn_click(self.btndot.cget("text")))
        self.btnequal = ctk.CTkButton(self, text="=", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1, hover_color="#f4a23e",
            command=lambda: self.btn_equal(self.resLabel.cget("text")))
        
        # Buttons in column 3
        self.btnerase = ctk.CTkButton(self, text="←", font=("Roboto", 30), corner_radius=100, width=80, height=40, fg_color="#808080", text_color="black", border_color="black", border_width=1, hover_color="#a6a6a6",
            command=lambda: self.btn_erase(self.resLabel.cget("text")))
        self.btndivide = ctk.CTkButton(self, text="÷", font=("Roboto", 30), corner_radius=100, width=80, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1, hover_color="#f4a23e",
            command=lambda: self.btn_click(self.btndivide.cget("text")))
        self.btntimes = ctk.CTkButton(self, text="x", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1, hover_color="#f4a23e",
            command=lambda: self.btn_click(self.btntimes.cget("text")))
        self.btnminus = ctk.CTkButton(self, text="-", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1, hover_color="#f4a23e",
            command=lambda: self.btn_click(self.btnminus.cget("text")))
        self.btnplus = ctk.CTkButton(self, text="+", font=("Roboto", 30), corner_radius=100, width=60, height=40, fg_color="#e0810d", text_color="white", border_color="black", border_width=1, hover_color="#f4a23e",
            command=lambda: self.btn_click(self.btnplus.cget("text")))

        # Label configs and positions in rows 0 and 1
        self.contaLabel.grid(row=0, column=0, columnspan=4, sticky="new")
        self.resLabel.grid(row=1, column=0, columnspan=4, sticky="new")
        # Buttons configs and positions in row 2
        self.btnAC.grid(row=2, column=0, sticky="new", padx=1, pady=5)
        self.btnneg.grid(row=2, column=1, sticky="new", padx=1, pady=5)
        self.btnperc.grid(row=2, column=2, sticky="new", padx=1, pady=5)
        self.btnerase.grid(row=2, column=3, sticky="new", padx=1, pady=5)        
        # Buttons configs and positions in row 3
        self.btn7.grid(row=3, column=0, sticky="new", padx=1, pady=5)
        self.btn8.grid(row=3, column=1, sticky="new", padx=1, pady=5)
        self.btn9.grid(row=3, column=2, sticky="new", padx=1, pady=5)
        self.btndivide.grid(row=3, column=3, sticky="new", padx=1, pady=5)
        # Buttons configs and positions in row 4
        self.btn4.grid(row=4, column=0, sticky="new", padx=1, pady=5)
        self.btn5.grid(row=4, column=1, sticky="new", padx=1, pady=5)
        self.btn6.grid(row=4, column=2, sticky="new", padx=1, pady=5)
        self.btntimes.grid(row=4, column=3, sticky="new", padx=1, pady=5)
        # Buttons configs and positions in row 5
        self.btn1.grid(row=5, column=0, sticky="new", padx=1, pady=5)
        self.btn2.grid(row=5, column=1, sticky="new", padx=1, pady=5)
        self.btn3.grid(row=5, column=2, sticky="new", padx=1, pady=5)
        self.btnminus.grid(row=5, column=3, sticky="new", padx=1, pady=5)
        # Buttons configs and positions in row 6
        self.btn0.grid(row=6, column=0, sticky="new", padx=1, pady=5)
        self.btndot.grid(row=6, column=1, sticky="new", padx=1, pady=5)
        self.btnequal.grid(row=6, column=2, sticky="new", padx=1, pady=5)
        self.btnplus.grid(row=6, column=3, sticky="new", padx=1, pady=5)

    def btn_click(self, numberOrSymbol):
        try:
            self.resLabel.configure(text=("{}{}".format(self.resLabel.cget("text"), numberOrSymbol)))
        except:
            self.resLabel.configure(text=("Error"), text_color="red")

    def btn_erase(self, conta):
        try:
            self.resLabel.configure(text=(conta[:-1]))
        except:
            self.resLabel.configure(text=("Error"), text_color="red")

    def btn_equal(self, conta):
        try:
            # substitute "*" for x and "/" for ÷
            self.resLabel.configure(text=("{}".format(eval(conta))))
            self.contaLabel.configure(text=("{}".format(conta)))
        except:
            self.resLabel.configure(text=("Error"), text_color="red")

    def btn_perc(self, conta):
        try:
            self.contaLabel.configure(text=("{}".format("({})*100".format(conta))))
            self.resLabel.configure(text=("{}".format(eval("({})*100".format(conta)))))
        except:
            self.resLabel.configure(text=("Error"), text_color="red")

    def btn_neg(self, conta):
            try:
                self.resLabel.configure(text=(eval("({})*(-1)".format(self.resLabel.cget("text")))))
            except:
                self.resLabel.configure(text=("Error"), text_color="red")

    def btn_AC(self):
        self.contaLabel.configure(text="")
        self.resLabel.configure(text="", text_color="white")
    
app = App()
app.mainloop()
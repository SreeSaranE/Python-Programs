import customtkinter as ctk

class app:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Calculator")
        self.window.geometry('380x300')
        self.window.resizable(False, False)

        self.padding: dict = {'padx': 30,'pady': 10}

        self.number1 = ctk.CTkLabel(self.window, text="Number 1")
        self.number1.grid(row=0, column=0, **self.padding)
        self.num1_entry = ctk.CTkEntry(self.window)
        self.num1_entry.grid(row=0, column=1, **self.padding)

        self.number2 = ctk.CTkLabel(self.window, text="Number 2")
        self.number2.grid(row=1, column=0, **self.padding)
        self.num2_entry = ctk.CTkEntry(self.window)
        self.num2_entry.grid(row=1, column=1, **self.padding)

        self.results = ctk.CTkLabel(self.window, text="Result")
        self.results.grid(row=2, column=0, **self.padding)
        self.results_entry = ctk.CTkEntry(self.window)
        self.results_entry.grid(row=2, column=1, **self.padding)

        self.cal_add = ctk.CTkButton(self.window, text='+', command=self.callculate_add)
        self.cal_add.grid(row=3, column=0, **self.padding)

        self.cal_add = ctk.CTkButton(self.window, text='-', command=self.callculate_sub)
        self.cal_add.grid(row=3, column=1, **self.padding)

        self.cal_add = ctk.CTkButton(self.window, text='*', command=self.callculate_mul)
        self.cal_add.grid(row=4, column=0, **self.padding)

        self.cal_add = ctk.CTkButton(self.window, text='/', command=self.callculate_div)
        self.cal_add.grid(row=4, column=1, **self.padding)

        self.reset_val = ctk.CTkButton(self.window, text='Reset', command=self.reset_all)
        self.reset_val.grid(row=5, column=0, **self.padding)
        

    def reset(self, text: str):
        self.results_entry.delete(0,ctk.END)
        self.results_entry.insert(0, text)
    
    def reset_all(self):
        self.results_entry.delete(0,ctk.END)
        self.results_entry.insert(0, '0')
        self.num1_entry.delete(0,ctk.END)
        self.num1_entry.insert(0, '0')
        self.num2_entry.delete(0,ctk.END)
        self.num2_entry.insert(0, '0')

    def callculate_add(self):
        try:
            num1: float = float(self.num1_entry.get())
            num2: float = float(self.num2_entry.get())
            self.reset(num1+num2)

        except ValueError:
            self.reset("Invalid Input")
    
    def callculate_sub(self):
        try:
            num1: float = float(self.num1_entry.get())
            num2: float = float(self.num2_entry.get())
            self.reset(num1-num2)

        except ValueError:
            self.reset("Invalid Input")

    def callculate_mul(self):
        try:
            num1: float = float(self.num1_entry.get())
            num2: float = float(self.num2_entry.get())
            self.reset(num1*num2)

        except ValueError:
            self.reset("Invalid Input")

    def callculate_div(self):
        try:
            num1: float = float(self.num1_entry.get())
            num2: float = float(self.num2_entry.get())
            self.reset(num1/num2)

        except ValueError:
            self.reset("Invalid Input")
            

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    cal = app()
    cal.run()

import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator from kuldeep singh")

        self.result_var = tk.StringVar()

        
        self.entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 24), bd=10,bg="white", insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=5)

        
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'log',
            '(', ')', 'sqrt', 'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18), command=self.calculate).grid(row=row_val, column=col_val)
            elif button == 'C':
                tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18), command=self.clear).grid(row=row_val, column=col_val)
            else:
                tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.append_to_expression(b)).grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def append_to_expression(self, value):
        current_text = self.result_var.get()
        new_text = current_text + str(value)
        self.result_var.set(new_text)

    def calculate(self):
        try:
            expression = self.result_var.get()
            
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log10')  
            expression = expression.replace('sqrt', 'math.sqrt')

            result = eval(expression)
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
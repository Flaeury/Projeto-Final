import tkinter as tk
import math


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        #
        self.entry = tk.Entry(root, width=20, font=(
            'Arial', 20), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        # Botões
        buttons = [
            ('√x', 1, 0), ('x²', 1, 1), ('ce', 1, 2), ('c', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
        ]

        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, font=(
                'Arial', 20), command=lambda t=text: self.add_to_entry(t))
            button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    def add_to_entry(self, value):
        if value == '=':
            current = self.entry.get()
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        elif value == 'c':  # Limpar a entrada
            self.entry.delete(0, tk.END)
        elif value == 'ce':  # Limpar a entrada atual
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            # Remove o último caractere
            self.entry.insert(tk.END, current[:-1])
        elif value == 'x²':  # Eleva ao quadrado
            current = self.entry.get()
            try:
                result = eval(current)**2
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        elif value == '√x':  # Raiz quadrada
            current = self.entry.get()
            try:
                result = math.sqrt(eval(current))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        else:
            self.entry.insert(tk.END, value)


# Criar e iniciar a aplicação
root = tk.Tk()
app = Calculadora(root)
root.mainloop()

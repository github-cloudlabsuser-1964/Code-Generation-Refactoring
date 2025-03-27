import tkinter as tk
from operations import add, subtract, multiply, divide, percentage, square, square_root

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ultra Polished Calculator")
        self.entry_text = tk.StringVar()
        self.display = tk.Entry(master, textvariable=self.entry_text, font=("Arial", 16), bd=10, insertwidth=2, width=14,
                                borderwidth=4, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self._create_buttons()

    def _create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3),
            ("Sqr", 5, 0), ("Sqrt", 5, 1), ("C", 5, 2), ("=", 5, 3),
        ]
        for (text, r, c) in buttons:
            tk.Button(self.master, text=text, padx=20, pady=10, font=("Arial", 14),
                      command=lambda val=text: self._on_button_click(val)) \
                .grid(row=r, column=c, sticky="nsew")

    def _on_button_click(self, char):
        if char == "C":
            self.entry_text.set("")
        elif char == "=":
            expression = self.entry_text.get()
            try:
                # Minimal parser for standard operators:
                if "+" in expression:
                    a, b = expression.split("+")
                    result = add(float(a), float(b))
                elif "-" in expression:
                    a, b = expression.split("-")
                    result = subtract(float(a), float(b))
                elif "*" in expression:
                    a, b = expression.split("*")
                    result = multiply(float(a), float(b))
                elif "/" in expression:
                    a, b = expression.split("/")
                    result = divide(float(a), float(b))
                elif "%" in expression:
                    a, b = expression.split("%")
                    result = percentage(float(a), float(b))
                else:
                    result = expression
                self.entry_text.set(result)
            except:
                self.entry_text.set("Error")
        elif char == "Sqr":
            try:
                val = float(self.entry_text.get())
                self.entry_text.set(square(val))
            except:
                self.entry_text.set("Error")
        elif char == "Sqrt":
            try:
                val = float(self.entry_text.get())
                self.entry_text.set(square_root(val))
            except:
                self.entry_text.set("Error")
        else:
            current = self.entry_text.get()
            self.entry_text.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
import tkinter as tk
from keypad import Keypad


class CalculatorUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Calculator")

        keys = ["7", "8", "9", "/", "4", "5", "6", "*",
                "1", "2", "3", "-", " ", "0", ".", "C", "^", "+", "=", "DEL", "ret"]

        self.entry_field = tk.Entry(
            self.root, font=("Arial", 18), justify="right")
        self.entry_field.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.keypad = Keypad(self.root, keynames=keys,
                             columns=4, entry=self.entry_field)
        self.keypad.grid(row=1, column=0, columnspan=4, sticky="nsew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        for col in range(4):
            self.root.grid_columnconfigure(col, weight=1)

    def run(self):
        self.root.mainloop()

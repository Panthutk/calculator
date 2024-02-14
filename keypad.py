import tkinter as tk
from tkinter import ttk


class Keypad(tk.Frame):

    def __init__(self, parent, keynames=[], columns=3, entry=None, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.keynames = keynames
        self.entry = entry
        self.init_components(columns)

    def init_components(self, columns) -> None:
        for i, key in enumerate(self.keynames):
            button = tk.Button(self, text=key, padx=5, pady=5,
                               command=lambda k=key: self.handle_key_press(k))

            row = i // columns
            col = i % columns

            if key in ['+', '-', '*', '/']:
                # Place operator buttons in the last column
                button.grid(row=row, column=columns, sticky=tk.NSEW)
            else:
                button.grid(row=row, column=col, sticky=tk.NSEW)

            self.columnconfigure(col, weight=1)

    def bind(self, sequence=None, func=None, add=None):
        for child in self.winfo_children():
            child.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        for child in self.winfo_children():
            child[key] = value

    def __getitem__(self, key):
        return self.winfo_children()[0][key]

    def configure(self, cnf=None, **kwargs):
        super().configure(cnf, **kwargs)
        for child in self.winfo_children():
            child.configure(cnf, **kwargs)

    @property
    def frame(self):
        return super()

    def handle_key_press(self, key):
        current_text = self.entry.get()
        new_text = current_text + key
        self.entry.delete(0, tk.END)
        self.entry.insert(0, new_text)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Calculator")

    keys = ["7", "8", "9", "/", "4", "5", "6", "*",
            "1", "2", "3", "-", "0", ".", "^", "+"]
    entry_field = tk.Entry(root, font=("Arial", 18))
    entry_field.grid(row=0, column=0, columnspan=4, sticky="nsew")

    keypad = Keypad(root, keynames=keys, columns=4, entry=entry_field)
    keypad.grid(row=1, column=0, columnspan=4, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    for col in range(4):
        root.grid_columnconfigure(col, weight=1)

    root.mainloop()

import tkinter as tk
from tkinter import ttk


class Keypad(tk.Frame):

    def __init__(self, parent, keynames=[], columns=3, entry=None, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.keynames = keynames
        self.entry = entry
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        for i, key in enumerate(self.keynames):
            button = tk.Button(self, text=key, padx=5, pady=5,
                               command=lambda k=key: self.handle_key_press(k))

            row = i // columns
            col = i % columns

            if key in ['+', '-', '*', '/', '^', '=']:
                button.grid(row=row, column=col, sticky=tk.NSEW)
            else:
                button.grid(row=row, column=col, sticky=tk.NSEW)

            self.columnconfigure(col, weight=1)
            self.rowconfigure(row, weight=1)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        for child in self.winfo_children():
            child.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for child in self.winfo_children():
            child[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.winfo_children()[0][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        super().configure(cnf, **kwargs)
        for child in self.winfo_children():
            child.configure(cnf, **kwargs)
    # the the superclass object for this keypad.
    # This is so that a programmer can set properties of a keypad's frame,
    # e.g. keypad.frame.configure(background='blue')

    @property
    def frame(self):
        return super()

    def handle_key_press(self, key):
        current_text = self.entry.get()
        new_text = current_text + key
        self.entry.delete(0, tk.END)
        self.entry.insert(0, new_text)


class CalculatorUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Calculator")

        keys = ["7", "8", "9", "/", "4", "5", "6", "*",
                "1", "2", "3", "-", " ", "0", ".", "C", "^", "+", "="]

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

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
        sizegrip = ttk.Sizegrip(self)
        sizegrip.grid(row=0, column=columns, sticky=tk.NSEW)
        self.columnconfigure(columns, weight=1)

        for i, key in enumerate(self.keynames):
            button = tk.Button(self, text=key, padx=5, pady=5,
                               command=lambda k=key: self.handle_key_press(k))

            row = i // columns
            col = i % columns

            if key in ['+', '-', '*', '/', '^', '=', 'ret']:
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
    # the superclass object for this keypad.
    # This is so that a programmer can set properties of a keypad's frame,
    # e.g. keypad.frame.configure(background='blue')

    @property
    def frame(self):
        return super()

    def handle_key_press(self, key):
        current_text = self.entry.get()

        if key == 'C':
            # Reset the entry field
            self.entry.delete(0, tk.END)
        elif key == '^':
            # Replace '^' with '**' for exponentiation
            new_text = current_text + '**'
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)
        elif key == '=':
            try:
                # Evaluate the expression and update the entry field
                result = eval(current_text.replace('^', '**'))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                # Handle any errors during evaluation
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif key == 'DEL':
            # Delete the last character in the entry field
            new_text = current_text[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)
        elif key == 'ret':
            # Show the previous calculation
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.previous_calculation)
        else:
            # For other operators and digits
            new_text = current_text + key
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)
            self.previous_calculation = current_text

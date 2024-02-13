import tkinter as tk
from tkinter import ttk


# TODO Keypad should extend Frame so that it is a container


class Keypad(tk.Frame):

    def __init__(self, parent, keynames=[], columns=3, **kwargs):
        # TODO call the superclass constructor with all args except
        # keynames and columns
        tk.Frame.__init__(self, parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        for i, key in enumerate(self.keynames):
            button = tk.Button(self, text=key, padx=10, pady=10,
                               command=lambda k=key: self.handle_key_press(k))

            row = i // columns
            col = i % columns

            # Check if the button is an operator (+, -, *, //, **)
            if key in ['+', '-', '*', '//', '**']:
                button.grid(row=row, column=columns - 1, sticky=tk.NSEW)
            else:
                button.grid(row=row, column=col, sticky=tk.NSEW)

        for i in range(columns - 1):
            self.columnconfigure(i, weight=1)
        self.columnconfigure(columns - 1, weight=1)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        # TODO Write a bind method with exactly the same parameters
        # as the bind method of Tkinter widgets.
        # Use the parameters to bind all the buttons in the keypad
        # to the same event handler.
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

    # TODO Write a property named 'frame' the returns a reference to
    # the the superclass object for this keypad.
    # This is so that a programmer can set properties of a keypad's frame,
    # e.g. keypad.frame.configure(background='blue')
    @property
    def frame(self):
        return super()

    def handle_key_press(self, key):
        print(f"Keypad Key pressed: {key}")


if __name__ == '__main__':
    keys = list('789456123 0+*-//**')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

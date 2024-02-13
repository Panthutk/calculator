"""Display the calculator user interface."""
from keypad import Keypad


if __name__ == '__main__':
    # create the UI.  There is no controller (yet), so nothing to inject.
    ui = Keypad()
    # run the UI
    ui.run()

"""Display the calculator user interface."""
from keypad import CalculatorUI


if __name__ == '__main__':
    # create the UI.  There is no controller (yet), so nothing to inject.
    ui = CalculatorUI()
    # run the UI
    ui.run()

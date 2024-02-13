## Files for Lab 6

| file              | For                    |
|-------------------|------------------------|
|`calculator_ui.py` | CalculatorUI, with 2 keypads and display area. |
|`keypad.py`        | Keypad class           |
|`main.py`          | script to start the UI |

Create `calculator_ui.py` yourself. 
Write your solution to problems 1 and 2 in this file.

Then implement a Keypad component in `keypad.py`,
as described on Google Classroom for week 6.

## Keypad Component

A configurable keypad written using tkinter. 
Keypad behaves like a tkinter component.

To create a 2x2 keypad use:
```python
keys = ['1','2','3','4']

keypad = Keypad(parent, keynames=keys, columns=2)
```
If there are not enough keys to fill all grid cells,
then leave some grid cells empty.

To bind key presses to an event handler use (for example):
```python
def key_handler(event):
    key = event.widget['text']
    print("You pressed", key)

keypad.bind("<Button-1>", key_handler)
```

This code should bind *all* the keys to the same event handler.


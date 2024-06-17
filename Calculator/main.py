from tkinter import *

def on_button_press(num):
    global equation_str
    equation_str = equation_str + str(num)
    equation_var.set(equation_str)

def on_equals():
    global equation_str
    try:
        result = str(eval(equation_str))
        equation_var.set(result)
        equation_str = result
    except SyntaxError:
        equation_var.set("Syntax Error")
        equation_str = ""
    except ZeroDivisionError:
        equation_var.set("Division by Zero")
        equation_str = ""

def on_clear():
    global equation_str
    equation_var.set("")
    equation_str = ""

window = Tk()
window.title("Simple Calculator")
window.geometry("500x500")

equation_str = ""
equation_var = StringVar()

label = Label(window, textvariable=equation_var, font=('consolas', 20), bg="grey", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

buttons = [
    Button(frame, text='1', height=4, width=9, font=35, command=lambda: on_button_press(1)),
    Button(frame, text='2', height=4, width=9, font=35, command=lambda: on_button_press(2)),
    Button(frame, text='3', height=4, width=9, font=35, command=lambda: on_button_press(3)),
    Button(frame, text='4', height=4, width=9, font=35, command=lambda: on_button_press(4)),
    Button(frame, text='5', height=4, width=9, font=35, command=lambda: on_button_press(5)),
    Button(frame, text='6', height=4, width=9, font=35, command=lambda: on_button_press(6)),
    Button(frame, text='7', height=4, width=9, font=35, command=lambda: on_button_press(7)),
    Button(frame, text='8', height=4, width=9, font=35, command=lambda: on_button_press(8)),
    Button(frame, text='9', height=4, width=9, font=35, command=lambda: on_button_press(9)),
    Button(frame, text='0', height=4, width=9, font=35, command=lambda: on_button_press(0)),
    Button(frame, text='+', height=4, width=9, font=35, command=lambda: on_button_press('+')),
    Button(frame, text='-', height=4, width=9, font=35, command=lambda: on_button_press('-')),
    Button(frame, text='*', height=4, width=9, font=35, command=lambda: on_button_press('*')),
    Button(frame, text='/', height=4, width=9, font=35, command=lambda: on_button_press('/')),
    Button(frame, text='=', height=4, width=9, font=35, command=on_equals),
]

button_positions = [
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2),
    (3, 0), (3, 1), (3, 2),
    (0, 3), (1, 3), (2, 3),
    (3, 3)
]

for i, button in enumerate(buttons):
    button.grid(row=button_positions[i][0], column=button_positions[i][1])

clear_button = Button(window, text='Clear', height=4, width=12, font=35, command=on_clear)
clear_button.pack()

window.mainloop()

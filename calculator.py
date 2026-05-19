from tkinter import *

# ---------------- WINDOW ---------------- #

root = Tk()

root.title("Modern Calculator")

root.geometry("420x720")

root.configure(bg="black")

# ---------------- DISPLAY ---------------- #

entry = Entry(
    root,
    font=("Poppins", 40, "bold"),
    bg="black",
    fg="white",
    bd=0,
    justify=RIGHT,
    insertbackground="white"
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=20,
    pady=30,
    ipady=40
)

# ---------------- FUNCTIONS ---------------- #

def click(value):

    current = entry.get()

    entry.delete(0, END)

    entry.insert(END, current + str(value))


def clear():

    entry.delete(0, END)


def backspace():

    current = entry.get()

    entry.delete(0, END)

    entry.insert(0, current[:-1])


def calculate():

    try:

        expression = entry.get()

        expression = expression.replace('÷', '/')

        expression = expression.replace('×', '*')

        result = eval(expression)

        entry.delete(0, END)

        entry.insert(0, result)

    except:

        entry.delete(0, END)

        entry.insert(0, "Error")


# ---------------- BUTTON STYLE ---------------- #

button_font = ("Poppins", 22, "bold")

# ---------------- BUTTONS ---------------- #

buttons = [

    ('AC', 1, 0, '#5c5470'),
    ('⌫', 1, 1, '#5c5470'),
    ('+/-', 1, 2, '#5c5470'),
    ('÷', 1, 3, '#7b6d9c'),

    ('7', 2, 0, '#2f2b36'),
    ('8', 2, 1, '#2f2b36'),
    ('9', 2, 2, '#2f2b36'),
    ('×', 2, 3, '#7b6d9c'),

    ('4', 3, 0, '#2f2b36'),
    ('5', 3, 1, '#2f2b36'),
    ('6', 3, 2, '#2f2b36'),
    ('-', 3, 3, '#7b6d9c'),

    ('1', 4, 0, '#2f2b36'),
    ('2', 4, 1, '#2f2b36'),
    ('3', 4, 2, '#2f2b36'),
    ('+', 4, 3, '#7b6d9c'),

    ('%', 5, 0, '#2f2b36'),
    ('0', 5, 1, '#2f2b36'),
    ('.', 5, 2, '#2f2b36'),
    ('=', 5, 3, '#cbb4ff')

]

# ---------------- CREATE BUTTONS ---------------- #

for (text, row, col, color) in buttons:

    if text == 'AC':

        command = clear

    elif text == '⌫':

        command = backspace

    elif text == '=':

        command = calculate

    elif text == '+/-':

        command = lambda: click('-')

    else:

        command = lambda t=text: click(t)

    button = Button(

        root,

        text=text,

        bg=color,

        fg="white",

        activebackground=color,

        activeforeground="white",

        font=button_font,

        bd=0,

        relief=FLAT,

        command=command
    )

    button.grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=10,
        pady=10,
        ipadx=10,
        ipady=20
    )

# ---------------- RESPONSIVE GRID ---------------- #

for i in range(6):

    root.grid_rowconfigure(i, weight=1)

for j in range(4):

    root.grid_columnconfigure(j, weight=1)

# ---------------- RUN ---------------- #

root.mainloop()
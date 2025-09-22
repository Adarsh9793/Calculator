
from tkinter import *

# Step 1: GUI setup
window = Tk()
window.geometry("300x400")
window.title("Simple Calculator")

# Step 2: Entry box
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# Step 3: Button click logic
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

# Step 4: Operation functions
def add():
    global i, math
    i = int(e.get())
    math = "addition"
    e.delete(0, END)

def sub():
    global i, math
    i = int(e.get())
    math = "subtraction"
    e.delete(0, END)

def mult():
    global i, math
    i = int(e.get())
    math = "multiplication"
    e.delete(0, END)

def div():
    global i, math
    i = int(e.get())
    math = "division"
    e.delete(0, END)

def equal():
    n2 = int(e.get())
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + n2)
    elif math == "subtraction":
        e.insert(0, i - n2)
    elif math == "multiplication":
        e.insert(0, i * n2)
    elif math == "division":
        e.insert(0, i / n2)

def clear():
    e.delete(0, END)

# Step 5: Buttons
buttons = [
    ('1', 10, 60), ('2', 80, 60), ('3', 170, 60),
    ('4', 10, 120), ('5', 80, 120), ('6', 170, 120),
    ('7', 10, 180), ('8', 80, 180), ('9', 170, 180),
    ('0', 10, 240)
]

for (text, x, y) in buttons:
    Button(window, text=text, width=12, command=lambda t=text: click(t)).place(x=x, y=y)

Button(window, text='+', width=12, command=add).place(x=80, y=240)
Button(window, text='-', width=12, command=sub).place(x=170, y=240)
Button(window, text='*', width=12, command=mult).place(x=10, y=300)
Button(window, text='/', width=12, command=div).place(x=80, y=300)
Button(window, text='=', width=12, command=equal).place(x=170, y=300)
Button(window, text='Clear', width=12, command=clear).place(x=10, y=350)

# Step 6: Main loop
window.mainloop()
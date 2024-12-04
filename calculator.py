from tkinter import *
from tkmacosx import Button  # Importing the tkmacosx Button
from tkinter import PhotoImage

# Initialize main window
me = Tk()
me.geometry("350x480")
me.title("CALCULATOR")
me.iconphoto(True, PhotoImage(file='/Users/subhamrakshit/Desktop/coding/GUI/calculator-tkinter/calc-icon.png'))
me.config(background='#1E1E2F')  # Deep dark blue-gray

# Label for Title
Label(me, text="CALCULATOR", bg='#1E1E2F', fg='#F5F5F5', font=("Helvetica", 24, 'bold')).pack(side=TOP, pady=10)

# Input field
textin = StringVar()
operator = ""

# Functions
def clickbut(number):
    """Handles number or operator button click."""
    global operator
    operator += str(number)
    textin.set(operator)

def equlbut():
    """Evaluates the expression."""
    global operator
    try:
        result = str(eval(operator))
        textin.set(result)
        operator = ""
    except Exception:
        textin.set("Error")
        operator = ""

def clrbut():
    """Clears the input field."""
    global operator
    operator = ""
    textin.set("")

# Input entry field
Entry(
    me, font=("Courier New", 16, 'bold'), textvar=textin, width=20, bd=5,
    bg='#292A36', fg='#FFFFFF', justify='right', insertbackground='#FFFFFF'
).pack(pady=10)

# Buttons configuration
buttons = [
    ('1', 10, 120), ('2', 90, 120), ('3', 170, 120), ('+', 250, 120),
    ('4', 10, 190), ('5', 90, 190), ('6', 170, 190), ('-', 250, 190),
    ('7', 10, 260), ('8', 90, 260), ('9', 170, 260), ('*', 250, 260),
    ('0', 10, 330), ('.', 90, 330), ('/', 170, 330), ('CE', 250, 330),
    ('=', 10, 400)
]

# Colors
digit_bg = '#4CAF50'  # Green
digit_fg = '#FFFFFF'
op_bg = '#2196F3'  # Blue
op_fg = '#FFFFFF'
clr_bg = '#F44336'  # Red
clr_fg = '#FFFFFF'
eq_bg = '#FF9800'  # Orange
eq_fg = '#FFFFFF'

# Create and place buttons dynamically using tkmacosx Button
for (text, x, y) in buttons:
    if text == "=":
        Button(
            me, text=text, width=320, height=60, bg=eq_bg, fg=eq_fg,
            activebackground='#FF7700', activeforeground='#FFFFFF', command=equlbut,
            font=("Courier New", 16, 'bold')
        ).place(x=x, y=y)
    elif text == "CE":
        Button(
            me, text=text, width=80, height=60, bg=clr_bg, fg=clr_fg,
            activebackground='#FF5733', activeforeground='#FFFFFF', command=clrbut,
            font=("Courier New", 16, 'bold')
        ).place(x=x, y=y)
    else:
        bg_color = digit_bg if text.isdigit() else op_bg
        Button(
            me, text=text, width=80, height=60, bg=bg_color, fg=digit_fg,
            activebackground='#388E3C' if text.isdigit() else '#1976D2',
            activeforeground='#FFFFFF', command=lambda t=text: clickbut(t),
            font=("Courier New", 16, 'bold')
        ).place(x=x, y=y)

# Run the main loop
me.mainloop()

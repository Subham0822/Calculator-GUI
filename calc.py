from tkinter import *

# Initialize main window
me = Tk()
me.geometry("366x460")
me.title("CALCULATOR")
me.config(background='#2D2D2D')  # Dark gray-blue

# Label
Label(me, text="CALCULATOR", bg='#2D2D2D', fg='#FFFFFF', font=("Times", 30, 'bold')).pack(side=TOP)

# Input field
textin = StringVar()
operator = ""

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
    except Exception as e:
        textin.set("Error")
        operator = ""

def clrbut():
    """Clears the input field."""
    global operator
    operator = ""
    textin.set("")

# Input entry field
Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='#E0E0E0', fg='#000000').pack()

# Buttons configuration
buttons = [
    ('1', 10, 100), ('2', 75, 100), ('3', 140, 100),
    ('4', 10, 170), ('5', 75, 170), ('6', 140, 170),
    ('7', 10, 240), ('8', 75, 240), ('9', 140, 240),
    ('0', 10, 310), ('.', 75, 310),
    ('+', 205, 100), ('-', 205, 170),
    ('*', 205, 240), ('/', 205, 310),
    ('CE', 270, 100), ('=', 10, 380)
]

# Colors
digit_bg = '#4CAF50'  # Green
digit_fg = '#4169E1'  # Royal Blue
op_bg = '#2196F3'  # Blue
op_fg = '#4169E1'  # Royal Blue
clr_bg = '#F44336'  # Red
clr_fg = '#4169E1'  # Royal Blue
eq_bg = '#FF9800'  # Orange
eq_fg = '#4169E1'  # Royal Blue

# Create and place buttons dynamically
for (text, x, y) in buttons:
    if text == "=":
        Button(me, text=text, padx=151, pady=14, bd=4, bg=eq_bg, fg=eq_fg, command=equlbut,
               font=("Courier New", 16, 'bold')).place(x=x, y=y)
    elif text == "CE":
        Button(me, text=text, padx=14, pady=119, bd=4, bg=clr_bg, fg=clr_fg, command=clrbut,
               font=("Courier New", 16, 'bold')).place(x=x, y=y)
    elif text == ".":
        Button(me, text=text, padx=47, pady=14, bd=4, bg=digit_bg, fg=digit_fg, command=lambda t=text: clickbut(t),
               font=("Courier New", 16, 'bold')).place(x=x, y=y)
    else:
        bg_color = digit_bg if text.isdigit() else op_bg
        Button(me, text=text, padx=14, pady=14, bd=4, bg=bg_color, fg=op_fg, command=lambda t=text: clickbut(t),
               font=("Courier New", 16, 'bold')).place(x=x, y=y)

# Run the main loop
me.mainloop()

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("CALCULATOR")
window.geometry("320x450")
window.configure(background="pink")
window.resizable(width=False, height=False)


def click(value):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(value))


def clear():
    display.delete(0, END)

def backspace():
    current = display.get()
    display.delete(0, END)
    display.insert(0, current[:-1])

def calculate():
    try:
        expression = display.get()
        result = eval(expression)

        display.delete(0, END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        display.delete(0, END)
    except:
        messagebox.showerror("Error", "Invalid expression")
        display.delete(0, END)

display = Entry(
    window,
    font=("Arial", 24),
    borderwidth=5,
    relief="ridge",
    justify="right", width=15,
)

display.grid(row=0, column=0, columnspan=4, padx=10, pady=15)


button1 = Button(text="1", command= lambda  t = "1":click (t), width=6, height=3)
button1.grid(row=1, column=0, padx=10, pady=8)

button2 = Button(text="2", command= lambda t = "2":click(t), width=6, height=3)
button2.grid(row=1, column=1)

button3 = Button(text="3", command= lambda t = "3":click(t), width=6, height=3)
button3.grid(row=1, column=2)

button4 = Button(text="4", command= lambda t = "4":click(t), width=6, height=3)
button4.grid(row=2, column=0, padx=10, pady=8)

button5 = Button(text="5", command= lambda t = "5":click(t), width=6, height=3)
button5.grid(row=2, column=1)

button6 = Button(text="6", command= lambda t = "6":click(t), width=6, height=3)
button6.grid(row=2, column=2)

button7 = Button(text="7", command= lambda t = "7":click(t), width=6, height=3)
button7.grid(row=3, column=0, padx=10, pady=8)

button8 = Button(text="8", command= lambda t = "8":click(t), width=6, height=3)
button8.grid(row=3, column=1)

button9 = Button(text="9", command= lambda t = "9":click(t), width=6, height=3)
button9.grid(row=3, column=2)

button_multiply = Button(text="*", command= lambda t = "*":click(t), width=6, height=3)
button_multiply.grid(row=1, column=3, padx=10, pady=8)

button_divide = Button(text="/", command= lambda t = "/":click(t), width=6, height=3)
button_divide.grid(row=4, column=3)

button_subtract = Button(text="-", command= lambda t = "-":click(t), width=6, height=3)
button_subtract.grid(row=3, column=3)

button_add = Button(text="+", command= lambda t = "+":click(t), width=6, height=3)
button_add.grid(row=2, column=3)

button_equal = Button(text="=", command=calculate, width=15, height=2)
button_equal.grid(row=5, column=1, columnspan=2, padx=10, pady=10)


button10 = Button(text="0", command= lambda t = "0":click(t), width=6, height=3)
button10.grid(row=4, column=1)

button_clear = Button(text="C", command=clear, width=6, height=3)
button_clear.grid(row=4, column=0, padx=10, pady=8)

button_delete = Button(text="⌫", command=backspace, width=6, height=3)
button_delete.grid(row=4, column=2)


window.mainloop()
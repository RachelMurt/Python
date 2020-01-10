from tkinter import *
import math, operator, parser
from decimal import *

window = Tk()
window.title("Calculator")
window.geometry("240x400")
window.configure(background = "azure3")

total = 0
query = []

operator_index = {"+": operator.add, "-": operator.sub, "x": operator.mul, "/": operator.__truediv__ }

def clear_all():
    global query
    display.delete(0, END)
    query = []

def refresh_display():
    global query
    display.delete(0, END)
    disptext = ""
    for x in range(len(query)):
        disptext = disptext + str(query[x])

    display.insert(1, disptext)

def variables(num):
    global total, query
    display.insert(total, num)
    total += 1

    query = query + [num]
    refresh_display()

def operation(operator):
    global total, query
    length = len(operator)
    display.insert(total, operator)
    total +=length
    query = query + [operator]
    refresh_display()

def back():
    whole_string = display.get()
    if len(whole_string):
        new = whole_string[:-1]
        clear_all()
        display.insert(0, new)
    else:
        clear_all()
        display.insert(0, "Error, please press C")

def answer():
    global query, total, operator_index, diplay

    var = []
    operators = []

    for x in range(len(query)):
        if query[x] == "+" or query[x] == "-" or query[x] == "x" or query[x] == "/":
            operators = operators + [query[x]]
        else:
            var = var + [query[x]]
    
    result = Decimal(var[0])
    
    for y in range(len(operators)):
        result = round(operator_index[operators[y]](result,Decimal(var[y+1])),5)

    query = []
    clear_all()
    display.insert(total," = " + str(result))

#calculator buttons grid

#answer box
display = StringVar()
display = Entry(text = (total), justify = RIGHT, fg = "black", bg = "white", font=("Helvetica", 16))
display.place(x = 10, y = 20, width = 220, height = 50)

#bg
spacefill = Label(text = " ", fg = "black", bg = "azure4")
spacefill.place(x = 5, y = 85, width = 230, height = 275)

#MC
MCbtn = Button(text = "MC", fg = "black", bg = "white", font = 20)
MCbtn.place(x = 10, y = 90, width = 40, height = 40)

#MR
MRbtn = Button(text = "MR",fg = "black", bg = "white", font = 20)
MRbtn.place(x = 55, y = 90, width = 40, height = 40)

#MS
MSbtn = Button(text = "MS",fg = "black", bg = "white", font = 20)
MSbtn.place(x = 100, y = 90, width = 40, height = 40)

#Back Arrow
arrowbtn = Button(text = " ← ", fg = "black", bg = "white", font = 20, command = back)
arrowbtn.place(x = 10, y = 135, width = 40, height = 40)

#CE
CEbtn = Button(text = "CE",fg = "black", bg = "white", font = 20)
CEbtn.place(x = 55, y = 135, width = 40, height = 40)

#Clear
Cbtn = Button(text = "C",fg = "black", bg = "white", font = 20, command = clear_all)
Cbtn.place(x = 100, y = 135, width = 40, height = 40)

#Plus/Minus
plusminusbtn = Button(text = "±", fg = "black", bg = "white", font = 20)
plusminusbtn.place(x = 145, y = 135, width = 40, height = 40)

#Square Root
squarerootbtn = Button(text = "√", fg = "black", bg = "white", font = 20)
squarerootbtn.place(x = 190, y = 135, width = 40, height = 40)

#seven
sevenbtn = Button(text = "7", fg = "black", bg = "white", font = 20, command = lambda: variables(7))
sevenbtn.place(x = 10, y = 180, width = 40, height = 40)

#eight
eightbtn = Button(text = "8", fg = "black", bg = "white", font = 20, command = lambda: variables(8))
eightbtn.place(x = 55, y = 180, width = 40, height = 40)

#nine
ninebtn = Button(text = "9", fg = "black", bg = "white", font = 20, command = lambda: variables(9))
ninebtn.place(x = 100, y = 180, width = 40, height = 40)

#divide
dividebtn = Button(text = "/", fg = "black", bg = "white", font = 20, command = lambda: operation("/"))
dividebtn.place(x = 145, y = 180, width = 40, height = 40)

#percentage
percentbtn = Button(text = "%", fg = "black", bg = "white", font = 20)
percentbtn.place(x = 190, y = 180, width = 40, height = 40)

#four
fourbtn = Button(text = "4", fg = "black", bg = "white", font = 20, command = lambda: variables(4))
fourbtn.place(x = 10, y = 225, width = 40, height = 40)

#five
fivebtn = Button(text = "5", fg = "black", bg = "white", font = 20, command = lambda: variables(5))
fivebtn.place(x = 55, y = 225, width = 40, height = 40)

#six
sixbtn = Button(text = "6", fg = "black", bg = "white", font = 20, command = lambda: variables(6))
sixbtn.place(x = 100, y = 225, width = 40, height = 40)

#multiply
multiplybtn = Button(text = "X", fg = "black", bg = "white", font = 20, command = lambda: operation("x"))
multiplybtn.place(x = 145, y = 225, width = 40, height = 40)

#one
onebtn = Button(text = "1", fg = "black", bg = "white", font = 20, command = lambda: variables(1))
onebtn.place(x = 10, y = 270, width = 40, height = 40)

#two
twobtn = Button(text = "2", fg = "black", bg = "white", font = 20, command = lambda: variables(2))
twobtn.place(x = 55, y = 270, width = 40, height = 40)

#three
threebtn = Button(text = "3", fg = "black", bg = "white", font = 20, command = lambda: variables(3))
threebtn.place(x = 100, y = 270, width = 40, height = 40)

#minus
minusbtn = Button(text = "-", fg = "black", bg = "white", font = 20, command = lambda: operation("-"))
minusbtn.place(x = 145, y = 270, width = 40, height = 40)

#equals
equalsbtn = Button(text = "=", fg = "black", bg = "white", font = 20, command = lambda: answer())
equalsbtn.place(x = 190, y = 270, width = 40, height = 85)

#zero
zerobtn = Button(text = "0", fg = "black", bg = "white", font = 20, command = lambda: variables(0))
zerobtn.place(x = 10, y = 315, width = 85, height = 40)

#decimal
decimalbtn = Button(text = ".", fg = "black", bg = "white", font = 20)
decimalbtn.place(x = 100, y = 315, width = 40, height = 40)

#add
addbtn = Button(text = "+", fg = "black", bg = "white", font = 20, command = lambda: operation("+"))
addbtn.place(x = 145, y = 315, width = 40, height = 40)

#exit
exitbtn = Button(text = "Exit", fg = "black", bg = "indian red", font = 20)
exitbtn.place(x = 10, y = 360, width = 85, height = 40)

#help
helpbtn = Button(text = "Help", fg = "black", bg = "lawn green", font = 20)
helpbtn.place(x =145 , y = 360, width = 85, height = 40)


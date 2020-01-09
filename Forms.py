# Forms Example

from tkinter import *

# define procedures
def click(char):
    display.set(char)

# create the window
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.title("window")

# create main display label
display = StringVar()
label = Label(window, textvariable=display, fg="black", bg="grey", width=13, font=("Helvetica", 18), anchor=E).grid(row=0, column=0, columnspan=3)
display.set("0")

# create buttons using a grid
buttonA = Button(window, text="A", fg="blue", command=lambda: click("A"), width=8, font=("Helvetica", 16)).grid(row=1, column=0, columnspan=2)
buttonB = Button(window, text="B", fg="blue", command=lambda: click("B"), width=3, font=("Helvetica", 16)).grid(row=2, column=0)
buttonC = Button(window, text="C", fg="blue", command=lambda: click("C"), width=3, font=("Helvetica", 16)).grid(row=2, column=1)
buttonD = Button(window, text="D", fg="blue", command=lambda: click("D"), width=3, height=3, font=("Helvetica", 16)).grid(row=1, column=2, rowspan=2)

# start the event loop
window.mainloop()

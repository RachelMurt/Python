from tkinter import *
import csv
import time
import math, operator, parser
from decimal import *

# globally declare the expression variable 
expression = ""
# Function to update expressiom 
# in the text entry box 
def press(num):
    # point out the global expression variable
    global expression
    # concatenation of string
    expression = expression + str(num)
    # update the expression by using set method
    equation.set(expression) 
  
# Function to evaluate the final expression 
def equalpress():
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
    # Put that code inside the try block 
    # which may generate the error
    try:
        global expression 
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression))
        equation.set(total) 
        # initialze the expression variable 
        # by empty string 
        expression = "" 
    # if error is generate then handle 
    # by the except block 
    except:
        equation.set(" error ")
        expression = "" 
  

# Function to clear the contents 
# of text entry box 
def clear():
    global expression
    expression = ""
    equation.set("")


#Standard calculator window
def gui():
    gui = Tk()
    gui.title("Calculator") #Naming window
    gui.geometry("230x320") #Size of window
    gui.configure (background = "grey") #Changing background colour
    equation = StringVar() 
    # create the text entry box for 
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation) 
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=4, ipadx=70) 
    equation.set('enter your expression') 
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='red',command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='red',command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='red',command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='red',command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='red',command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='red',command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='red',command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='red',command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='red',command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='black', bg='red',command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='red',command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' * ', fg='black', bg='red',command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', fg='black', bg='red',command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='black', bg='red',command=lambda:equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='Clear', fg='black', bg='red',command=lambda:clear, height=1, width=7) 
    clear.grid(row=5, column=1)
    # start the GUI
    gui.mainloop()

#Creating help centre 
    def helpcentre():
        helpwindow = Toplevel()
        helpwindow.title("Help Centre") #Naming window
        helpwindow.geometry("620x770") #Creating size of window
        helpwindow.configure (background = "Grey") #Changing background colour

        logo = PhotoImage(file="Calc.png") #Inserting company logo
        logoimage = Label(helpwindow, image=logo) #Helpwindow is placed here so everything goes on the top layer
        logoimage.place(x = 1, y = 1, width=650, height=750) #Where logo is positioned

        #Creating close window function
        def close_window():
            helpwindow.destroy()

        #Creating exit button
        button7 = Button(helpwindow, text = "Exit", command = close_window) #Creating text on button and calling close window function
        button7.place(x = 470, y = 710, width=140, height=45) #Creating size of button and positioning it
        button7.configure (background = "snow") #Changing background colour

        helpwindow.mainloop()

    frame = Frame(window)
    frame.pack()
#######################
    
#Help and close buttons
    
#######################
    
    #Help button
    button13= Button(calwindow, text = "Help", command = lambda: helpcentre(), font=15) #Creating text on box and calling helpcentre function
    button13.place(x=145, y= 280, width =80,height = 35) #Creating size of button and positioning it
    button13.configure (background = "orange") #Changing background colour

    calwindow.mainloop()   

#######################################################################################################################

#Mortgage calculator

def mortgagecalculator():
    morwindow = Tk()
    morwindow.title("Mortgage") #Naming window
    morwindow.geometry("400x350") #Size of window
    morwindow.configure (background = "grey") #Changing background colour

    total=0 #Setting total to 0
    #Creating calculate function
    def calculate():
        global total
        down = downpaymentbox.get()
        down = float(down)
        purchase = purchasepricebox.get()
        purchase = float(purchase)
        term = termbox.get()
        term = float(term)
        interest = interestratebox.get()
        interest = float(interest)
        newsum = (purchase) - (down)
        newsum2 = (newsum) / 100
        newsum3 = (newsum2) * (100 + (interest))
        total = (newsum3) / ((term) * 12)
        totalbox["text"] = "£{0:.2f}".format(total) #Changing format of answer so it has pound sign in front and goesto 2 decimal places

    #Creating close window function
    def close_window():
        morwindow.destroy()

    #Creating help centre 
    def helpcentre():
        helpwindow = Toplevel()
        helpwindow.title("Help Centre") #Naming window
        helpwindow.geometry("620x760") #Creating size of window
        helpwindow.configure (background = "Grey") #Changing background colour

        logo = PhotoImage(file="Mort.png") #Inserting company logo
        logoimage = Label(helpwindow, image=logo) #Helpwindow is placed here so everything goes on the top layer
        logoimage.place(x = 1, y = 1, width=600, height=700) #Where logo is positioned

        #Creating close window function
        def close_window():
            helpwindow.destroy()

        #Creating exit button
        button7 = Button(helpwindow, text = "Exit", command = close_window) #Creating text on button and calling close window function
        button7.place(x = 470, y = 710, width=140, height=45) #Creating size of button and positioning it
        button7.configure (background = "snow") #Changing background colour

        helpwindow.mainloop()
           



    frame = Frame(window)
    frame.pack()

    #Creating title 
    titlelbl = Label(morwindow, text = "Mortgage Calculator", font =40) #Creating text on label
    titlelbl.place(x = 16, y = 15) #placing title
    titlelbl.configure (background ="grey", font=("Courier",23 )) #Changing backgorund colour and font

    #Creating purchase prise label
    purchasepricelbl = Label(morwindow, text = "Purchase Price ", font =30) #Creating text on label
    purchasepricelbl.place(x = 30, y = 90, width=180, height=25) #Creating size and position of button
    purchasepricelbl.configure (background ="grey") #Changing background colour

    #Creatingpurchase price entry box
    purchasepricebox = Entry(morwindow, text = "")
    purchasepricebox.place(x = 200, y = 90, width=120, height=25) #Creating size and position of button
    purchasepricebox.focus() #Creating the button to already to be focused on this box


    #Creating down payment label
    downpaymentlbl = Label(morwindow, text = " Down Payment ", font =30) #Creating text on label
    downpaymentlbl.place(x = 26, y = 120, width=180, height=25) #Creating size and position of button
    downpaymentlbl.configure (background ="grey")

    #Creating down payment box
    downpaymentbox = Entry(morwindow, text = "")
    downpaymentbox.place(x = 200, y = 120, width=120, height=25) #Creating size and position of button


    #Creating term (years) label
    termlbl = Label(morwindow, text = "Term (years)", font =30) #Creating text on label
    termlbl.place(x = 16, y = 150, width=180, height=25) #Creating size and position of button
    termlbl.configure (background ="grey")

    #Creating term (years) box
    termbox = Entry(morwindow, text = "")
    termbox.place(x = 200, y = 150, width=120, height=25) #Creating size and position of button


    #Creating interest rate label
    interestratelbl = Label(morwindow, text = "Interest rate(%)", font =30) #Creating text on label
    interestratelbl.place(x = 26, y = 180, width=180, height=25) #Creating size and position of button
    interestratelbl.configure (background ="grey") #Changing background colour

    #Creating interest rate box
    interestratebox = Entry(morwindow, text = "")
    interestratebox.place(x = 200, y = 180, width=120, height=25) #Creating size and position of button

    #Calculate button
    calculatelst = Button(morwindow, text = "Calculate", command = lambda: calculate(), fg = "black", bg ="white") #Creating text on label and calling on fucntion calculate
    calculatelst.place(x = 150, y = 230, width=100, height=25) #Creating size and position of button

    #Total box
    display = StringVar()
    totalbox = Label(morwindow, text = "£{0:.2f}".format(total), fg = "black", bg = "white", font=30) #Setting total box to display pound sign and 2 decimal points
    totalbox.place(x=130, y = 270, width = 150, height = 25) #Creating size and position of button
    display.set("0") #Creating the total box to display 0

    #Help button
    helpbutton=Button(morwindow, text = "Help", command = lambda: helpcentre(), font=40) #Creating text on label and calling the function help centre
    helpbutton.place(x= 40, y = 300, width = 60, height = 30) #Creating size and position of button
    helpbutton.configure (background = "orange") #Changing colour of background

    #Close button
    closebutton=Button(morwindow, text = "Close", command = lambda: close_window(), font=40)  #Creating text on label and calling the function close window
    closebutton.place(x= 300, y = 300, width = 60, height = 30) #Creating size and position of button
    closebutton.configure (background = "snow") #Changing colour of background


    window.mainloop()




########################################################################


#Vehicle lease calculator

def vehiclelease():
    vehwindow = Tk()
    vehwindow.title("Vehicle Lease") #Naming window
    vehwindow.geometry("400x380") #Creating size of window
    vehwindow.configure (background = "grey") #Changing colour of background


    total=0

    #Creating calculate function
    def calculate():
        global total
        leasevalue = leasevaluebox.get()
        leasevalue = float(leasevalue)
        leaseperiod = leaseperiodbox.get()
        leaseperiod = float(leaseperiod)
        residualvalue = residualvaluebox.get()
        residualvalue = float(residualvalue)
        interestrate = interestratebox.get()
        interestrate = float(interestrate)
        lvfrv = ((leasevalue-residualvalue)/leaseperiod)
        totalveh = (lvfrv * (interestrate / 100 +1))
        total=totalveh           
        totalbox["text"] = "£{0:.2f}".format(total) #Formating answer so it has pound sign with 2 decimal places

    #Creating cloe window function
    def close_window():
        vehwindow.destroy()

    #Creating helpcentre fucntion
    def helpcentre():
        helpwindow = Toplevel()
        helpwindow.title("Help Centre") #Naming window
        helpwindow.geometry("630x770") #Creating size of window
        helpwindow.configure (background = "orange") #Changing background colour

        logo = PhotoImage(file="Veh.png") #Inserting company logo
        logoimage = Label(helpwindow, image=logo) #Help window is placed here so everything goes on the top layer
        logoimage.place(x = 1, y = 1, width=620, height=700) #Where logo is positioned

        #Creating close window function
        def close_window():
            helpwindow.destroy()

        #Creating exit button
        button7 = Button(helpwindow, text = "Exit", command = close_window)  #Creating text on label and calling the function close window
        button7.place(x = 470, y = 710, width=140, height=45) #Creating size and position of button
        button7.configure (background = "snow") #Changing background colour       



        helpwindow.mainloop()
           



    frame = Frame(window)
    frame.pack()

    #Creating title
    titlelbl = Label(vehwindow, text = "Vehicle Lease", font = 25) #Creating text of label
    titlelbl.place(x = 70, y = 20) #Placing title
    titlelbl.configure (background ="grey", font=("Courier",24 )) #Changing backgorund and font

    #Creating label for lease value
    leasevaluelbl = Label(vehwindow, text = "Lease value", font=30) #Creating text of label
    leasevaluelbl.place(x = 18, y = 90, width=180, height=25) #Positioning and creating size
    leasevaluelbl.configure (background = "grey") #Changing background colour
    #Creating entry box for lease value
    leasevaluebox = Entry(vehwindow, text = "")
    leasevaluebox.place(x = 200, y = 90, width=120, height=25) #Creating size and position of button
    leasevaluebox.focus() #Making the mouse focused on this box

    #Creating label for lease period
    leaseperiodlbl = Label(vehwindow, text = "Lease period", font=30) #Creating text of label
    leaseperiodlbl.place(x = 22, y = 130, width=180, height=25) #Creating size and position of button
    leaseperiodlbl.configure (background = "grey") #Changing background colour

    #Creating entry box for lease period
    leaseperiodbox = Entry(vehwindow, text = "")
    leaseperiodbox.place(x = 200, y = 130, width=120, height=25) #Creating size and position of button


    #Creating label for lease period
    residualvaluelbl = Label(vehwindow, text = "Residual value", font=30) #Creating text of label
    residualvaluelbl.place(x = 25, y = 170, width=180, height=25) #Creating size and position of button
    residualvaluelbl.configure (background = "grey") #Changing background colour

    #Creating entry box for residual value
    residualvaluebox = Entry(vehwindow, text = "")
    residualvaluebox.place(x = 200, y = 170, width=120, height=25) #Creating size and position of button

    #Creating label interest rate
    interestratelbl = Label(vehwindow, text = "Interest rate (%)", font=30) #Creating text of label
    interestratelbl.place(x =50, y = 210, width=140, height=25) #Creating size and position of button
    interestratelbl.configure (background = "grey") #Changing background colour

    #Creating entry box for interest rate
    interestratebox = Entry(vehwindow, text = "")
    interestratebox.place(x = 200, y = 210, width=120, height=25) #Creating size and position of button

    #Calculate button
    calculatelst = Button(vehwindow, text = "Calculate", command = lambda: calculate()) #Creating text of label and calling calculate function
    calculatelst.place(x = 150, y = 260, width=100, height=25) #Creating size and position of button
    calculatelst.configure (background = "grey") #Changing background colour

    #Total box
    display = StringVar()
    totalbox = Label(vehwindow, text = "£{0:.2f}".format(total), fg = "black", bg = "white", font=30) #Formatting label so it diplays pound sign and 2 decimal places
    totalbox.place(x=135, y = 300, width = 130, height = 25) #Creating size and position of button
    display.set("0") #Creating the display box to show 0


    #Help button
    helpbutton=Button(vehwindow, text = "Help", command = lambda: helpcentre(), font=40) #Creating text of label and calling function of help centre
    helpbutton.place(x= 60, y = 335, width = 60, height = 30) #Creating size and position of button
    helpbutton.configure (background = "orange") #Changing background colour

    #closebutton
    closebutton=Button(vehwindow, text = "Close", command = lambda: close_window(), font=40) #Creating text of label and calling 
    closebutton.place(x= 275, y = 335, width = 60, height = 30) #Creating size and position of button
    closebutton.configure (background = "snow") #Changing background colour

    window.mainloop()








#######################################################################################################################################################

#Fuel economy

#Creating fucntion for fuel economy
def fueleconomy():
    fuelwindow = Tk()
    fuelwindow.title("Fuel Economy") #Naming window
    fuelwindow.geometry("370x325") #Changing size of window
    fuelwindow.configure (background = "grey") #Changing background colour


    total = 0 #Setting the total to 0

    #Creating fucntion for calcualte
    def calculate():
        global total
        distance = distancebox.get()
        distance = float(distance)
        fuel = fuelusedbox.get()
        fuel = float(fuel)
        total = distance/fuel
        totalbox["text"] = ("%.2f" % total) # rounds up to two decimal places

    #Creating fucntion for close window
    def close_window():
        fuelwindow.destroy()

    #Creating fucntion for help centre
    def helpcentre():
        helpwindow = Toplevel()
        helpwindow.title("Help Centre") #Naming window
        helpwindow.geometry("640x730") #Changing size of window
        helpwindow.configure (background = "orange") #Changing background colour

        logo = PhotoImage(file="Fuel.png") #Inserting company logo
        logoimage = Label(helpwindow, image=logo) #Help window is placed here so everything goes on the top layer
        logoimage.place(x = 1, y = 1, width=620, height=700) #Where logo is positioned

    #Creating fucntion for close window
        def close_window():
            helpwindow.destroy()

        button7 = Button(helpwindow, text = "Exit", command = close_window) #Naming button and calling on function of close window
        button7.place(x = 480, y = 665, width=140, height=45) #Creating size of button and positioning it
        button7.configure (background = "snow") #Changing background colour   




        helpwindow.mainloop()
           



    frame = Frame(window)
    frame.pack()

    titlelbl = Label(fuelwindow, text = "Fuel Economy(MPG)", font = 25) #Creating label
    titlelbl.place(x = 30, y = 20) #Placing title
    titlelbl.configure (background ="grey", font=("Courier",21 )) #Changing background colour

    distancelbl = Label(fuelwindow, text = "Distance (miles)", font =30)
    distancelbl.place(x = 20, y = 90, width=180, height=25) #Creating size of label and positioning it
    distancelbl.configure (background ="grey") #Changing background colour

    distancebox = Entry(fuelwindow, text = "")
    distancebox.place(x = 200, y = 90, width=120, height=25) #Creating size of button and positioning it
    distancebox.focus() #Creating the mouse to automatically be focused on this box


    fuelusedlbl = Label(fuelwindow, text = " Fuel used (gallons) ", font=30) #Creating fuel used label
    fuelusedlbl.place(x = 30, y = 120, width=180, height=25) #Creating size of labeland positioning it
    fuelusedlbl.configure (background ="grey")#Changing background colour

    fuelusedbox = Entry(fuelwindow, text = "")
    fuelusedbox.place(x = 200, y = 120, width=120, height=25) #Placing fuel used box

    #Calculate button
    calculatelst = Button(fuelwindow, text = "Calculate", command = lambda: calculate(),  fg= "black", bg = "white") #Creating text on button and calling function of calcualte
    calculatelst.place(x = 135, y = 175, width=100, height=25) #Creating size and position 

    #Total box
    display = StringVar()
    totalbox = Label(fuelwindow, text = (total), fg = "black", bg = "white", font =30)
    totalbox.place(x=90, y = 220, width = 200, height = 25) #Creating size of button and positioning it
    display.set("0") #Creating total box to display 0


    helpbutton=Button(fuelwindow, text = "Help", command = lambda: helpcentre(), font=40) #Creating text on button and calling function ofhelpcentre
    helpbutton.place(x= 30, y = 260, width = 50, height = 40) #Creating size of button and positioning it
    helpbutton.configure (background = "orange") #Changing background colour

    closebutton=Button(fuelwindow, text = "Close", command = lambda: close_window(), font=40) #Creating text on button and calling function of close window
    closebutton.place(x= 280, y = 260, width = 60, height = 40) #Creating size of button and positioning it
    closebutton.configure (background = "snow")#Changing background colour





    window.mainloop()
        
#############################################################################


#Main menu
    
window = Tk()
window.title("Calculator") #Naming window
window.geometry("350x550") #Changing size of window
window.configure (background = "cornsilk") #Changing background colour

#Creating title
mslbl = Label( text = "Please choose an option:", font = 50)
mslbl.place(x = 90, y = 15)
mslbl.configure (background = "cornsilk") #Changing background colour

#Creating fucntion for close window
def close_window():
    window.destroy()

#Creating fucntion for help centre
def helpcentre():
    helpwindow = Toplevel()
    helpwindow.title("Help Centre") #Naming window
    helpwindow.geometry("540x700") #Changing size of window
    helpwindow.configure (background = "orange") #Changing background colour

    logo = PhotoImage(file="Main.png") #Inserting company logo
    logoimage = Label(helpwindow, image=logo) #Helpwindow is placed here so everything goes on the top layer
    logoimage.place(x = 1, y = 1, width=540, height=700) #Where logo is positioned

#Creating fucntion for close window
    def close_window():
        helpwindow.destroy()

    button7 = Button(helpwindow, text = "Exit", command = close_window) #Naming button and calling on function of close window
    button7.place(x = 380, y = 650, width=140, height=45) #Creating size of button and positioning it
    button7.configure (background = "snow") #Changing background colour

    helpwindow.mainloop()
       

frame = Frame(window)
frame.pack()

#Inserting button on help screen
button1 = Button( text = "Standard Calculator", command = lambda: main()) #Naming button and calling on fucntion of standard calculator
button1.place(x = 100, y = 80, width=140, height=55) #Creating size of button and positioning it
button1.configure (background = "grey") #Changing background colour

button2 = Button( text = "Mortgage Calculator", command = lambda: mortgagecalculator ())  #Naming button and calling on fucntion of mortgage calculator
button2.place(x = 100, y = 155, width=140, height=55) #Creating size of button and positioning it
button2.configure (background = "grey") #Changing background colour

button3 = Button( text = "Vehicle Lease", command = lambda: vehiclelease ())  #Naming button and calling on function of vehicle lease
button3.place(x = 100, y = 230, width=140, height=55) #Creating size of button and positioning it
button3.configure (background = "grey") #Changing background colour

button4 = Button( text = "Fuel Economy (MPG)", command = lambda: fueleconomy()) #Naming button and calling on function of fuel economy
button4.place(x = 100, y = 305, width=140, height=55) #Creating size of button and positioning it
button4.configure (background = "grey") #Changing background colour

button5 = Button( text = "Help", command = lambda: helpcentre ()) #naming button and calling on function of help centre
button5.place(x = 20, y = 495, width=140, height=45) #creating size of button and positioning it
button5.configure (background = "orange") #Changing background colour

button6 = Button( text = "Exit", command = close_window) #naming button and calling on function of close window
button6.place(x = 190, y = 495, width=140, height=45)#creating size of button and positioning it
button6.configure (background = "snow") #Changing background colour

window.mainloop()

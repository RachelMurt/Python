from tkinter import *
import csv
import time
import math, operator, parser
from decimal import *

#Standard calculator window
def standardcalculator():
    calwindow = Tk()
    calwindow.title("Calculator") #Naming window
    calwindow.geometry("230x320") #Size of window
    calwindow.configure (background = "grey") #Changing background colour

    global bar #Creating a global total
    bar = 0 #Setting the total to 0
    
   
        
#Creating 'C' fucntion    
    def clear_all():
        bar.delete(0, END)

#Creating variable fucntion for the numbers
    def variables(num):
        global bar
        bar = total + num
        bar.get(total, num)
        

###Creating back function
##    def back():
##        numbers = bar.get()
##        if len(numbers):
##            new = numbers[:-1]
##            clear_all()
##            bar.insert(0, new)
##        else:
##            clear_all()
##            bar.insert(0, "Error, please press C") #creating error handling message 

#Creating MS function
    def MS():
        global stored
        stored = bar.get()

#Creating MC function
    def MC():
        global stored
        stored = clear_all()
        del stored

#Creating MR fucntion
    def MR():
        global stored
        bar.insert(total, stored)

#Creating add function
    def add():
        global total
        num = bar.get()
        total =(num) + "+"
        clear_all()

#Creating minus function
    def minus():
        global total
        num = bar.get()
        total = (num) + "-"
        clear_all()

#Creating multiply function
    def multiply():
        global total
        num = bar.get()
        clear_all()

#Creating divide '/' fucntion
    def divide():
        global total
        num = bar.get()
        total = (num) + "/"
        clear_all()

#Creating equals '=' function
    def equals():
        try:
            global total
            bar.insert(str(eval(total))
        except:
            bar.insert("error")
            total = 0

#Creating percentage '%' function
    def percentage():
        global total
        total = bar.get()
        if len(total):
            new = total[:-1]
            new = float(new)
            total = float(total)
            total = (new * total) / 100
            final = new + total
            final = float(final)
            clear_all()

#Creating sqaureroot function
    def squareroot():
        global total
        num = bar.get()
        num = float(num)
        num = math.sqrt(num)
        clear_all()
       

#Creating plus and minus '-' function
    def plusminus():
        global total
        bar.insert(0, "-")

#Creating decimal point '.' function
    def decimal():
        bar.insert(END, ".")

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

    #Creating display bar
    bar = Entry (calwindow, text = (total), justify = RIGHT, fg = "black", bg = "white") #Creating colours of box and justifying text to the right
    bar.place(x =10, y=10, width=215, height =30) #Positioning the bar
    
#########################
    
    #CREATING BUTTONS
    
#########################
    
         #LINE1
    
#########################
    #MC button
    button1 = Button(calwindow, text = "MC", command = lambda: MC(), font=10) #Creating text on box and calling MC function
    button1.place(x=10, y= 50, width =35,height = 35) #Creating size of button and positioning it
    button1.configure (background = "ghostwhite") #Changing background colour

    #MR button
    button2 = Button(calwindow, text = "MR", command = lambda: MR(), font=10) #Creating text on box and calling MR function
    button2.place(x=55, y= 50, width =35,height = 35) #Creating size of button and positioning it
    button2.configure (background = "ghostwhite") #Changing background colour

    #MS button
    button3 = Button(calwindow, text = "MS", command = lambda: MS(), font=10) #Creating text on box and calling MS function
    button3.place(x=100, y= 50, width =35,height = 35) #Creating size of button and positioning it
    button3.configure (background = "ghostwhite") #Changing background colour

    #CE button
    button4 = Button(calwindow, text = "CE", command = lambda: clear_all(), font=10) #Creating text on box and calling CE function
    button4.place(x=145, y= 50, width =35,height = 35) #Creating size of button and positioning it
    button4.configure (background = "ghostwhite") #Changing background colour

    #C button
    button5= Button(calwindow, text = "C", command = clear_all, font=10) #Creating text on box and calling MC function
    button5.place(x=190, y= 50, width =35,height = 35) #Creating size of button and positioning it
    button5.configure (background = "ghostwhite") #Changing background colour

#####################
    
      #LINE2
    
#####################
    
    #Number 6 button
    button6= Button(calwindow, text = "6", command = lambda: variables(6), font=15) #Creating text on box and calling variables function
    button6.place(x=10, y= 95, width =35,height = 35)#Creating size of button and positioning it
    button6.configure (background = "ghostwhite") #Changing background colour

    #Number 8 button
    button8= Button(calwindow, text = "8", command = lambda: variables(8), font=15) #Creating text on box and calling variables function
    button8.place(x=55, y= 95, width =35,height = 35) #Creating size of button and positioning it
    button8.configure (background = "ghostwhite") #Changing background colour

    #Number 9 button
    button9= Button(calwindow, text = "9", command = lambda: variables(9), font=15)  #Creating text on box and calling variables function
    button9.place(x=100, y= 95, width =35,height = 35) #Creating size of button and positioning it
    button9.configure (background = "ghostwhite") #Changing background colour

    #Plus and minus button
    button10= Button(calwindow, text = "+/-", command = lambda: plusminus(), font=15)  #Creating text on box and calling plusminus function
    button10.place(x=145, y= 95, width =35,height = 35) #Creating size of button and positioning it
    button10.configure (background = "ghostwhite") #Changing background colour

    #Sqaureroot button
    button11= Button(calwindow, text = "√", command = lambda: squareroot(), font=15) #Creating text on box and calling sqaureroot function
    button11.place(x=190, y= 95, width =35,height = 35) #Creating size of button and positioning it
    button11.configure (background = "ghostwhite") #Changing background colour
    

########################
    
        #LINE3
    
########################
    
    #Number 4 button
    button11= Button(calwindow, text = "4", command = lambda: variables(4), font=15)  #Creating text on box and calling variables function
    button11.place(x=10, y= 140, width =35,height = 35) #Creating size of button and positioning it
    button11.configure (background = "ghostwhite") #changing background colour

    #Number 5 button
    button12= Button(calwindow, text = "5", command = lambda: variables(5), font=15)  #Creating text on box and calling variables function
    button12.place(x=55, y= 140, width =35,height = 35) #Creating size of button and positioning it
    button12.configure (background = "ghostwhite") #Changing background colour

    #Number 6 button
    button13= Button(calwindow, text = "6", command = lambda: variables(6), font=15)  #Creating text on box and calling variables function
    button13.place(x=100, y= 140, width =35,height = 35) #Creating size of button and positioning it
    button13.configure (background = "ghostwhite") #Changing background colour

    #Back button             
    button14= Button(calwindow, text = "←", command = back, font=20)  #Creating text on box and calling back function
    button14.place(x=145, y= 140, width =35,height = 35) #Creating size of button and positioning it
    button14.configure (background = "ghostwhite") #Changing background colour

    #Percentage button
    button15= Button(calwindow, text = "%", command = lambda: percentage(), font=15)  #Creating text on box and calling percentage function
    button15.place(x=190, y= 140, width =35,height = 35) #Creating size of button and positioning it
    button15.configure (background = "ghostwhite") #Changing background colour
    
########################
    
        #LINE4
    
########################
    
    #Number 1 button
    button16= Button(calwindow, text = "1", command = lambda: variables(1), font=15)  #Creating text on box and calling variables function
    button16.place(x=10, y= 185, width =35,height = 35) #Creating size of button and positioning it
    button16.configure (background = "ghostwhite")#Changing background colour

    #Number 2 button
    button17= Button(calwindow, text = "2", command = lambda: variables(2), font=15) #Creating text on box and calling variables function
    button17.place(x=55, y= 185, width =35,height = 35) #Creating size of button and positioning it
    button17.configure (background = "ghostwhite") #Changing background colour
    
    #Number 3 button
    button18= Button(calwindow, text = "3", command = lambda: variables(3), font=15) #Creating text on box and calling variables function
    button18.place(x=100, y= 185, width =35,height = 35) #Creating size of button and positioning it
    button18.configure (background = "ghostwhite") #Changing background colour

    #Minus button
    button19= Button(calwindow, text = "-", command = lambda: minus(), font=15)  #Creating text on box and calling minus function
    button19.place(x=145, y= 185, width =35,height = 35) #Creating size of button and positioning it
    button19.configure (background = "ghostwhite") #Changing background colour

    #Divide button
    button20= Button(calwindow, text = "÷", command = lambda: divide(), font=15)  #Creating text on box and calling divide function
    button20.place(x=190, y= 185, width =35,height = 35) #Creating size of button and positioning it
    button20.configure (background = "ghostwhite") #Changing background colour

########################
    
        #LINE5
    
########################
    
    #Number 0 button
    button21= Button(calwindow, text = "0", command = lambda: variables(0), font=15) #Creating text on box and calling variables function
    button21.place(x=10, y= 230, width =35,height = 35) #Creating size of button and positioning it
    button21.configure (background = "ghostwhite") #Changing background colour

    #Decimal point button
    button22= Button(calwindow, text = ".", command = lambda: decimal(), font=15)  #Creating text on box and calling decimal function
    button22.place(x=55, y= 230, width =35,height = 35) #Creating size of button and positioning it
    button22.configure (background = "ghostwhite") #Changing background colour

    #Multiplication button
    button23= Button(calwindow, text = "x", command = lambda: multiply(), font=15)  #Creating text on box and calling multiply function
    button23.place(x=100, y= 230, width =35,height = 35) #Creating size of button and positioning it
    button23.configure (background = "ghostwhite") #Changing background colour

    #Add button
    button24= Button(calwindow, text = "+", command = lambda: add(), font=15) #Creating text on box and calling add function
    button24.place(x=145, y= 230, width =35,height = 35) #Creating size of button and positioning it
    button24.configure (background = "ghostwhite") #Changing background colour

    #Equals button
    button25= Button(calwindow, text = "=", command = lambda: equals(), font=15) #Creating text on box and calling equals function
    button25.place(x=190, y= 230, width =35,height = 35) #Creating size of button and positioning it
    button25.configure (background = "ghostwhite") #Changing background colour

#######################
    
#Help and close buttons
    
#######################
    
    #Help button
    button26= Button(calwindow, text = "Help", command = lambda: helpcentre(), font=15) #Creating text on box and calling helpcentre function
    button26.place(x=145, y= 280, width =80,height = 35) #Creating size of button and positioning it
    button26.configure (background = "orange") #Changing background colour

 #Creating fucntion for the window to close
    def close_window():
        calwindow.destroy()

    #Close window button
    button27= Button(calwindow, text = "Exit", command = close_window, font=15)  #Creating text on box and calling close window function
    button27.place(x=10, y= 280, width =80,height = 35)#Creating size of button and positioning it
    button27.configure (background = "snow")#Changing background colour


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
        totalbox["text"] = (total)

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
button1 = Button( text = "Standard Calculator", command = lambda: standardcalculator ()) #Naming button and calling on fucntion of standard calculator
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

#importing libraries to use
from tkinter import *
import csv
import time

total = 0

#adds customer details to list box
def add_to_list():
    name = namebox.get()
    namebox.delete(0,END)
    tableselection = table.get()
    table.set("Table Number")
    newdata = name + " , " + tableselection + " , " + "£{0:.2f}".format(total) + "\n"
    name_list.insert(END,newdata)
    namebox.focus()
    file = open("customer_list.csv","a")
    file.write(newdata)
    file.close()

#Tells the program what to do when certain buttons are clicked
def OnButtonClick(button_id):
    global total
    if button_id == 1:
        total = total + 4.50
        finalTotal = float(total)
        textbox4["text"] ="£{0:.2f}".format(finalTotal)
    elif button_id == 2:
        total = total + 3.50
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 3:
        total = total + 6
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 4:
        total = total + 6.50
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 5:
        total = total + 7
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 6:
        total = total + 5.50
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 7:
        total = total + 1.80
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 8:
        total = total + 0.5
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 9:
        total = total + 1
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 10:
        total = total + 1.80
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 11:
        total = total + 1.50
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 12:
        total = total + 1.90
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 13:
        total = total + 2
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 14:
        total = total + 1.80
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 15:
        total = total + 2.20
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 16:
        total = total + 2.20
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 17:
        total = total + 3
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 18:
        total = total + 2.50
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)
    elif button_id == 19:
        total = total + 2.50
        finalTotal = float(total)
        textbox4["text"] = "£{0:.2f}".format(finalTotal)

        
#Prints the list box to a csv file
def print_list():
    file=open("customer_list.csv","r")
    print(file.read())

#Resets the running total
def reset_total():
    global total
    total = total - total
    finalTotal = float(total)
    textbox4["text"] = "£{0:.2f}".format(finalTotal)
    
#Gives the price a 20% discount
def twenty_per():
    global total
    discount = total/100 *20
    total = total - discount
    textbox4["text"] = "£{0:.2f}".format(total)
    
    
#Gives the price a 30% discount
def thirty_per():
    global total
    discount = total/100 *30
    total = total - discount
    textbox4["text"] = "£{0:.2f}".format(total)
    
#Gives the price a 50% discount
def fifty_per():
    global total
    discount = total/100 *50
    total = total - discount
    textbox4["text"] = "£{0:.2f}".format(total)




    
#Help functions
#========================================================================================
  
#Creating the help window
def helpfun():
    #Help for the discount buttons
    
    def discounts():

        #Code for the button to close the window, rather than click on the 'X'
        #Destroys the current window process, closing it
        def disquit():
            top.destroy()
            
        #Top level creates a new window on top of the current one
        top = Toplevel()
        top.title("Discounts and Totals")
        top.geometry("830x450")
        top.configure(background = "SkyBlue1")
        top.wm_iconbitmap("icon.ico")

        
        #Must put "top" when you define a new button/label etc, or it will
        #Be placed in the wrong window
        
        logo = PhotoImage(file ="download.png")
        logoimage = Label(top, image = logo)
        logoimage.place(x = 350, y = 20)
        logoimage.configure(background = "black")
        
        titlelbl = Label(top, text = "How to use the EPOS" , font = 12)
        titlelbl.place(x = 50, y = 20, width = 210, height = 52)
        titlelbl.configure(background = "SkyBlue4", foreground = "white")

        part1lbl = Label(top, text = "Discounts and Totals", font = 12)
        part1lbl.place(x= 50, y = 75, width = 210, height = 52)
        part1lbl.configure(background = "SkyBlue4", foreground = "white")

        part1 = PhotoImage(file ="discounts.png")
        part1image = Label(top, image = part1)
        part1image.place(x = 55, y = 130)

        quitbtn = Button(top, text = "Close", font = 10, command = lambda: disquit())
        quitbtn.place(x = 700, y = 20, width = 120, height = 30)
        quitbtn.configure(background = "tomato2", foreground = "white")

        part1text = """            These buttons allow you to change the price
            when a customer has a coupon or voucher for the store!
            For example, 20% off will discount the current running total
            by 20%. The total will then update to the new, discounted price!
            When you click the "add to list" button, you will see the new
            total with the discounted price.
            The running total of the customer's current order updates
            when a button is pressed."""

        discountMeaning = Label(top, text = part1text, justify = LEFT, font = 10)
        discountMeaning.place(x = 300, y = 170, width = 480)
        discountMeaning.configure(background = "SkyBlue1")

        #Keeps the window running until the user closes it
        top.mainloop()


    #Names/Tables help function
    def namesfun():

        def namesquit():
            nameTop.destroy()
        #Makes a new window for the names and tables help
        nameTop = Toplevel()
        nameTop.title("Happy Coffee Shop Experience - Help")
        nameTop.geometry ("900x500")
        nameTop.configure(background = "SkyBlue1")
        nameTop.wm_iconbitmap("icon.ico")

        logo = PhotoImage(file ="download.png")
        logoimage = Label(nameTop, image = logo)
        logoimage.place(x = 430, y = 20)
        logoimage.configure(background = "black")

        titlelbl = Label(nameTop, text = "How to use the EPOS" , font = 12)
        titlelbl.place(x = 50, y = 20, width = 210, height = 52)
        titlelbl.configure(background = "SkyBlue4", foreground = "white")

        part1lbl = Label(nameTop, text = "Names, tables and files", font = 12)
        part1lbl.place(x= 50, y = 75, width = 210, height = 52)
        part1lbl.configure(background = "SkyBlue4", foreground = "white")

        part1 = PhotoImage(file ="nameboxes.png")
        part1image = Label(nameTop, image = part1)
        part1image.place(x = 50, y = 140)

        quitbtn = Button(nameTop, text = "Close", font = 10, command = lambda: namesquit())
        quitbtn.place(x = 700, y = 20, width = 120, height = 30)
        quitbtn.configure(background = "tomato2", foreground = "white")

        part1text = """        This part is used to insert customer's names,
        what table they are sitting at, and eventually, what their
        total price was. Type the customer's name into the box,
        select a table, and when you are done with their order, click
        on the "add to list" button. This will put their details into
        the white box. At the end of the day, click on the "Print List"
        button to print the details to the csv file named "customer_list.csv"
        This allows us to monitor the daily income!"""

        nameMeaning = Label(nameTop, text = part1text, justify = LEFT, font = 10)
        nameMeaning.place(x = 400, y = 200, width = 480)
        nameMeaning.configure(background = "SkyBlue1")

        nameTop.mainloop()

    def productsfun():

        def prodquit():
            prodTop.destroy()
            
        #Makes a new window for the products help
        prodTop = Toplevel()
        prodTop.title("Happy Coffee Shop Experience - Help")
        prodTop.geometry ("900x500")
        prodTop.configure(background = "SkyBlue1")
        prodTop.wm_iconbitmap("icon.ico")

        logo = PhotoImage(file ="download.png")
        logoimage = Label(prodTop, image = logo)
        logoimage.place(x = 400, y = 20)
        logoimage.configure(background = "black")
        
        titlelbl = Label(prodTop, text = "How to use the EPOS" , font = 12)
        titlelbl.place(x = 50, y = 20, width = 210, height = 52)
        titlelbl.configure(background = "SkyBlue4", foreground = "white")

        part1lbl = Label(prodTop, text = "Products", font = 12)
        part1lbl.place(x = 50, y = 75, width = 210, height = 52)
        part1lbl.configure(background = "SkyBlue4", foreground = "white")

        part1 = PhotoImage(file ="products.png")
        part1image = Label(prodTop, image = part1)
        part1image.place(x = 50, y = 140)

        quitbtn = Button(prodTop, text = "Close", font = 10, command = lambda: prodquit())
        quitbtn.place(x = 700, y = 20, width = 120, height = 30)
        quitbtn.configure(background = "tomato2", foreground = "white")

        part1text = """        These are all the buttons for our current
        products in the store. Every button has a price assigned to it,
        this price will be added to the running total, and then to
        the list box when you click the "add to list" button. These buttons
        are colour coded, red for food items, pink for children's
        items, green for drinks and purple for snacks. The yellow button,
        "Clear Price" sets the running total back to 0 in case you
        make a mistake. The total will update when you click on a button,
        this allows you to keep track of the current order's total price.."""

        nameMeaning = Label(prodTop, text = part1text, justify = LEFT, font = 10)
        nameMeaning.place(x = 350, y = 170, width = 480)
        nameMeaning.configure(background = "SkyBlue1")

        prodTop.mainloop()
    
    def helpquit():
            helpwindow.destroy()
            
    helpwindow = Toplevel()
    helpwindow.title("Happy Coffee Shop Experience - Help")
    helpwindow.geometry ("600x250")
    helpwindow.configure(background = "SkyBlue1")
    helpwindow.wm_iconbitmap("icon.ico")

    titlelbl = Label(helpwindow, text = "How to use the EPOS" , font = 12)
    titlelbl.place(x = 20, y = 20, width = 210, height = 52)
    titlelbl.configure(background = "SkyBlue4", foreground = "white")


    discount = Button(helpwindow, text = "Discounts and Totals", font = 12, command =lambda: discounts())
    discount.place(x= 250, y = 90, width = 300, height = 30)
    discount.configure(background = "SkyBlue4", foreground = "white")

    names = Button(helpwindow, text = "Names, tables and files", font = 12, command =lambda: namesfun())
    names.place(x= 250, y = 130, width = 300, height = 30)
    names.configure(background = "SkyBlue4", foreground = "white")

    products = Button(helpwindow, text = "Product Buttons", font = 12, command = lambda: productsfun())
    products.place(x= 250, y = 170, width = 300, height = 30)
    products.configure(background = "SkyBlue4", foreground = "white")

    quitbtn = Button(helpwindow, text = "Close", font = 10, command = lambda: helpquit())
    quitbtn.place(x = 430, y = 18, width = 120, height = 30)
    quitbtn.configure(background = "tomato2", foreground = "white")



    logo = PhotoImage(file ="download.png")
    logoimage = Label(helpwindow, image = logo)
    logoimage.place(x = 20, y = 120)
    logoimage.configure(background = "black")

    helpwindow.mainloop()





#Building the GUI
#========================================================================================
  
#Defining window
window = Tk()
window.title("Happy Coffee Shop Experience")
window.geometry("850x600")
window.configure(background = "SkyBlue1")
window.wm_iconbitmap("icon.ico")

#Date
datelbl = Label(text = "Date: " + time.strftime("%d/%m/%y"), font = 16)
datelbl.place(x = 30, y = 40)
datelbl.configure(background = "SkyBlue1")

#Placing logo
logo = PhotoImage(file = "download.png")
logoimage = Label(image = logo)
logoimage.configure(background = "black")
logoimage.place(x = 330, y = 50)

#Name Label
namelbl = Label(text = "Customer's Name: ")
namelbl.place(x = 30, y = 90, width=100, height=25)
namelbl.configure(background = "SkyBlue1")
namebox = Entry(text = "")
namebox.place(x = 130, y = 90, width=150, height=25)
namebox.focus()

#Selecting a table dropdown
tablelbl = Label(text = "Select a table: ")
tablelbl.place(x = 30, y = 140, width=100, height=25)
tablelbl.configure(background = "SkyBlue1")
table = StringVar(window)
table.set("Table Number")
tablemenu = OptionMenu(window, table, "Table 1","Table 2","Table 3","Table 4","Table 5","Table 6","Table 7","Table 8","Table 9","Table 10")
tablemenu.place(x = 130, y = 140)

#List box for names & tables
name_list=Listbox()
name_list.place(x = 130, y = 190,width=150, height=100)

#Add to list button
addbtn = Button(text = "Add to List", command = lambda: [add_to_list() ,reset_total() ])
addbtn.place(x = 30, y = 340, width=100, height=25)

#Save to csv file button
printlst = Button(text = "Save File", command = print_list)
printlst.place(x = 155, y = 340, width=100, height=25)

#Help button to open help windows
helpbtn = Button(text = "Click for help", command = lambda: helpfun())
helpbtn.place (x = 30, y = 370, width=100, height=25)






# Food Buttons - 10 per row
# Row 1 ==================================================================================

#Sandwich
button3 = Button (text = "Sandwich £4.50", command = lambda: OnButtonClick(1) )
button3.place(x = 570, y = 50, width = 120, height = 50)
button3.configure(background = "tomato2")

#Soup
button4 = Button(text = "Soup £3.50", command = lambda: OnButtonClick(2) )
button4.place(x = 570, y = 100, width = 120, height = 50)
button4.configure(background = "tomato2")

#S & S Combo
button5 = Button(text = "S & S Combo £6.00", command = lambda: OnButtonClick(3) )
button5.place(x = 570, y = 150, width = 120, height = 50)
button5.configure(background = "tomato2")

#Full Breakfast
button6 = Button(text = "Full Breakfast £6.50", command = lambda: OnButtonClick(4) )
button6.place(x = 570, y = 200, width = 120, height = 50)
button6.configure(background = "tomato2")

#Goats Tart Salad
button7 = Button(text = "Goats Tart Salad £7.00", command = lambda: OnButtonClick(5) )
button7.place(x = 570, y = 250, width = 120, height = 50)
button7.configure(background = "tomato2")

#Daily Special
button8 = Button(text = "Daily Special £5.50", command = lambda: OnButtonClick(6) )
button8.place(x = 570, y = 300, width = 120, height = 50)
button8.configure(background = "tomato2")

#Children's Meal
button9 = Button(text = "Children's Meal £1.80", command = lambda: OnButtonClick(7) )
button9.place(x = 570, y = 350, width = 120, height = 50)
button9.configure(background = "orchid1")

#Baby Chino
button10 = Button(text = "Baby Chino £0.50", command = lambda: OnButtonClick(8) )
button10.place(x = 570, y = 400, width = 120, height = 50)
button10.configure(background = "orchid1")

#Biscotti
button11 = Button(text = "Biscotti £1.00", command = lambda: OnButtonClick(9) )
button11.place(x = 570, y = 450, width = 120, height = 50)
button11.configure(background = "MediumPurple1")

#Clear Till
button12 = Button(text = "Clear Price", command = lambda: reset_total() )
button12.place(x = 570, y = 500, width = 120, height = 50)
button12.configure(background = "gold")





# Food Buttons - 10 per row
# Row 2 ==================================================================================

#Tea
button13 = Button(text = "Breakfast Tea £1.80", command = lambda: OnButtonClick(10) )
button13.place(x = 700, y = 50, width = 120, height = 50)
button13.configure(background = "PaleGreen1")

#Americano
button14 = Button(text = "Americano £1.50", command = lambda: OnButtonClick(11) )
button14.place(x = 700, y = 100, width = 120, height = 50)
button14.configure(background = "PaleGreen1")

#Latte
button15 = Button(text = "Latte £1.90", command = lambda: OnButtonClick(12) )
button15.place(x = 700, y = 150, width = 120, height = 50)
button15.configure(background = "PaleGreen1")

#Cappuccino
button16 = Button(text = "Cappuccino £2.00", command = lambda: OnButtonClick(13) )
button16.place(x = 700, y = 200, width = 120, height = 50)
button16.configure(background = "PaleGreen1")

#Espresso
button17 = Button(text = "Espresso £1.80", command = lambda: OnButtonClick(14) )
button17.place(x = 700, y = 250, width = 120, height = 50)
button17.configure(background = "PaleGreen1")

#Macchiato
button18 = Button(text = "Macchiato £2.20", command = lambda: OnButtonClick(15) )
button18.place(x = 700, y = 300, width = 120, height = 50)
button18.configure(background = "PaleGreen1")

#Hot Chocolate
button19 = Button(text = "Hot Chocolate £2.20", command = lambda: OnButtonClick(16) )
button19.place(x = 700, y = 350, width = 120, height = 50)
button19.configure(background = "PaleGreen1")

#Cake
button20 = Button(text = "Cake £3.00", command = lambda: OnButtonClick(17) )
button20.place(x = 700, y = 400, width = 120, height = 50)
button20.configure(background = "MediumPurple1")

#Tray Bake
button21 = Button(text = "Tray Bake £2.50", command = lambda: OnButtonClick(18) )
button21.place(x = 700, y = 450, width = 120, height = 50)
button21.configure(background = "MediumPurple1")

#Scone
button22 = Button(text = "Scone £2.50", command = lambda: OnButtonClick(19) )
button22.place(x = 700, y = 500, width = 120, height = 50)
button22.configure(background = "MediumPurple1")



#Discounts ==================================================================================

button23 = Button(text = "20% off", command = lambda: twenty_per() )
button23.place(x = 370, y = 190, width = 120, height = 50)
button23.configure(background = "orange")

button24 = Button(text = "30% off", command = lambda: thirty_per() )
button24.place(x = 370, y = 250, width = 120, height = 50)
button24.configure(background = "orange")

button25 = Button(text = "50% off", command = lambda: fifty_per() )
button25.place(x = 370, y = 310, width = 120, height = 50)
button25.configure(background = "orange")



#total box
display = StringVar()
textbox4 = Label(text = "£{0:.2f}".format(total), fg = "black", bg = "white", font=("Helvetica", 16))
textbox4.place(x = 370, y = 450,width = 120 ,height = 50)
display.set("0")

window.mainloop()

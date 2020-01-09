#Listing showing sample food items consumed within a day
#TIME, MTYPE, DESC, SERVING, KCAL, SFATg
08:11, Breakfast, Cereal, 200, 210, 1.6
08:20, Breakfast, Pancake, 38, 74, 1.4
08:20, Breakfast, Coffee, 200, 20, 0.4
10.30, Snack, Chocolate, 10, 56, 2.5
12:15, Lunch, Soup, 300, 170, 0.3
12:20, Lunch, Sandwich, 180, 365, 2.3
12:25, Lunch, Yogurt, 125, 65, 0.1
14:00, Snack, Apple, 100, 51, 0.1
17:30, Dinner, Fries, 70, 129, 0.6
17.30, Dinner, Chicken Breast, 155, 240, 3.5
17.30, Dinner, Broccoli, 85, 29, 0.1
18:00, Snack, Coffee, 200, 20, 0.4
20:00, Snack, Coffee, 200, 20, 0.4
20:00, Snack, Chocolate, 10, 56, 2.5
22:30, Snack, Cereal, 200, 210, 1.6

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
    newdata = name + " , "  + "{:,}".format(total) + "\n"
    name_list.insert(END,newdata)
    namebox.focus()
    file = open("Diet.csv","a")
    file.write(newdata)
    file.close()

#Tells the program what to do when certain buttons are clicked
def OnButtonClick(button_id):
    global total
    if button_id == 1:
        total = total + 4.50
        finalTotal = float(total)
        textbox4["text"] ="{:,}".format(finalTotal)
    elif button_id == 2:
        total = total + 3.50
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 3:
        total = total + 6
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 4:
        total = total + 6.50
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 5:
        total = total + 7
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 6:
        total = total + 5.50
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 7:
        total = total + 1.80
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 8:
        total = total + 0.5
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 9:
        total = total + 1
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 10:
        total = total + 1.80
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 11:
        total = total + 1.50
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)
    elif button_id == 12:
        total = total + 1.90
        finalTotal = float(total)
        textbox4["text"] = "{:,}".format(finalTotal)

        
#Prints the list box to a csv file
def print_list():
    file=open("Diet.csv","r")
    print(file.read())

#Resets the running total
def reset_total():
    global total
    total = total - total
    finalTotal = float(total)
    textbox4["text"] = "{:,}".format(finalTotal)
    textbox5["text"] = "{:,}".format(finalTotal)
    textbox6["text"] = "{:,}".format(finalTotal)
    
#Building the GUI
#========================================================================================
  
#Defining window
window = Tk()
window.title("Diet Gui")
window.geometry("850x600")
window.configure(background = "grey")
#Date
datelbl = Label(text = "Date: " + time.strftime("%d/%m/%y"), font = 16)
datelbl.place(x = 30, y = 40)
datelbl.configure(background = "grey")
#Name Label
namelbl = Label(text = "Name: ")
namelbl.place(x = 30, y = 90, width=100, height=25)
namelbl.configure(background = "grey")
namebox = Entry(text = "")
namebox.place(x = 130, y = 90, width=150, height=25)
namebox.focus()
#List box for names & tables
name_list=Listbox()
name_list.place(x = 130, y = 190,width=150, height=100)
#Add to list button
addbtn = Button(text = "Add to List", command = lambda: [add_to_list() ,reset_total() ])
addbtn.place(x = 30, y = 340, width=100, height=25)
#Save to csv file button
printlst = Button(text = "Save File", command = print_list)
printlst.place(x = 155, y = 340, width=100, height=25)

# Food Buttons - 10 per row
# Row 1 ==================================================================================

#Sandwich
button3 = Button (text = "Cereal", command = lambda: OnButtonClick(1) )
button3.place(x = 570, y = 50, width = 120, height = 50)
button3.configure(background = "grey")

#Soup
button4 = Button(text = "Pancake", command = lambda: OnButtonClick(2) )
button4.place(x = 570, y = 100, width = 120, height = 50)
button4.configure(background = "grey")

#S & S Combo
button5 = Button(text = "Chocolate", command = lambda: OnButtonClick(3) )
button5.place(x = 570, y = 150, width = 120, height = 50)
button5.configure(background = "grey")

#Full Breakfast
button6 = Button(text = "Soup", command = lambda: OnButtonClick(4) )
button6.place(x = 570, y = 200, width = 120, height = 50)
button6.configure(background = "grey")

#Goats Tart Salad
button7 = Button(text = "Sandwich", command = lambda: OnButtonClick(5) )
button7.place(x = 570, y = 250, width = 120, height = 50)
button7.configure(background = "grey")

#Daily Special
button8 = Button(text = "Yogurt", command = lambda: OnButtonClick(6) )
button8.place(x = 570, y = 300, width = 120, height = 50)
button8.configure(background = "grey")

#Children's Meal
button9 = Button(text = "Apple", command = lambda: OnButtonClick(7) )
button9.place(x = 570, y = 350, width = 120, height = 50)
button9.configure(background = "grey")

#Baby Chino
button10 = Button(text = "Fries", command = lambda: OnButtonClick(8) )
button10.place(x = 570, y = 400, width = 120, height = 50)
button10.configure(background = "grey")

#Biscotti
button11 = Button(text = "Chicken Breast", command = lambda: OnButtonClick(9) )
button11.place(x = 570, y = 450, width = 120, height = 50)
button11.configure(background = "GREY")

#Clear Till
button12 = Button(text = "Clear", command = lambda: reset_total(),  )
button12.place(x = 570, y = 500, width = 120, height = 50)
button12.configure(background = "orange")

# Food Buttons - 10 per row
# Row 2 ==================================================================================

#Tea
button13 = Button(text = "Coffee", command = lambda: OnButtonClick(10) )
button13.place(x = 700, y = 50, width = 120, height = 50)
button13.configure(background = "grey")

#Americano
button14 = Button(text = "Broccoli", command = lambda: OnButtonClick(11) )
button14.place(x = 700, y = 100, width = 120, height = 50)
button14.configure(background = "grey")

#Latte
button15 = Button(text = "Hot Chocolate", command = lambda: OnButtonClick(12) )
button15.place(x = 700, y = 150, width = 120, height = 50)
button15.configure(background = "grey")


#total box1
display1 = StringVar()
textbox4 = Label(text = "{:,}".format(total), fg = "snow", bg = "black", font=("Helvetica", 16))
textbox4.place(x = 370, y = 450,width = 120 ,height = 50)
display1.set("0")
#total box2
display2 = StringVar()
textbox6 = Label(text = "{:,}".format(total2), fg = "snow", bg = "black", font=("Helvetica", 16))
textbox6.place(x = 370, y = 450,width = 120 ,height = 50)
display2.set("0")
#total box3
display3 = StringVar()
textbox5 = Label(text = "{:,}".format(total3), fg = "snow", bg = "black", font=("Helvetica", 16))
textbox5.place(x = 370, y = 450,width = 120 ,height = 50)
display3.set("0")

window.mainloop()


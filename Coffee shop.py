## Coffee Shop Program. Order your favourite coffees. Just make sure you pay for them!


import csv

## function to let user order coffee
def coffeeOrder():
    
    ## open the menu
    file = open("menulist.txt", "r")
    ## use the csv reader to open the file and remove the commas
    csv1 = csv.reader(file, delimiter = ',')

    ## display coffee menu sorted by coffee/tea name
    col = sorted(csv1)
    for i in range( 0, len( col ) ):
        print( "Coffees & Teas:",col[i][0], "\tSize:",col[i][1], "\tPrice:",col[i][2] )

    ## select how many items you wish to order
    orderQty = int(input("How many drinks are you ordering?: "))
    drinksOrder = []    ## list to store coffee order
    size = []        ## list to store size

    ## loop through and enter coffee order
    for i in range(orderQty):
        drinks = input("What drink would you like?: ")
        drinksOrder.append(drinks)
        drinkSize = input("What size would you like, Regular or Large?: ")
        size.append(drinkSize)
                 
    ## loop and display user order
    for k in range(len(drinksOrder)):
        print( "Coffee & Teas:",drinksOrder[k], "\tProduct:",col[k][1],"\tSize:",(size[k]), "\tCost", col[k][2])
        k+=1
        ## Calculate the total order cost
        TotalOrderCost = sum(float(col[k][2]) for k in range(len(drinksOrder)))

    print ("Total order cost is: ", TotalOrderCost , "\n")

    payment = float(input("Enter Payment amount: "))

    if(payment > TotalOrderCost):
        change = payment - TotalOrderCost
        print("Your change is:", round(change,2), "enjoy your coffee")
    else:
        print('===============================================')
        print("£",payment," is not enough  you need £",TotalOrderCost)
        print('===============================================')
        return

## main function
def main():
        option =  ' '
        while option != 'Q':
              ## welcome message
                print("Python Coffee Shop")
                print("------------------")
                option = input ("""
                1 - Key 1 to order some drinks
                Q - Exit
                """)
                if option =='1':
                    coffeeOrder()    
                elif option =='Q' or 'q':
                    print('Goodbye. Thank you for visiting our coffee shop')
                    print('===============================================')
                    break
                else:
                    print ('Invalid Selection - please try again')
main()
  

             




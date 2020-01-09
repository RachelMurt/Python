import time
import random

print("Welcome to this choose your own adventure!")
print("==============================================")
time.sleep(1)

def dungeon():
    print("You walk down the dimly lit hallway, torch in hand.")
    print("Water drips from the roof as you check your surroundings,")
    print("the darkness seems to creep from every corner. You come to")
    print("an intersection, paths leading to your [left], [right] and [straight]")
    direc1 = input("What direction do you continue in?: ")
    if direc1 == 'left':
        print(" ")
        print("You go left, and the floor suddenly disappears beneath you,")
        print("Sending you falling to your death!")
        time.sleep(2)
        print(" ")
        dungeon()
    elif direc1 == 'right':
        print(" ")
        print("You enter a room, it has a treasure chest in the middle of it.")
        print("There are numbers written on the walls, you guess it gives you the code for the chest.")
        print("Around the room, written on the walls multiple times is the code 11307.")
        print("But the chest only has room for two numbers.")
        ans = input("Do you [add] or [multiply] the numbers? ")
        if ans == 'multiply':
            code1 = 1 * 1 * 3 * 7
            print("You enter" , code1 , "and the chest opens.... and slams down on your hand instantly")
            print("You're stuck there forever!")
            print(" ")
            time.sleep(2)
            dungeon()
        elif ans == 'add':
            code2 = 1 + 1 + 3 + 7
            print("You enter" ,code2, "and you hear it unlock!")
        else:
            print("That wasn't an answer! The walls start slowly closing in, crushing the treasure chest and you!")
            time.sleep(2)
            print(" ")
            dungeon()
        rewardList = ['gold coins!', 'a magical sword!', 'spell scrolls!', 'a dog!', 'an animal picture book!', 'psychedelic pastries!', 'a broom!']
        print("You open it carefully,")
        print("inside you find", random.choice(rewardList))
        
    elif direc1 == 'straight':
        print(" ")
        print("You continue into the dungeon, wandering endlessly.")
        print("You eventually find the exit and escape with no loot!")
        print("What a dissappointing dungeon.") 
    else:
        print("That's not an option!")
        print("A monster catches up to you, and you perish in the dungeon.")
        time.sleep(2)
        print(" ")
        dungeon()



dungeon()
    

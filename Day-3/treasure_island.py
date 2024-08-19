# Treasure Island Game
print("\n")
print("Welcome to Treasure Island")
print("Your mission is to find the Treasure")
print("\n")
choice1 = input("You're at a crossroad, where do you want to go? type \"left\" or \"right\" -- ")
choice1 = choice1.lower()
if choice1 == "right":
    print("You made the correct decision")
    choice2 = input("You're at a lake, would you like to \"swim\" or \"wait\" -- ")
    choice2 = choice2.lower()
    if choice2 == "wait":
        print("You made the correct decision")
        print("A boat arrives to take you accross the lake")
        choice3 = input("You have 3 doors to choose from, \"red\" or \"blue\" or \"green\" -- ")
        choice3 = choice3.lower()
        if choice3 == "green":
            print("You win! Treasure is yours to take.\n")
        elif choice3 == "red":
            print("You were burned by raging fire,'GAME OVER'\n ")
        elif choice3 == "blue":
            print("You were eaten by Zombies,'GAME OVER'\n ")
        else:
            print("Wrong Input\n")

    elif choice2 == "swim":
        print("Sorry, you were eaten by Crocodile! 'GAME OVER'\n ")
    else:
        print("Wrong Input\n")
        
elif choice1 == "left":
    print("Sorry, you made the wrong decision! 'GAME OVER'\n ")
else:
    print("Wrong Input\n")

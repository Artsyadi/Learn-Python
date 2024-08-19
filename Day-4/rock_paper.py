# Rock-Paper-Scissor Game
import random
import module
print("What do you choose?")
print("Type 0 for Rock, 1 for Paper, 2 for Scissor")
choice = int(input("What is your input - "))
print(module.game[choice])
computer_choice = random.randint(0,2)
if choice>=3 or choice<0:
    print("You chose a invalid number!")
elif choice==computer_choice:
    print("Computer Chose :")
    print(module.game[computer_choice])
    print("It's a draw!")
elif (choice==0 and computer_choice==1) or (choice==1 and computer_choice==2) or (choice==2 and computer_choice==0):
    print("Computer Chose :")
    print(module.game[computer_choice])
    print("You Lose!")
elif (choice==0 and computer_choice==2) or (choice==1 and computer_choice==0) or (choice==2 and computer_choice==1):
    print("Computer Chose :")
    print(module.game[computer_choice])
    print("You Win!")
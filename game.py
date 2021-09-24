import random

userWins=0
compWins=0
userChoice=["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors please input from the selection located below")
while True:
    userInput = input("Type Rock or Paper or Scissors or q to quit\n").lower().strip()

    rand = random.randint(0,2)
    compInput = userChoice[rand]
    print("the comp chose ",compInput)

    if userInput == "q":
        break

    elif userInput not in userChoice:
        print("pick a selectiom from the choice selection from above")
        continue

    elif userInput=="rock" and compInput=="scissors":
        print("you win")
        userWins+=1

    elif userInput=="paper" and compInput=="rock":
        print("you win")
        userWins+=1

    elif userInput=="scissors" and compInput=="paper":
        print("you win")
        userWins+=1

    elif userInput==compInput:
        print("draw")

    else:
        print("comp wins")
        compWins+=1
    

    print("your score: ", userWins," and the computer score: " , compWins)

print("you have chosen to quit the game")

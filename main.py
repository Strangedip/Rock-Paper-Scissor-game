# Rock-Paper-Scissor-game
# first python game

#create a rock paper scissor game using basics if else nad compare

import random

comp = random.randint(1,3)

if comp ==1:
    comp= "rock"
elif comp==2:
    comp="paper"
else:
    comp="scissor"
    
player = input("Type your choice :\nrock, paper, scissor : ")

print (f"comp Chose {comp}")

if comp == "rock" :
    if player == "paper":
        print("You won!")
    elif player=="scissor":
        print("you lose !")
    else :
        print("the game is a Tie !")

elif comp == "paper" :
    if player == "rock":
        print("you lose !")
    elif player=="scissor":
        print("You won!")
    else :
        print("the game is a Tie !")

elif comp == "scissor": 
    if player == "rock":
        print("You won!")
    elif player=="paper":
       print("you lose !")
    else :
        print("the game is a Tie !")
        

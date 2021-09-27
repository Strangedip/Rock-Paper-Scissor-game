#create rock paper scissor game using functions

import random               

def gamewin(comp, player):
    if comp == player:
        return None
    elif comp == "r":
        if player=="p":
            return True
        else :
            return False
    elif comp == "p":
        if player=="s":
            return True
        else :
            return False
    elif comp == "s":
        if player=="r":
            return True
        else :
            return False
        

comp = random.randint(1,3)

if comp ==1:
    comp="r"
elif comp ==2:
    comp="p"
else:
    comp="s"


player= input("Enter Your Choice\nRock(r), Paper(p), scissor(s) : ")

print(f"The Computer Chose {comp}")


a=gamewin(comp,player)

if a==None:
    print("Its a Tie !")
elif a:
    print("You Won !")
else :
    print("You lose !")


    

print("Welcome to the Coins and Dies Game!")
print("First Step - Flip a Coin. If head, you can choose 6-side die. If tail, you can choose 4-side die")

import random

def flip_coin():
    return random.choice(["Head","Tail"])
coin=flip_coin()
print("The coin landed on"+" "+coin)

if coin == "Head":
    die_choice="6-side die"
else:
    die_choice="4-side die"
print("You will use"+" "+ die_choice)

roll=[]
if die_choice=="6-side die":
    def roll6die():
        return random.randint(1,6)
    die6=roll6die()
    roll.append(die6)
    print("The die landed on"+" "+str(die6))
    if die6<=3:
        print("You can roll 3 more times")
    else:
        print("You can roll 2 more times")
elif die_choice=="4-side die":
    def roll4die():
        return random.randint(1,4)
    die4=roll4die()
    roll.append(die4)
    print("The die landed on"+" "+str(die4))
    if die4<=3:
        print("You can roll 3 more times")
    else:
        print("You can roll 2 more times")


if die_choice=="6-side die":
    rolls=int(input("How many time can you roll? Enter 2 or 3 "))
    while rolls:
        x=random.randint(1,6)
        rolls -= 1
        roll.append(x)
elif die_choice=="4-side die":
    rolls=int(input("How many time can you roll? Enter 2 or 3 "))
    while rolls:
        y=random.randint(1,4)
        rolls -= 1
        roll.append(y) 
print("Your last round rolls are:"+" "+str(roll[1:]))

totalsum=sum(roll)
print("Your total score is"+" "+ str(totalsum))

if totalsum >= 10:
    print("You win the game!")
else:
    print("Sorry, you lost.")

#I think more information should be given at the start of the game about the games objectives and how you win.
#I know that the coin will either be heads or tails but I think it would be cool if the user got to input something that actually flipped the coin rather than just saying what it landed on
#I don't understand why we are given an option of 2 or 3 roles, why would you choose 2?
#The code all works well, but I think you could add more strategy for the user
















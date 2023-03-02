print("Welcome to the Coins and Dies Game!")

while True:
    print("Are you ready for the game? Answer Yes or No")
    qs=input()
    if qs.lower() == "yes":
        break
    else:
        print("This is not the answer, try again")

print("First Step - Flip a Coin. If HEAD, you will use a 6-side die. If TAIL, you will use a 4-side die")

while True:
    print("Are you ready to flip a coin? Answer Y or N")
    qs=input()
    if qs.lower() == "y":
        break
    else:
        print("This is not the answer,try again")

import random

def flip_coin():
    return random.choice(["Head","Tail"])
coin=flip_coin()
print("The coin landed on"+" "+coin)

while True:
    print("Are you ready to check which die you will use? Answer Y or N")
    qs=input()
    if qs.lower() == "y":
        break
    else:
        print("This is not the answer,try again")

if coin == "Head":
    die_choice="6-side die"
else:
    die_choice="4-side die"
print("You will use a "+" "+ die_choice)

if die_choice=="6-side die":
    print("6-side die will have 6 sides, you will have chance to lands on [1,2,3,4,5,6]")
elif die_choice=="4-side die":
    print("4-side die will have 6 sides, you will have chance to lands on [1,2,3,4]")

while True:
    print("Are you ready to roll the first round using selected die? Answer Y or N")
    qs=input()
    if qs.lower() == "y":
        break
    else:
        print("This is not the answer,try again")

roll=[]
if die_choice=="6-side die":
    def roll6die():
        return random.randint(1,6)
    die6=roll6die()
    roll.append(die6)
    print("The die landed on"+" "+str(die6))
    print("If the die lands on [1,2,or 3], you can roll 3 more times. If the die lands on [4,5,or 6], you can roll 2 more times")
    if die6<=3:
        r=3
        print("Now You can roll 3 more times")
    else:
        r=2
        print("Now You can roll 2 more times")
elif die_choice=="4-side die":
    def roll4die():
        return random.randint(1,4)
    die4=roll4die()
    roll.append(die4)
    print("The die landed on"+" "+str(die4))
    print("If the die lands on [1,2,or 3], you can roll 3 more times. If the die lands on [4], you can roll 2 more times")
    if die4<=3:
        r=3
        print("Now You can roll 3 more times")
    else:
        r=2
        print("Now You can roll 2 more times")

while True:
    print("Are you ready to check your last round rolls? Answer Y or N")
    qs=input()
    if qs.lower() == "y":
        break
    else:
        print("This is not the answer,try again")

if die_choice=="6-side die":
    while True:
        rolls=int(input("How many time can you roll? Enter 2 or 3 "))
        if rolls==r:
            break
        else:
            print("Enter your true number of rolls")
    while rolls:
        x=random.randint(1,6)
        rolls -= 1
        roll.append(x)
elif die_choice=="4-side die":
    while True:
        rolls=int(input("How many time can you roll? Enter 2 or 3 "))
        if rolls==r:
            break
        else:
            print("Please enter your true number of the rolls")
    while rolls:
        y=random.randint(1,4)
        rolls -= 1
        roll.append(y) 
print("Your last round rolls are:"+" "+str(roll[1:]))

while True:
    print("One last step! Check your total score. Answer Y or N")
    qs=input()
    if qs.lower() == "y":
        break
    else:
        print("This is not the answer,try again")

totalsum=sum(roll)
print("Your total score is"+" "+ str(totalsum))
print("If your total score is higher than or equal to 10, you wins! If lower than 10, you lost, please try again!")

if totalsum >= 10:
    print("You win the game!")
else:
    print("Sorry, you lost.")



















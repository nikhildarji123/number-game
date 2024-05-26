import random

u = 0
c = 0
options = ["rock", "paper","scissors","test"]
while True:
    n = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if n == "q":
        break

    if n not in ["rock","paper","scissors"]:
        continue

    number = random.randint(0,2)
    # rock : 0, paper: 1, scissors: 2
    computer_pick = options[number]
    print("Computer picked ", computer_pick + ".")

    if n == "rock" and computer_pick == "scissors":
        print("You win!")
        u += 1
        continue
    elif n == "paper" and computer_pick == "rock":
        print("You win!")
        u += 1
        continue
    elif n == "scissors" and computer_pick == "paper":
        print("You win!")
        u += 1
        continue
    else:
        print("you lost!")
        c += 1
print("you won ", u ," times.")
print("you lost ", c," times.")
print("Goodbye!")

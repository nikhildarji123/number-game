import random

n = input("Type a number: ")
if n.isdigit():
    n = int(n)

    if n <= 0:
        print('Please type a number larger than 0 next time')
        quit()
else:
    print('Please type a number next time')
    quit()

number = random.randint(0,n)
guesses = 0

while True:
    guesses += 1
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please type a number next time')
        continue
    if guess == number:
        print("You guessed it!")
        break
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
print("You got it in ",guesses," guesses")
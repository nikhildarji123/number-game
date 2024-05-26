print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()
print("okay! let's play : )")

answer = input("what does cpu stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for ? ").lower()
if answer == "graphic processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for ? ").lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for ? ").lower()
if answer == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score)  +  " question correct !" )
print("You got " + str((score/4) * 100)  +  "%." )
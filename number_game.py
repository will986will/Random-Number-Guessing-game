import random
print("*************************")
print("  Guess the number game")
print("*************************\n")

print ("Would you like 1.easy/2.medium/3.hard")
difficulty = int(input("1/2/3"))
if difficulty == 1:
    print("Guess the generated number between 1 and 10.\n")
    number=random.randint(1,10)
    guess=int(input("What is your first guess?"))
    attempts = 1
    while guess!= number:
      if guess >  number:
        print("Too high")
        previousguess = guess
        guess = int(input("Guess again...:"))
        attempts = attempts + 1
      else:
        print("Too low")
        previousguess = guess
        guess = int(input("Guess again...:"))
        attempts = attempts + 1
    print("Correct, you took", attempts, "attmepts to guess")

if difficulty == 2:
    print("Guess the generated number between 1 and 100.\n")
    number=random.randint(1,100)
    guess=int(input("What is your first guess?"))
    attempts = 1
    while guess!= number:
      if guess >  number:
        print("Too high")
        previousguess = guess
        guess = int(input("Guess again...:"))
        attempts = attempts + 1
      else:
        print("Too low")
        previousguess = guess
        guess = int(input("Guess again...:"))
        attempts = attempts + 1
    print("Correct, you took", attempts, "attmepts to guess")

if difficulty == 3:
    print("Guess the generated number between 1 and 500.\n")
    number=random.randint(1,500)
    guess=int(input("What is your first guess?"))
    attempts = 1
    while guess!= number:
      if guess >  number:
        print("Too high")
        previousguess = guess
        guess = int(input("Guess again...:"))
        attempts = attempts + 1
      else:
        print("Too low")
        previousguess = guess
        guess = int(input("Guess again...:"))
        attempts = attempts + 1
    print("Correct, you took", attempts, "attmepts to guess")


# Generate a random number between 1–10.

# Ask user to guess until they get it right.

# Give hints: “Too high / Too low”.


import random
secret = random.randint(1,10)
attempts = 0


while True :
 guess = int(input("Guess the number(1-10): "))
 attempts+=1

 if guess < secret:
  print("too low!, try again")

 elif guess > secret:
  print("too high!, try again")

 else:
  print("Correct! The number was ", secret)
  print("You guessed it in", attempts, "attempts")
  break



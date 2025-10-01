# Number Guessing game with exception handling

import random

secret = random.randint(1,10)

try:
    number = int(input("Guess a number 1-10: "))
    if number < 1 or number > 10:
        raise ValueError("Error! Number should be in between 1 and 10")
    
    if number == secret:
        print("You guessed the number right!")
        
    else:
        print("Wrong the number was",secret)

except ValueError as e:
    print(e)

finally:
    print("Game Over!")
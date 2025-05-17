# Used to generate a random number between 1 and 40

import random
 
print("Guessing game")


answer = random.randint(1, 40)

guess_count = 0

while guess_count < 10:
    guess = int(input("Enter your guess: "))
    if guess != answer:
        if guess < answer:
            print("Guess is low")
        elif guess > answer:
            print("Guess is high")
        print("Try again")
        guess_count += 1
    else:
        print("You got the answer!")
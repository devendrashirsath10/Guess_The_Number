# Guess_The_Number

A Python-based Guess the Number game that uses the random library to generate a secret number. Players receive hints for each guess until they find the correct number, showcasing Python basics such as loops, conditions, user input, and random number generation.

import random

n = random.randint(1,50)

a = -1

Guesses=1

while (a!=n):
    a=int(input("Guess The Number :"))
    if (a>n):
        print("Lower Number Please")
        Guesses+=1
    elif(a<n):
        print("Higher Number Please")
        Guesses+=1

print(f"You have Guessed the Number {n} ,Correctly in {Guesses} Attempt")













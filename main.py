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

import random
print("numberguessinggame")
number = random.randint(1,9)
chances = 0

print("guess a number(between1and9): ")

while chances<5:
    guess = int(input("enter you guess: "))
    if guess ==number:
        print("you won")
        break
    elif guess<number:
        print("guess a higher number than",guess)
    else:
        print("guess a lower number than",guess)

    chances += 1

if not chances<5:
    print("you lose,the number is",number)


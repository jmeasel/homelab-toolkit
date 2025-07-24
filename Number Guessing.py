import random

print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess == secret_number:
        print("You got it! The number was", secret_number)
        break
    elif guess < secret_number:
        print("Too low. Try again!")
    else:
        print("Too high. Try again!")

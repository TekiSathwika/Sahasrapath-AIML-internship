#3. Number Guessing Game
#Task: Create a guessing game where the program stores a secret number.

number = int(input("Enter secret number: "))
guess = 0 
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("You Won ")
    elif guess > number:
        print("Too High")
    else:
        print("Too Low")

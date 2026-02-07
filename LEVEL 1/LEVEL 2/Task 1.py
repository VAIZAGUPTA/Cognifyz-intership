import random

secret_number = random.randint(1, 100)
attempts = 0
previous_difference = None

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    difference = abs(secret_number - guess)

    if guess == secret_number:
        print("Correct! You guessed the number 🎉")
        print("Total attempts:", attempts)
        break

    if guess > secret_number:
        print("Too high")
    else:
        print("Too low")

    if previous_difference is not None:
        if difference < previous_difference:
            print("Hint: You are getting warmer 🔥")
        else:
            print("Hint: You are getting colder ❄️")

    previous_difference = difference

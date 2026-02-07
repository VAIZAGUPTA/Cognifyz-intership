import random

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

secret_number = random.randint(start, end)
attempts = 0

print("Guess the number between", start, "and", end)

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("Correct! You guessed the number 🎉")
        print("Total attempts:", attempts)
        break

    elif guess > secret_number:
        print("Too high ⬆️ — try a smaller number")

    else:
        print("Too low ⬇️ — try a bigger number")

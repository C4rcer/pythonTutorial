secret_number = 9
guess_count = 0  # tracks attempts
guess_limit = 3  # limit for attempts

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1  # increment guess_count by 1 each iteration
    if guess == secret_number:  # if the user guesses the secret_number print message and break out of loop
        print("You won!")
        break
else:
    print("You failed")

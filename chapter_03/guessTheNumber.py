import random

guessed_number = random.randint(1,20)

condition = True
user_guess_counter = 0
print("I am thinking of a number between 1 to 20.")
while condition:
    # print("Take a guess.")
    try:
        user_answer = int(input("Take a guess.\n"))
    except Exception as e:
        print("Please enter an integer between 1 to 20.")
    user_guess_counter += 1
    # print(user_answer)
    if user_answer == guessed_number:
        print(f"Good job! You guessed my number in {user_guess_counter} guesses!")
        condition = False
    elif user_answer < guessed_number:
        print("Your guess is too low!")
    elif user_answer > guessed_number:
        print("Your guess is too high!")

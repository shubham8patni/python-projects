import random

def user_guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low!")
        elif guess > random_number:
            print("Sorry, guess again. Too high!")
    
    print(f"Bingo! You guessed the correct number: {guess}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    counter = 0
    while feedback != 'c':
        counter += 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # It can also be high since low = high

        print(f"Computer's guess: {guess}")
        feedback = input(f"Is my guess {guess}, too high (H), too low (L) or correct (c): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    print(f"Yay! The computer guessed the correct number {guess} in {counter} turns.")

#user_guess(10)
computer_guess(20)
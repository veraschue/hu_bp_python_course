from random import randint


def guess_a_number():
    """Game to guess a number the computer randomly generated."""

    random_number = randint(0, 100)
 
    guess = int(raw_input("Please enter an integer between 0 and 100: "))
    count_guesses = 1
    while guess != random_number:
        count_guesses = count_guesses + 1
        guess = evaluate_my_number(guess, random_number)
    else:
        print('Hooray! Your guess is right!\nYou needed {} guesses.'.format(count_guesses))
        new_game = unicode(raw_input("Do you want to play again? If so, say 'yes'! "))
        if new_game == 'yes':
            guess_a_number()
        else:
            print('Goodbye!')


def evaluate_my_number(guess, random_number):
    """Is the guess to high or to low? Guess again!"""

    if guess < random_number:
        guess = int(raw_input("Too low! Please try again: "))
        return guess
    else:
        guess = int(raw_input("Too high! Please try again: "))
        return guess

guess_a_number()
from random import randint


def guess_a_number():
    """Game to guess a number the computer randomly generated."""

    random_number = randint(0, 100)
 
    guess = check_raw("Please enter an integer between 0 and 100: ")
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
        print 'Too low!',
        guess = check_raw()
        return guess
    else:
        print 'Too high!',
        guess = check_raw()
        return guess


def check_raw(print_string='Please try again: '):
    """hkjg"""

    try:
        checked_int = int(raw_input(print_string))
        if checked_int < 0 or checked_int > 100:
            print 'Your number has to be between 0 and 100!',
            checked_int = check_raw()
    except ValueError:
        print 'That was not an integer!',
        checked_int = check_raw()

    return checked_int

guess_a_number()
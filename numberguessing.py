import random
number = random.randint(1,100)
#while True:
    try:
        guessnum = int(input('Guess a number between 1 and 100: '))
    except ValueError:
        print('Please enter a valid input')
    if guessnum < number:
        print('Too low!')
    elif guessnum > number:
        print('Too high')
    elif guessnum == number:
        print('You got it!')
        break

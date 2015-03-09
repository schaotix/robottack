from random import choice
import pics # robot faces

pics.face()
print('Welcome to RoboShamBo.')
user = input('What is your name?: ')
print('Prepare to lose, {}'.format(user))

rps = ['rock', 'paper', 'scissors']

uChoice = input('Rock, Paper, Scissors? ')
uChoice = uChoice.lower()
bChoice = choice(rps)

if (uChoice == bChoice):
    print('You chose {}, I chose {}, therefore we tie!'.format(uChoice, bChoice))

elif (uChoice == 'rock'):
    if (bChoice == 'paper'):
        print('You chose {}, I chose {}. I win!'.format(uChoice, bChoice))
    else:
        print('You chose {}, I chose {}. You win!'.format(uChoice, bChoice))

elif (uChoice == 'paper'):
    if (bChoice == 'scissors'):
        print('You chose {}, I chose {}. I win!'.format(uChoice, bChoice))
    else:
        print('You chose {}, I chose {}. You win!'.format(uChoice, bChoice))

elif (uChoice == 'scissors'):
    if (bChoice == 'rock'):
        print('You chose {}, I chose {}. I win!'.format(uChoice, bChoice))
    else:
        print('You chose {}, I chose {}. You win!'.format(uChoice, bChoice))


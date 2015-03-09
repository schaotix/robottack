from random import choice
import pics # robot faces

pics.face()
print('Welcome to RoboShamBo.')
user = input('What is your name?: ')
print('Prepare to lose, {}'.format(user))

rps = ['r', 'p', 's']

uChoice = input('(R)ock, (P)aper, (S)cissors? ')
uChoice = uChoice.lower()
bChoice = choice(rps)

if uChoice == bChoice:
    print('You chose {}, I chose {}, therefore we tie!'.format(uChoice, bChoice))
    pics.face()


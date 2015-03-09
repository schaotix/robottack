from random import choice
import pics


class Robot:
    power = 3
    def hit(self):
        pics.attack1()
        print('\x1b[31m')
        print("GAH!")
        print('\x1b[0m')
        self.power -= 1


class Player:
    power = 3
    def hit(self):
        print('\x1b[31m')
        print("I'm hit!")
        print('\x1b[0m')
        self.power -= 1


robo = Robot()  # declaring objects for robot
user = Player()  # and user


def strike():

    if uChoice == bChoice:
        print('You chose {}, I chose {}, therefore we tie!'.format(uChoice, bChoice))
    elif uChoice == 'rock':
        if bChoice == 'paper':
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            user.hit()
        else:
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            robo.hit()
    elif uChoice == 'paper':
        if bChoice == 'scissors':
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            user.hit()
        else:
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            robo.hit()
    elif uChoice == 'scissors':
        if bChoice == 'rock':
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            user.hit()
        else:
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            robo.hit()

    if robo.power == 3:
        pics.face()
    elif robo.power == 2:
        pics.attack1()
    elif robo.power == 1:
        pics.attack2()
    elif robo.power <= 0:
        pics.attack3()
    else:
        print("What'd you do?!")



pics.face()  # print the first face
print('Welcome to RoboShamBo.')
u = input('What is your name?: ')
print('Prepare to lose, {}'.format(u))
uChoice = input('Rock, Paper, Scissors? ')
rps = ['rock', 'paper', 'scissors']  # declaring a list to hold the three choices
uChoice = uChoice.lower()
bChoice = choice(rps)
strike()








from random import choice


class Robot:
    power = 3

    def hit(self):
        self.power -= 1

        if self.power == 2:
            face1()
            strike()
        elif self.power == 1:
            face2()
            strike()
        elif self.power <= 0:
            face3()
        else:
            print('What did you do?!')



class Player:
    power = 3

    def hit(self):
        print('\x1b[31m')
        print("You're hit! -1")
        self.power -= 1
        print('Player power = {}'.format(self.power))
        if self.power <= 0:
            print("You're dead. :-(")
            print('\x1b[0m')
        else:
            strike()


robot = Robot()  # declaring objects for robot
user = Player()  # and user


def face():
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')

def face1():
    # yellow
    print('\x1b[33m')
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')
    print('\x1b[0m')

def face2():
    # red
    print('\x1b[31m')
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')
    print('\x1b[0m')

def face3():
    # red background - kaboom!
    print('\x1b[41m')
    print('KABOOM!!!')
    print('\x1b[0m')


def strike():

    rps = ['rock', 'paper', 'scissors']  # declaring a list to hold the three choices
    uChoice = input('Rock, Paper, Scissors? ')
    uChoice = uChoice.lower()
    bChoice = choice(rps)

    if uChoice == bChoice:
        print('You chose {}, I chose {}, therefore we tie!'.format(uChoice, bChoice))
        strike()
    elif uChoice == 'rock':
        if bChoice == 'paper':
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            user.hit()
        else:
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            robot.hit()
    elif uChoice == 'paper':
        if bChoice == 'scissors':
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            user.hit()
        else:
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            robot.hit()
    elif uChoice == 'scissors':
        if bChoice == 'rock':
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            user.hit()
        else:
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            robot.hit()

def main():
    face()  # print the first face
    print('Welcome to RoboShamBo.')
    u = input('What is your name?: ')
    print('Prepare to lose, {}'.format(u))
    strike()


main()







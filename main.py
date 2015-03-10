from random import choice
import time

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
        print('\x1b[0m')
        if self.power <= 0:
            print('\x1b[31m')
            print("You're dead. :-(")
            print('\x1b[0m')
        else:
            strike()


robot = Robot()  # declaring objects for robot
user = Player()  # and user


def face():
    print('\t_________')
    print('\t| (.Y.) |')
    print('\t|   o   |')
    print('\t| /|||\\ |')
    print('\t|_______|')

def face1():
    # yellow
    print('\x1b[33m')
    print('\t_________')
    print('\t| (.Y.) |')
    print('\t|   o   |')
    print('\t| /|||\\ |')
    print('\t|_______|')
    print('\x1b[0m')

def face2():
    # red
    print('\x1b[31m')
    print('\t_________')
    print('\t| (.Y.) |')
    print('\t|   o   |')
    print('\t| /|||\\ |')
    print('\t|_______|')
    print('\x1b[0m')

def face3():
    # red background - kaboom!
    print('\x1b[41m')
    print('\tKABOOM!!!')
    print('\x1b[0m')
    print('\n\tYou Win! Congratulations!')


def strike():

    rps = ['rock', 'paper', 'scissors']  # declaring a list to hold the three choices
    uChoice = input('Rock, Paper, Scissors? ')
    uChoice = uChoice.lower()
    bChoice = choice(rps)

    if uChoice == bChoice:
        time.sleep(1)
        print('You chose {}, I chose {}, therefore we tie!'.format(uChoice, bChoice))
        time.sleep(1)
        strike()
    elif uChoice == 'rock':
        if bChoice == 'paper':
            time.sleep(1)
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            time.sleep(1)
            user.hit()
        else:
            time.sleep(1)
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            time.sleep(1)
            robot.hit()
    elif uChoice == 'paper':
        if bChoice == 'scissors':
            time.sleep(1)
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            time.sleep(1)
            user.hit()
        else:
            time.sleep(1)
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            time.sleep(1)
            robot.hit()
    elif uChoice == 'scissors':
        if bChoice == 'rock':
            time.sleep(1)
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            time.sleep(1)
            user.hit()
        else:
            time.sleep(1)
            print('You chose {}, I chose {}.'.format(uChoice, bChoice))
            time.sleep(1)
            robot.hit()

def main():
    face()  # print the first face
    print('Welcome to RoboShamBo.')
    time.sleep(1)
    u = input('What is your name?: ')
    print('Prepare to lose, {}'.format(u))
    strike()


main()







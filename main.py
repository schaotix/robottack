from random import choice
import pics


class Robot:
    power = 3
    def hit(self):
        pics.attack1()
        print('Gah! You won!')
        self.power -= 1


class Player:
    power = 3
    def hit(self):
        self.power -= 1


robo = Robot()  # declaring objects for robot
user = Player()  # and user


def strike():

    if uChoice == bChoice:
        pics.face()  # it's a tie, so plain face
        print('You chose {}, I chose {}, therefore we tie!'.format(uChoice, bChoice))

    elif uChoice == 'rock':
        if bChoice == 'paper':
            print('You chose {}, I chose {}. I win!'.format(uChoice, bChoice))
            user.power -= 1
        else:
            print('You chose {}, I chose {}. You win!'.format(uChoice, bChoice))
            robo.power -= 1

    elif uChoice == 'paper':
        if bChoice == 'scissors':
            print('You chose {}, I chose {}. I win!'.format(uChoice, bChoice))
            user.power -= 1
        else:
            print('You chose {}, I chose {}. You win!'.format(uChoice, bChoice))
            robo.power -= 1

    elif uChoice == 'scissors':
        if bChoice == 'rock':
            print('You chose {}, I chose {}. I win!'.format(uChoice, bChoice))
            user.power -= 1
        else:
            print('You chose {}, I chose {}. You win!'.format(uChoice, bChoice))
            robo.power -= 1

    if robo.power == 3:
        pics.face()
    elif robo.power == 2:
        pics.attack1()
    elif robo.power == 1:
        pics.attack2()
    elif robo.power <= 0:
        pics.attack3()
    else:
        print('What''d you do?!')


pics.face()  # print the first face
print('Welcome to RoboShamBo.')
u = input('What is your name?: ')
print('Prepare to lose, {}'.format(u))


rps = ['rock', 'paper', 'scissors']  # declaring a list to hold the three choices


uChoice = input('Rock, Paper, Scissors? ')
uChoice = uChoice.lower()
bChoice = choice(rps)

strike()





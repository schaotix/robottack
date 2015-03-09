import time

class Target:
    power = 4
    def attack(self):
        print('Gah!')
        self.power -= 1

    def checkPower(self):
        if self.power <= 0:
            print('\x1b[45m')
            print('D E S T R O Y E D')
            print('\x1b[m')
        else:
            print('Power at {}'.format(self.power))


def main():

    robo1 = Target()
    num = int(input('Fire how many shots? '))
    while num != 0:
        print('\x1b[31m')
        print('Firing!')
        time.sleep(1)
        print('\x1b[m')
        robo1.attack()
        num -= 1
        robo1.checkPower()

main()



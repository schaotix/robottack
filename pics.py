def face():
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')

def attack1():
    # cyan 
    print('\x1b[36m')
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')
    print('\x1b[0m')

def attack2():
    # yellow
    print('\x1b[33m')
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')
    print('\x1b[0m')
    robo1.power -= 1

def attack3():
    # red
    print('\x1b[31m')
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')
    print('\x1b[0m')
    robo1.power -= 1

def attack4():
    # red background - kaboom!
    print('\x1b[41m')
    print('KABOOM!!!')
    print('\x1b[0m')
    
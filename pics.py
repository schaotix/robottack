def face():
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')

def attack1():
    # yellow
    print('\x1b[33m')
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')
    print('\x1b[0m')
    robo1.power -= 1

def attack2():
    # red
    print('\x1b[31m')
    print('_________')
    print('| (.Y.) |')
    print('|   o   |')
    print('| /|||\\ |')
    print('|_______|')
    print('\x1b[0m')
    robo1.power -= 1

def attack3():
    # red background - kaboom!
    print('\x1b[41m')
    print('KABOOM!!!')
    print('\x1b[0m')
    

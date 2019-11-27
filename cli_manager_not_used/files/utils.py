import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_menu():
    clear_screen()
    print('###################################################')
    print('             Cars Collection Manager               ')
    print('###################################################')
    print()
    print('Options:')
    print('1 - Seed Brands')
    print('2 - Seed Fuel Type')
    print('3 - Seed Cars Examples')
    print('0 - Exit')
    print()


def exit_menu():
    clear_screen()
    print()
    print('You logout.')
    print()

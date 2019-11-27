import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_collection.settings")
django.setup()
from cli_manager.files.fake_data import faker_brand, faker_car, faker_fuel_type
from cli_manager.files.utils import exit_menu, create_menu


def main():
    create_menu()
    option = input('Select the option: ')
    while option != '0':
        create_menu()
        options(option)
        option = input('Select the option: ')
    exit_menu()


def options(option):
    if option == '1':
        faker_brand()
    elif option == '2':
        faker_fuel_type()
    elif option == '3':
        faker_car()
    else:
        print('Invalid option!')


if __name__ == '__main__':
    main()

from games.brolibs import welcome_message, exit_program
from games import bropy
from tools import kalkulator
from tools import mini_market

def menu():
    while True:
        print('\nMenu Program:\n1. Bropy Game\n2. Kalkulator\n3. Mini Market\n4. Exit\n')
        user_options = int(input('Silahkan pilih menu: '))

        if user_options == 1:
            bropy.start()
        elif user_options == 2:
            kalkulator.start()
        elif user_options == 3:
            mini_market.start()
        elif user_options == 4:
            exit_program()
        else:
            print('\nMohon pilih menu program yang sesuai!!')

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()
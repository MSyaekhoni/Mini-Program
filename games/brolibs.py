import socket
from time import sleep

PC_NAME = socket.gethostname()

def welcome_message():
    style = "*" * (len(PC_NAME) + 6)
    print(f"\n{style}")
    print(f"** {PC_NAME} **")
    print(f"{style}\n")

def exit_program():
    print("\nProgram akan dihentikan...")
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('\nProgram berhasil berhenti.')
    exit()

if __name__ == '__main__':
    welcome_message()
    exit_program()
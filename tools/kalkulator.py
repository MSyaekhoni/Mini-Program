import main

def start():
    while True:
        x = int(input('\nMasukkan angka pertama: '))
        y = int(input('Masukkan angka kedua: '))

        print(f'\nHasil Penjumlahan = {tambah(x, y)}\n')
        
        berhitung_lagi = input('Ingin berhitung lagi? [y/n]: ')
        
        if berhitung_lagi == 'n':
            main.menu()

def tambah(x, y):
    return x + y

if __name__ == '__main__':
    start()
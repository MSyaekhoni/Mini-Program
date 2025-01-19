import main

def start():
    while True:
        print('\nDaftar Operasi:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n')
        pilih_operasi = int(input('Silahkan pilih operasi: '))

        if pilih_operasi == 1:
            x = int(input('\nMasukkan angka pertama: '))
            y = int(input('Masukkan angka kedua: '))
            print(f'\nHasil Penjumlahan = {tambah(x, y)}\n')
            berhitung_lagi = input('Ingin berhitung lagi? [y/n]: ')
        elif pilih_operasi == 2:
            x = int(input('\nMasukkan angka pertama: '))
            y = int(input('Masukkan angka kedua: '))
            print(f'\nHasil Pengurangan = {kurang(x, y)}\n')
            berhitung_lagi = input('Ingin berhitung lagi? [y/n]: ')
        elif pilih_operasi == 3:
            x = int(input('\nMasukkan angka pertama: '))
            y = int(input('Masukkan angka kedua: '))
            print(f'\nHasil Perkalian = {kali(x, y)}\n')
            berhitung_lagi = input('Ingin berhitung lagi? [y/n]: ')
        elif pilih_operasi == 4:
            x = int(input('\nMasukkan angka pertama: '))
            y = int(input('Masukkan angka kedua: '))
            print(f'\nHasil Pembagian = {bagi(x, y)}\n')
            berhitung_lagi = input('Ingin berhitung lagi? [y/n]: ')
        else:
            print('\nSilahkan pilih menu operasi yang sesuai!')

        if berhitung_lagi == 'n':
            main.menu()

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

if __name__ == '__main__':
    start()
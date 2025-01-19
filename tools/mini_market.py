import main
from database import db_minimarket

print('SELAMAT DATANG DI MINI MARKET\n')

def start():
    while True:
        menu = int(input('Dartar Menu:\n1. Tambah Barang\n2. Check Barang\n3. Kembali\n\nSilahkan pilih menu: '))

        if menu == 1:
            add()
        elif menu ==2:
            check()
        elif menu == 3:
            main.menu()
        else:
            print('Pilih menu yang sesuai!!\n')

def add():
    kode_barang = input('kode barang: ')
    nama_barang = input('nama barang: ')
    harga_barang = int(input('harga barang: '))
    stok_barang = int(input('stok barang: '))

    db_minimarket.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)

def check():
    pass
if __name__ == '__main__':
    start()
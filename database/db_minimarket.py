import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_mini_market'
)

def insert_item(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang, stok_barang))
    db.commit()
    if cursor.rowcount > 0:
        print('\nData berhasil disimpan!\n')
    else:
        print('\nData gagal tersimpan!\n')

def fetch_item():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_barang')
    return cursor.fetchall()
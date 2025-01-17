import random
import main

def start():
    while True:
        goa = "[_]"
        deret_goa = [goa] * 4 #Goa Kosong
        goa_bro = deret_goa.copy() #Goa untuk Bropy
        bro_position = random.randint(1,4) #memberikan nilai posisi Bropy secara acak
        goa_bro[bro_position - 1] = "|0_0|"
        deret_goa = ' '.join(deret_goa)
        goa_bro = ' '.join(goa_bro)

        print(f"\nCoba perhatikan Goa dibawah ini!\n\n{deret_goa}\n")

        pilihan_user = int(input("Menurut kamu di Goa nomor berapa Bropy berada? [1][2][3][4]: "))
        while pilihan_user <= 0 or pilihan_user >= 5:
            pilihan_user = int(input("Tolong pilih nomor Goa yang sesuai! [1][2][3][4]: "))

        if bro_position == pilihan_user:
            print(f"\n{goa_bro}\n")
            print(f"SELAMAT KAMU MENANG! 🏆\nBropy berada di Goa nomor {bro_position} dan pilihan kamu adalah Goa nomor {pilihan_user}.")
        else:
            print(f"\n{goa_bro}\n")
            print(f"YAAH KAMU KALAH ☹️\nBropy tidak ada di Goa nomor {pilihan_user}. Bropy berada di Goa nomor {bro_position}.")

        main_lagi = input("\n\nIngin bermain lagi? [y/n]: ")
        if main_lagi == "n":
            main.menu()

if __name__ == '__main__':
    start()
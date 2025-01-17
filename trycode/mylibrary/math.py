def grade(nilai):
    if nilai >= 90:
        print(f"nilai {nilai} mendapatkan grade A")
    elif nilai >= 80 and nilai <= 89:
        print(f"nilai {nilai} mendapatkan grade B")
    elif nilai >= 60 and nilai <= 79:
        print(f"nilai {nilai} mendapatkan grade C")
    else:
        print(f"nilai {nilai} mendapatkan grade D")

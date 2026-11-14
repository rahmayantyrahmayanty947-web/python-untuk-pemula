for angka in range(1, 30):
    if angka % 2 != 0:
        continue
    if angka > 22:
        break
    print("Angka genap:", angka)
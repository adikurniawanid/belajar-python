angka = int(input("Masukan angka Kurang dari 3 atau Lebih dari 10 : "))

# +++++++3-----------10++++++++
if (angka < 3 or angka > 10):
    print("benar, kecil dari 3 atau besar dari 10")
else:
    print("salah, tidak kecil dari 3 atau besar dari 10")

# ------3+++++++10-------
if (angka > 3 and angka < 10):
    print("benar, antara 3 dan 10")
else:
    print("salah, tidak antara 3 dan 10")

# ------0+++++5------8+++++11------
print("pr1")
if((angka > 0 and angka < 5) or (angka > 8 and angka < 11)):
    print("Benar")
else:
    print("salah")
# ++++++0-----5++++++8-----11++++++
print("pr2")
if(angka < 0 or (angka > 5 and angka < 8) or angka > 11):
    print("Benar")
else:
    print("salah")

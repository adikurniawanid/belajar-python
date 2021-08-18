# uppercase
salam = "bRo!"
print(salam)
print(salam.upper())
print(salam.lower())

print(salam.islower())
print(salam.isupper())
print(salam.isalpha())  # alpabet
print(salam.isalnum())  # alpanumeric
print(salam.isspace())  # spasi doang
print(salam.isspace())  # semua kata dimulai dengan hurug besar

judul = "It Is Okay To Be Orang Kaya"
print("judul title gak?", judul.istitle())

print(judul.startswith("It"))
print(judul.startswith("it"))
print(judul.endswith("Orang Kaya"))
print(judul.endswith("orang kaya"))

list = ["aku", "sayang", "kamu"]
print(list)
print(" ".join(list))

list = "aku sayang kamu"
print(list.split(" "))

# alokasi karakter rjust(), ljust(), center

print("kanan".rjust(20))
print("kiri".ljust(20))
print("tengah".center(20))
print("tengah".center(20, "-"))
print("tengah".center(20, ":"))

# strip()
tengah = "walah-gitu-ya".center(20, "-")
print(tengah)
print(tengah.strip("-"))

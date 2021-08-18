nama = "marlene"
formatString = f"hello {nama}"
print(formatString)

# boolean
boolean = True
formatString = f"benergak? {boolean}"
print(formatString)

# angka
angka = 2005.5
formatString = f"angka = {angka}"
print(formatString)

# bilangan bulat
angka = 15
formatString = f"bilangan bulat = {angka:d}"
print(formatString)

# bilangan dengan ordo ribuan
angka = 20000000000000
formatString = f"bilangan bulat = {angka:,}"
print(formatString)

# bilangan desimal ambil dua angka belakang koma
angka = 20000000000000.52321
formatString = f"bilangan bulat = {angka:.2f}"
print(formatString)

# menampilkan leading zero
angka = 2000.52321
formatString = f"bilangan bulat = {angka:10.2f}"
print(formatString)

# menampilkan leading zero
angka = 2000.52321
formatString = f"bilangan bulat = {angka:010.2f}"
print(formatString)

# tanda plus minus
minus = -10
plus = 10
minus = f"minus = {minus}"
plus = f"minus = {plus}"
print(plus)
print(minus)

# memformat persen
persentase = 0.045
formatPersen = f"pesen {persentase:.2%}"
print(formatPersen)

# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5

formatString = f"harga total = Rp. {harga*jumlah:,}"
print(formatString)

# format angka lain(binary, oktal, hexadecimal)
angka = 255
formatBinary = f"binary {bin(angka)}"
formatOktal = f"oktal {oct(angka)}"
FormatHexa = f"hex {hex(angka)}"

print(formatBinary)
print(formatOktal)
print(FormatHexa)

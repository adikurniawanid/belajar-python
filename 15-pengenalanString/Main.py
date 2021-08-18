namaPertama = "ucup"
namaTengah = "otong"
namaAkhir = "surotong"

namaLengkap = namaPertama + " " + namaTengah + " " + namaAkhir
print(namaLengkap)

panjang = len(namaLengkap)
print(panjang)

# mengecek apakah ada char atau sting dalam string
d = "U"
print(d in namaLengkap)
d = "u"
print(d in namaLengkap)
d = "ucup"
print(d in namaLengkap)

print(d not in namaLengkap)

# mengulangsting
print("wk"*10)
print(10*"wk")

# indexing
print("index ke-0 : " + namaLengkap[0])
print("index ke-(-1) : " + namaLengkap[-1])  # ngambil dari belakang
# ngambil dalam range, namun yang terakhir gak dapet
print("index ke-0 s/d ke-3 : " + namaLengkap[0:3])
# ngambil pake jeda
print("index ke-0 s/d ke-10 : " + namaLengkap[0:10:2])

# item paling kecil
print("paling kecil :" + min(namaPertama))
print("paling besar :" + max(namaPertama))

# cek ascii
asciiCode = ord("c")
print(asciiCode)
asciiCode = ord("u")
print(asciiCode)

# operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print(jumlah)

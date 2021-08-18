# width and multiline

nama = "Ucup Surucup"
umur = 17
tinggi = 150.1
nomorSepatu = 44
# string multiline


String = f"nama = {nama},\numur = {umur},\ntinggi = {tinggi},\nnomor sepatu = {nomorSepatu}"
print("\n" + 5*"="+"Biodata" + 5*"=")
print(String)

# dengan triplets
String = f"""
nama         : {nama}
umur         : {umur:>5}
tinggi       : {tinggi:>10}
nomor sepatu : {nomorSepatu:>5}
"""
print(String)

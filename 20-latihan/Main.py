# Date and time
import datetime as dt

hariIni = dt.date.today()
print(hariIni)
print(f"""
Hari ini adlaah hari = {hariIni:%A}
"""
      )

tanggal = dt.date(2000, 1, 21)
print(tanggal)

print("Silahkan masukan tanggal, bulan, dan tahun lahir anda:")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))
tanggalLahir = dt.date(tahun, bulan, tanggal)
umurDalamHari = hariIni - tanggalLahir
umurDalamTahun = umurDalamHari // 365
umurDalamBulan = umurDalamHari // 30

print(f"""
tanggal Lahir \t:{tanggalLahir}
Hari Lahir \t:{tanggalLahir:%A}
Umur \t\t:{umurDalamHari.days} Hari
\t\t {umurDalamBulan.days} Bulan
\t\t {umurDalamTahun.days} Tahun
""")

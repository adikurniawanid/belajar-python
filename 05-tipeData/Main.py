from ctypes import c_double

angkaInteger = 1
print("data", angkaInteger)
print("-bertipe : ", type(angkaInteger))

angkaFloat = 21.01
print("data", angkaFloat)
print("-bertipe : ", type(angkaFloat))

dataString = "Adi Kurniawan"
print("data", dataString)
print("-bertipe : ", type(dataString))

dataBoolean = True
print("data", dataBoolean)
print("-bertipe : ", type(dataBoolean))

dataComplex = complex(5, 6)
print("data", dataComplex)
print("-bertipe : ", type(dataComplex))

# tipe data dari bahasa C
dataDoubleC = c_double(10.5)
print("-bertipe : ", type(dataDoubleC))

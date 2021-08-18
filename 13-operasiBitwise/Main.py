# operasi pada masing masing bit
# 1 : 00000001
# 2 : 00000010

a = 9
b = 5

# bitwise OR (|)
c = a | b
print("=============OR=============")
print('nilai : ', a, ", binary", format(a, '08b'))
print('nilai : ', b, ", binary", format(b, '08b'))
print("---------------------------(|)")
print('nilai : ', c, ", binary", format(c, '08b'))

# bitwise AND (&)
c = a & b
print("=============AND=============")
print('nilai : ', a, ", binary", format(a, '08b'))
print('nilai : ', b, ", binary", format(b, '08b'))
print("---------------------------(&)")
print('nilai : ', c, ", binary", format(c, '08b'))

# bitwise XOR (^) #salah satu true, sisanya false maka true
c = a ^ b
print("=============XOR=============")
print('nilai : ', a, ", binary", format(a, '08b'))
print('nilai : ', b, ", binary", format(b, '08b'))
print("---------------------------(^)")
print('nilai : ', c, ", binary", format(c, '08b'))

# bitwise NOT (~)
c = ~a
print("=============NOT=============")
print('nilai : ', a, ", binary", format(a, '08b'))
print("---------------------------(~)")
print('nilai : ', c, ", binary", format(c, '08b'))

# Flip data
d = 0b00001001
print('nilai : ', d, ", binary", format(d, '08b'))
print("---------------------------(^)")
e = 0b11111111
print('nilai : ', e ^ d, ", binary", format(e ^ d, '08b'))

# shifting
# shiftright (>>)
c = a >> 2
print("=============SHIFT=============")
print('nilai : ', a, ", binary", format(a, '08b'))
print("---------------------------(>>)")
print('nilai : ', c, ", binary", format(c, '08b'))

# shiftleft (<<)
c = a << 2
print("=============SHIFT=============")
print('nilai : ', a, ", binary", format(a, '08b'))
print("---------------------------(>>)")
print('nilai : ', c, ", binary", format(c, '08b'))

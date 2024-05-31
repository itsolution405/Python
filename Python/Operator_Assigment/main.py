# operator yang dapat di lakukan dengan penyingkatan
# operasi di tambah dengan assigment

a = 5 # adalah assigment
print("nilai a =", a)

a = a + 1 # artinya a = a + 1
print("nilai a =", a)

a += 1 # artinya a = a + 1
print("nilai a += 1, nilai a menjadi",a)

a -= 2 # artinya a = a - 2
print("nilai a -= 2, nilai a menjadi",a)

a *= 2 # artinya a = a * 5
print("nilai a *= 5, nilai a menjadi",a)

a /= 2 # artinya a = a / 2
print("nilai a /= 2, nilai a menjadi",a)

b = 10
print("\nnilai b =",b)

# modulus dan floar devision
b %= 3
print("nilai a %= 3, nilai b menjadi",b)

b = 10
print("\nnilai b =",b)

b //= 2
print("nilai a //= 2, nilai b menjadi",b)

#pangkat atau exponen
a = 5
print("nilai a =",a)
a **= 3
print("nilai a **= 2, nilai a menjadi",a)

# operasi bitwise
c = True
print("\nnilai c =",c)
c |= False
print("nilai c =",c)
c = False
print("nilai c |= False, nilai c menjadi",c)
c |= False
print("nilai c =",c)

# AND
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= False, nilai c menjadi",c)
c = True
print("nilai c =",c)
c &= True
print("nilai c &= True, nilai c menjadi",c)

# XOR
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c &= False, nilai c menjadi",c)
c = True
print("nilai c =",c)
c ^= True
print("nilai c ^= True, nilai c menjadi",c)

# geser geser
d= 0b0100
print("\nnilai d=",format(d, '04b'))
d >>= 2
print("\nnilai d >>= 2, nilai c menjadi",format(d, '04b'))
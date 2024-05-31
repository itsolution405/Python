# a = 10, a adlah variable dengan nilai 10

# tipe data: Angka satuan yang gak ada koma nya (integer)
data_integer = 11
print(type(data_integer))
print("data : ", data_integer, ", bertipe :", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print(type(data_float))
print("-bertipe : ", type(data_float))

# tipe data: kumpulan karakter (float)
data_string = "none"
print("data : ", data_string)
print("-bertipe : ", type(data_string))

# tipe data: biner true / false (boolean)
data_bool = True
print("data : ", data_bool)
print("-bertipe : ", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex (5,6)
print("data : ", complex)
print("-bertipe : ", type(complex))

# tipe data bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("-bertipe : ", type(data_c_double))
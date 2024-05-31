# Casting
# merubah dari satu tipe ke tipe lain
# tipe data = int, float, str, bool

print ("=====INTEGER=====")
data_int = 9
print("data = ", data_int, ",  type =", type(data_int))

data_float = float (data_int)
data_str = float (data_int)
data_bool = float (data_int) # akan false jika nilai int = 0
print("data = ", data_float, ",  type =", type(data_float))
print("data = ", data_str, ",  type =", type(data_str))
print("data = ", data_bool, ",  type =", type(data_bool))

# Float
print ("=====FLOAT=====")
data_bool = True;
print("data = ", data_bool, ",  type =", type(data_bool))

data_bool = float (data_bool) # akan dibulatkan ke bawah
data_str = float (data_bool)
data_float = float (data_bool) # akan false jika nilai float = 0
print("data = ", data_int, ",  type =", type(data_int))
print("data = ", data_str, ",  type =", type(data_str))
print("data = ", data_float, ",  type =", type(data_float))

# String
print ("=====STRING=====")
data_bool = "10";
print("data = ", data_str, ",  type =", type(data_str))

data_int = int (data_bool) # akan dibulatkan ke bawah
data_float = float (data_bool)
data_bool = bool (data_bool) # akan false jika nilai float = 0
print("data = ", data_int, ",  type =", type(data_int))
print("data = ", data_float, ",  type =", type(data_float))
print("data = ", data_bool, ",  type =", type(data_bool))
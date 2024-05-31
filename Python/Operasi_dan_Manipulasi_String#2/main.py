# operator dalam bentuk methods

# merubah case dari string

# merubah semua ke uppercase

salam = "bro"
print("normal = " + salam)

salam = salam.upper()
print("upper = " + salam)

# Merubah semua ke lowercase
salam = "Selamat Pagi".lower()
print("lower = " + salam)

# pengecekan dengan isX method

# contoh untuk pengecekan lower case

salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + "is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + "is upper = " + str(apakah_upper))

# isapha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk huruf dan angka
# isdesimal() <-- angka saja
# isspace() <-- spasi, tab, newline in
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle() #hasil bool

print(judul + " is title = " + str(cek_judul))

# ngecek komponen startswith() endswith()<--keren
cek_start = "Sangjanim"
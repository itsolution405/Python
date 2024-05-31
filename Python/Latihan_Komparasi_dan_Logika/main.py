# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++++3-----10++++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10"))

# Operasi Komparasi
# +++++3----------
# memeriksa angka kurang dari 3
isKurangdari = (inputUser < 3)
print(isKurangdari)

# -----3++++++++10-----
# Kasus irisan

print("\n",10*"=","\n")
inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \ndan \nlebih besar dari 10"))

# -----3+++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ",isLebihDari)

# ++++++++++++10------
# kurang dari 10
isKurangdari = inputUser < 10
print("Kurang dari 10 = ",isKurangdari)

# Operasi Logika
# ++++++++++3---------10++++++++++
isCorrect = isKurangdari and isLebihDari
print("angka yang anda masukan: ", isCorrect)

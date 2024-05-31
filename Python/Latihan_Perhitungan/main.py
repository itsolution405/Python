# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu adalah",celcius,"celcius")

# reamur
# (4/5)C
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur,"Reamur")

# fahrenhiet
fahrenhiet = ((9/5) * celcius) + 32
print("suhu dalam fahrenhiet adalah",fahrenhiet,"Fahrenhiet")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin,"Kelvin")
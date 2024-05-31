# operasi aritmatika

a = 10
b = -3

# operasi tambah +
hasill = a + b
print(a,'+',b,'=',hasill)

# operasi pengurangan - 
hasill = a - b
print(a,'-',b,'=',hasill)

# operasi perkalian *
hasill = a * b
print(a,'*',b,'=',hasill)

# operasi pembagian /
hasill = a / b
print(a,'/',b,'=',hasill)

# operasi exponent (pangkat) **
hasill = a ** b
print(a,'**',b,'=',hasill)

# operasi modulus (sisa bagi) % 
hasill = a % b
print(a,'%',b,'=',hasill)

# operasi floar (devision) % 
hasill = a // b
print(a,'//',b,'=',hasill)

# prioritas operasi, opracional precedence

'''
    1. ()
    2. exponent **
    3. perkalian dan teman-teman * / ** % //
    4. penjumlahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasill = x ** y * (z + x) / y - y % z // x
print (x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x)

hasill = x + y * z
print(x,'+',y,'*',z,'=',hasill)

# kurung akan mengambil langkah paling pertama
hasill = (x + y) * z
print('(',x,'+',y,')*',z,'=',hasill)
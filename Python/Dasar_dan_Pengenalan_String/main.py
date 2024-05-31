# 1. cara membuat string

data = "ini adalah string"
print (data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakkan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Hallo, Apa Kabar?"')
print("'Hallo, Apa Kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda |

# membuat tanda ' menjadi string
print('ini hari jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("c:\\user\\ucup")

# tab
print("ucup\totong")
print("ucup\t\t\totong")

# backspace
print("Ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed - unix, macos, linux
print("baris pertama.\rbaris kedua.") #CR -> carriage return - comodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") #CRLF -> line feed carriage return - dipakai oleh windows

# 3. Stringg literal atau raw

# hati-hati
print('c:\new folder') # akan salah print nya

print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print("""
Nama : Ucup
Kelas : 3 SD\new normal
Website : www.ucup.com/newID
""")
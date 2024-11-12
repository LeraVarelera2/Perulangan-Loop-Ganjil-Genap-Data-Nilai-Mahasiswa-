# Header (Judul Program)
print("Program untuk menentukan bilangan ganjil")
# Meminta input bilangan
a = int(input("Masukkan bilangan awal: "))
b = int(input("Masukkan bilangan akhir: "))
# Membuat Sebuah Perulangan 
while a <= b:
    if a % 2:
        print(a)
    a += 1


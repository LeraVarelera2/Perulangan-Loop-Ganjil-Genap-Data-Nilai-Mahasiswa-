# Meminta input jumlah mahasiswa
Jumlah_Mahasiswa = int(input("Banyak Mahasiswa : "))
# Membuat Perulangan untuk setiap mahasiswa
for i in range(Jumlah_Mahasiswa):                             
    print("Mahasiswa ke "+ str(i+1))        
# Meminta Input Jumlah Mata Kuliah                  
    Jumlah_Matkul = int(input("Banyak Matakuliah yang diambil: ")) 
# Membuat Perulangan untuk setiap Jumlah Matkul
    total_nilai = 0                                          
    for i in range(Jumlah_Matkul): 
# Meminta input nilai matkul                           
        nilai=int(input(f"Input nilai Matkul ke {i+1}: "))   
# Menjumlah seluruh nilai dan Rata-rata setiap mahasiswa
        total_nilai += nilai                                  
    ratarata=total_nilai/Jumlah_Matkul
    print(f"Rata-rata: {ratarata}")
    print("--------------------------------------------\n")





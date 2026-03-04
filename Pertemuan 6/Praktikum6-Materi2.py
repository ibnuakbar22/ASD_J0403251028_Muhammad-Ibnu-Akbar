#===========================================
# Nama : Muhammad Ibnu Akbar
# NIM : J0403251028
# Kelas : TPLB2
# Insertion Sort (Ascending)
#===========================================

def insertion_sort(data):
    # Melihat data awal
    print("Data Awal : ", data)
    print("="*50)
    
    # Loop mulai dari elemen kedua (index array ke 1)
    for i in range(1, len(data)):
        key = data[i] # simpan nilai yang disisipkan
        j = i - 1     # index elemen terakhir dibagian sebelumnya
        
        # Loop untuk membandingkan key dengan elemen sebelumnya
        print("Iterasi ke-", i)
        print("Nilai Key = ", key)
        print("Bagian Kiri (terurut): ", data[:i])
        print("Bagian Kanan (belum terurut): ", data[i:])

        # Geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            
        # Sisipkan key ke posisi yang benar
        data[j + 1] = key

        print("Setelah disisipkan: ", data)
        print("="*50)
        
    return data

# Eksekusi Program
angka = [7, 8, 5, 2, 4, 6]
hasil = insertion_sort(angka)
print("Hasil Sorting : ", hasil)
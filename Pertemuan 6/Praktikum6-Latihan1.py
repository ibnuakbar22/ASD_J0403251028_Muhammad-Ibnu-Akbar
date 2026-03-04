#===========================================
# Nama : Muhammad Ibnu Akbar
# NIM : J0403251028
# Kelas : TPLB2
#Latihan 1 . Memahami Kode Program (Insertion Sort)
#===========================================
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

        data[j + 1] = key

    return data
#Soal:
#1. Mengapa perulangan dimulai dari indeks 1?
#2. Apa fungsi variabel key?
#3. Mengapa digunakan while, bukan for?
#4. Operasi apa yang terjadi di dalam while?

#Jawaban : 
#   1. Karena indeks 0 sudah dianggap sebagai bagian yang sudah terurut
#   2. Variabel key digunakan untuk menyimpan nilai yang akan disisipkan ke posisi yang benar dalam bagian yang sudah terurut
#   3. Digunakan while karena kita tidak tahu berapa banyak elemen yang harus digeser untuk menemukan posisi yang benar untuk key
#   4. Di dalam while, elemen yang lebih besar dari key digeser ke kanan untuk membuat ruang bagi key, dan j terus berkurang untuk memeriksa elemen sebelumnya hingga menemukan posisi yang benar untuk key atau mencapai awal array.
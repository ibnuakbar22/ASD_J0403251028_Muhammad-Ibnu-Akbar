#===========================================
# Nama : Muhammad Ibnu Akbar
# NIM : J0403251028
# Kelas : TPLB2
#Latihan 2 . Melengkapi Potongan Kode Program (Insertion Sort)
#===========================================
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # 1. Jawaban Kondisi Ascending: data[j] > key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        # 2. Jawaban pengisian baris kosong: data[j + 1] = key
        data[j + 1] = key

    return data

# --- Contoh Eksekusi ---
angka = [7, 8, 5, 2, 4, 6]
print("Hasil Ascending:", insertion_sort(angka))
#Soal:
#1. Lengkapi kondisi agar menjadi sorting ascending.
#2. Ubah agar menjadi descending.
#Jawaban :
#1. Untuk sorting ascending, kondisi dalam while haruslah `data[j] > key`
#2. Untuk sorting descending, kondisi dalam while haruslah `data[j] < key`

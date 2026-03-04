#===========================================
# Nama : Muhammad Ibnu Akbar
# NIM : J0403251028
# Kelas : TPLB2
#Tracing Insertion Sort
#===========================================
#Buat program dengan menggunakan algoritma insertion sort
#Tracing dengan data = [5, 2, 4, 6, 1, 3]
#Soal:
#1. Tuliskan isi list setelah iterasi i = 1.
#2. Tuliskan isi list setelah iterasi i = 3.
#3. Berapa kali pergeseran terjadi pada iterasi i = 4?

#jawaban :
def insertion_sort_tracing(data):
    print(f"Data Awal: {data}\n" + "="*30)
    
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        pergeseran = 0
        
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            pergeseran += 1
            
        data[j + 1] = key
        print(f"Iterasi i={i} (Key={key}): {data} | Pergeseran: {pergeseran}")

# Eksekusi
data = [5, 2, 4, 6, 1, 3]
insertion_sort_tracing(data)

#1 . Setelah iterasi i = 1, isi list adalah [2, 5, 4, 6, 1, 3]
#2 . Setelah iterasi i = 3, isi list adalah [2, 4, 5, 6, 1, 3]
#3 . Pada iterasi i = 4, terjadi 4 kali pergeseran (angka 6, 5, 4, dan 2 digeser ke kanan) sehingga isi list menjadi [1, 2, 4, 5, 6, 3]
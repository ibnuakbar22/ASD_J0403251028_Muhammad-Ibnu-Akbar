#===========================================
# Nama : Muhammad Ibnu Akbar
# NIM : J0403251028
# Kelas : TPLB2
#Latihan 4 . Memahami Kode Program (Merge Sort)
#===========================================

from heapq import merge


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)
        
#Soal:
#1. Apa yang dimaksud dengan base case?
#2. Mengapa fungsi memanggil dirinya sendiri?
#3. Apa tujuan fungsi merge()?

#jawaban :
#1. Base case adalah kondisi di mana fungsi rekursif berhenti memanggil dirinya sendiri, biasanya ketika data yang diproses sudah cukup kecil atau sederhana untuk diselesaikan langsung.
#2. Fungsi memanggil dirinya sendiri untuk memecah masalah menjadi bagian yang lebih kecil, sehingga setiap bagian dapat diselesaikan secara terpisah dan kemudian digabungkan kembali untuk mendapatkan hasil akhir.
#3. Tujuan fungsi merge() adalah untuk menggabungkan dua bagian yang sudah terurut (left_sorted dan right_sorted) menjadi satu list yang terurut secara keseluruhan.   
#==========================================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']   # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']   # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
#    Jawab: A->B = 4, B->D = 5 → total = 9
#
# 2. Berapa total bobot jalur A -> C -> D?
#    Jawab: A->C = 2, C->D = 1 → total = 3
#
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jawab: A -> C -> D dengan total bobot = 3
#
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari
#    jumlah edge yang paling sedikit?
#    Jawab: Karena setiap edge memiliki bobot (cost) yang berbeda.
#    Jalur dengan edge lebih banyak bisa saja memiliki total bobot
#    lebih kecil dibanding jalur dengan edge lebih sedikit.
#    Contoh: A->B->D (2 edge, bobot 9) vs A->C->D (2 edge, bobot 3).
#    Yang menentukan adalah total bobot, bukan jumlah edge.
# ==========================================================
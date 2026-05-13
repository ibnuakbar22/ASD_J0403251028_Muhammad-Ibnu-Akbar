# ========================================================== 
# Nama  : Muhammad Ibnu Akbar 
# NIM   : J0403251028
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree 
# ========================================================== 

# ========================================================== 
# Program Optimasi Jaringan Jalan Antar Kota (Algoritma Prim)
# ========================================================== 
import heapq

# 1. Representasi Weighted Graph menggunakan Adjacency List
# Data jarak antar kota sesuai soal
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bogor': 5, 'Depok': 3, 'Bandung': 6},
    'Depok': {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},
    'Bandung': {'Jakarta': 6, 'Depok': 4}
}

def prim_kota(graph, start_city):
    visited = set([start_city])
    edges = []
    
    # Memasukkan jalan yang terhubung dengan kota awal ke antrian prioritas
    for neighbor, weight in graph[start_city].items():
        heapq.heappush(edges, (weight, start_city, neighbor))
        
    mst_jalan = []
    total_jarak = 0
    
    while edges:
        # Ambil jalan dengan jarak terpendek yang tersedia
        weight, u, v = heapq.heappop(edges)
        
        # Jika kota tujuan belum terhubung ke jaringan MST
        if v not in visited:
            visited.add(v)
            mst_jalan.append((u, v, weight))
            total_jarak += weight
            
            # Tambahkan jalan dari kota yang baru terhubung ke antrian
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst_jalan, total_jarak

# Menjalankan program dimulai dari Bogor
hasil_mst, total_min = prim_kota(graph, 'Bogor')

# 3 & 4. Output MST dan Total Bobot
print("--- Rencana Pembangunan Jalan Minimum ---")
for asal, tujuan, jarak in hasil_mst:
    print(f"Hubungkan: {asal} - {tujuan} (Jarak: {jarak})")

print("-" * 40)
print(f"Total Jarak (Bobot Minimum) = {total_min} km")

# ========================================================== 
# Jawaban Analisis: 
# ========================================================== 
# 1. Kasus apa yang dipilih? 
#    Kasus 1: Jaringan Jalan Antar Kota.

# 2. Algoritma apa yang digunakan? 
#    Algoritma Prim.

# 3. Edge mana saja yang dipilih dalam MST? 
#    - Bogor ke Depok (Bobot 2)
#    - Depok ke Jakarta (Bobot 3)
#    - Depok ke Bandung (Bobot 4)

# 4. Berapa total bobot MST? 
#    9 (2 + 3 + 4).

# 5. Mengapa edge tertentu tidak dipilih? 
#    Edge seperti Bogor-Jakarta (5) dan Jakarta-Bandung (6) tidak dipilih 
#    karena semua kota sudah bisa terhubung melalui jalur Depok dengan 
#    biaya/jarak yang jauh lebih kecil. Jika jalan tersebut tetap dibangun, 
#    maka akan terjadi pemborosan anggaran karena terbentuk sirkuit (cycle) 
#    yang tidak diperlukan untuk konektivitas dasar.
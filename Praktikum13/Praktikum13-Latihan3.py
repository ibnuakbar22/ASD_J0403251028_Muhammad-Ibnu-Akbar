# ========================================================== 
# Nama  : Muhammad Ibnu Akbar 
# NIM   : J0403251028
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree 
# ========================================================== 

# ========================================================== 
# Latihan 3 : Implementasi Algoritma Prim
# ==========================================================

import heapq 

# Struktur Graph menggunakan Adjacency List (Dictionary dalam Dictionary)
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

def prim(graph, start): 
    visited = set([start]) 
    edges = [] 
    
    # Masukkan semua edge dari node awal ke dalam priority queue (heap)
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
    
    mst = [] 
    total_weight = 0 
    
    print(f"Memulai dari node: {start}")
    
    while edges: 
        # Ambil edge dengan bobot terkecil yang terhubung dengan pohon saat ini
        weight, u, v = heapq.heappop(edges) 
        
        if v not in visited: 
            visited.add(v) 
            mst.append((u, v, weight)) 
            total_weight += weight 
            print(f"Edge terpilih: {u} - {v} (Bobot: {weight})")
            
            # Tambahkan edge dari node yang baru dikunjungi ke heap
            for neighbor, w in graph[v].items(): 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
                    
    return mst, total_weight 

# Menjalankan fungsi Prim dimulai dari node 'A'
mst, total = prim(graph, 'A') 

print("\n--- Hasil Akhir ---")
print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 
print("Total bobot =", total) 

# ========================================================== 
# Jawaban Analisis: 
# ========================================================== 
# 1. Node awal apa yang digunakan? 
#    Node awal yang digunakan adalah 'A' (ditentukan pada pemanggilan prim(graph, 'A')).

# 2. Edge mana yang dipilih pertama kali? 
#    Edge ('A', 'C') dengan bobot 2. Karena dari node A, tetangga dengan bobot 
#    terkecil adalah C.

# 3. Bagaimana Prim menentukan edge berikutnya? 
#    Prim melihat seluruh edge yang terhubung dari "kumpulan node yang sudah 
#    dikunjungi" ke "node yang belum dikunjungi", lalu memilih yang bobotnya paling kecil.

# 4. Berapa total bobot MST yang dihasilkan? 
#    Total bobot adalah 6. 
#    Rinciannya: (A-C: 2) + (C-D: 1) + (D-B: 3) = 6.

# 5. Apa perbedaan pendekatan Prim dan Kruskal? 
#    - Prim: Membangun MST secara "tumbuh" dari satu node awal seperti pohon yang 
#      membesar. Ia selalu terhubung dalam satu komponen tunggal di setiap langkahnya.
#    - Kruskal: Membangun MST dengan cara mengurutkan semua edge di seluruh graph 
#      dan mengambil yang terkecil satu per satu selama tidak membentuk cycle. 
#      Kruskal bisa membentuk beberapa "hutan" (komponen terpisah) sebelum 
#      akhirnya menyatu.
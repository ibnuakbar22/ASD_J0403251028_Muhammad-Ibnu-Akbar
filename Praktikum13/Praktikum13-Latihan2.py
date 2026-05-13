# ========================================================== 
# Nama  : Muhammad Ibnu Akbar 
# NIM   : J0403251028
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree 
# ========================================================== 

# ========================================================== 
# Implementasi Sederhana Algoritma Kruskal 
# ========================================================== 

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 

# Mengurutkan edge berdasarkan bobot terkecil (Prinsip Greedy)
edges.sort() 

mst = [] 
total_weight = 0 
connected = set() 

print("Proses Seleksi Edge:")
for weight, u, v in edges: 
    # Logika sederhana: Memilih edge yang menghubungkan node baru
    # (Catatan: Dalam implementasi kompleks, digunakan Union-Find untuk cek cycle)
    if u not in connected or v not in connected: 
        mst.append((u, v, weight)) 
        total_weight += weight 
        connected.add(u) 
        connected.add(v) 
        print(f"Diterima: {u}-{v} (Bobot: {weight})")
    else:
        print(f"Ditolak: {u}-{v} (Bobot: {weight}) - Berisiko membentuk cycle")

print("\n--- Hasil Akhir ---")
print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 

print("Total bobot =", total_weight) 

# ========================================================== 
# Jawaban Analisis: 
# ========================================================== 
# 1. Edge mana yang dipilih pertama kali? 
#    Edge (C, D) dengan bobot 1. Karena algoritma Kruskal selalu memulai 
#    dari edge dengan bobot terkecil setelah data diurutkan.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
#    Karena Kruskal adalah algoritma "Greedy". Tujuannya adalah mencari 
#    total bobot minimum, sehingga mengambil nilai terkecil di setiap langkah 
#    adalah strategi yang paling optimal untuk meminimalkan hasil akhir.

# 3. Berapa total bobot MST yang dihasilkan? 
#    Total bobot adalah 6. Berasal dari edge: (C,D) bobot 1, (A,C) bobot 2, 
#    dan (B,D) bobot 3.

# 4. Mengapa edge tertentu (seperti (A,B) bobot 4 atau (A,D) bobot 5) tidak dipilih? 
#    Karena pada saat algoritma mencapai edge tersebut, semua titik (A, B, C, D) 
#    sudah terhubung (terkoneksi). Jika edge tersebut dipaksakan masuk, 
#    maka akan terbentuk "cycle" (sirkuit tertutup), yang melanggar aturan 
#    utama dari sebuah Spanning Tree.
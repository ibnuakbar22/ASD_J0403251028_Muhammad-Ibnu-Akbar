# ========================================================== 
# Nama  : Muhammad Ibnu Akbar 
# NIM   : J0403251028
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree 
# ========================================================== 

# ========================================================== 
# Latihan 1 :  Memahami Konsep Spanning Tree
# ==========================================================

# 1. Daftar edge pada graph berdasarkan gambar
edges = [ 
    ('A', 'B'), 
    ('A', 'C'), 
    ('A', 'D'), 
    ('C', 'D'), 
    ('B', 'D') 
] 

# 2. Contoh spanning tree yang valid
# Syarat: Semua vertex (A, B, C, D) terhubung tanpa membentuk cycle/sirkuit.
spanning_tree = [ 
    ('A', 'C'), 
    ('C', 'D'), 
    ('D', 'B') 
] 

# Menampilkan Daftar Edge Graph
print("Edge pada graph:") 
for edge in edges: 
    print(edge) 

# Menampilkan Contoh Spanning Tree
print("\nSpanning Tree:") 
for edge in spanning_tree: 
    print(edge) 

# 3 & 4. Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges)) 
print("Jumlah edge spanning tree =", len(spanning_tree)) 

# ==========================================
# Jawaban Analisis: 
# ==========================================
# 1. Apa perbedaan graph awal dan spanning tree? 
#    Graph awal adalah struktur keseluruhan yang mengandung semua koneksi (edge) 
#    yang mungkin, termasuk yang membentuk sirkuit/cycle. 
#    Sedangkan Spanning Tree adalah subgraph (bagian dari graph) yang 
#    menghubungkan semua titik (vertex) tanpa adanya sirkuit sama sekali.

# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
#    Karena secara definisi, "Tree" (pohon) adalah graph yang terhubung namun 
#    tidak memiliki sirkuit. Jika terdapat cycle, maka struktur tersebut 
#    bukan lagi sebuah pohon, melainkan kembali menjadi graph biasa yang 
#    memiliki redundansi jalur.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit? 
#    Karena spanning tree hanya mengambil jumlah edge minimum yang diperlukan 
#    untuk menghubungkan semua vertex. Jika sebuah graph memiliki 'n' vertex, 
#    maka spanning tree-nya akan selalu memiliki tepat 'n - 1' edge. 
#    Dalam kasus ini: 4 vertex (A,B,C,D) menghasilkan 3 edge pada spanning tree.
# ========================================================== 
# Nama  : Muhammad Ibnu Akbar 
# NIM   : J0403251028
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree 
# ========================================================== 

# ========================================================== 
# Program Optimasi Jaringan Kabel Kampus (Kruskal)
# ========================================================== 

# 1. Representasi Weighted Graph: (Biaya, Gedung 1, Gedung 2)
kabel_tersedia = [
    (4, 'Gedung A', 'Gedung B'),
    (2, 'Gedung A', 'Gedung C'),
    (3, 'Gedung B', 'Gedung D'),
    (1, 'Gedung C', 'Gedung D'),
    (5, 'Gedung A', 'Gedung D')
]

# Mengurutkan kabel berdasarkan biaya pemasangan termurah
kabel_tersedia.sort()

terhubung = set()
jaringan_minimal = []
total_biaya = 0

# 2. Implementasi Logika Kruskal
# Kita iterasi setiap kabel mulai dari yang termurah
for biaya, g1, g2 in kabel_tersedia:
    # Memeriksa apakah kabel akan menghubungkan gedung yang belum terhubung sepenuhnya
    # (Logika sederhana untuk mendeteksi perlunya jalur baru tanpa membuat sirkuit)
    if g1 not in terhubung or g2 not in terhubung:
        jaringan_minimal.append((g1, g2, biaya))
        total_biaya += biaya
        terhubung.add(g1)
        terhubung.add(g2)

# 3. Output Hasil
print("Rencana Pemasangan Kabel (MST):")
for g1, g2, biaya in jaringan_minimal:
    print(f"- {g1} ke {g2} dengan biaya: {biaya}")

print("-" * 30)
print(f"Total Biaya Minimum: {total_biaya}")

# ========================================================== 
# Jawaban Analisis: 
# ========================================================== 
# 1. Algoritma apa yang digunakan? 
#    Algoritma Kruskal. Algoritma ini bekerja dengan mengurutkan semua 
#    biaya dari terkecil ke terbesar dan mengambilnya selama tidak membentuk cycle.

# 2. Edge mana saja yang dipilih? 
#    - Gedung C ke Gedung D (Biaya 1)
#    - Gedung A ke Gedung C (Biaya 2)
#    - Gedung B ke Gedung D (Biaya 3)

# 3. Berapa total biaya minimum? 
#    Total biayanya adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini? 
#    Karena tujuan utamanya adalah menghubungkan seluruh titik (gedung) 
#    dengan total biaya paling rendah. MST menjamin semua gedung terhubung 
#    tanpa ada kabel yang mubazir (redundant/cycle), sehingga penggunaan sumber daya menjadi sangat efisien.
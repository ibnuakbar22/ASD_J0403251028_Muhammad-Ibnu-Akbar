#=================================================
# Nama : Muhammad Ibnu Akbar
# NIM  : J0403251028
# Kelas: B-P2
#=================================================
# Materi 1 : Implementasi Dasar Graph
#=================================================

#representasi graph menggunakan dictionary
graph = {
    'A' : ['B','C'],
    'B' : ['A','D'],
    'C' : ['A','D'],
    'D' : ['B','C']
}

#menampilkan struktur graph
for node in graph :
    print(node, '->', graph[node])

#penjelasan :
#Graph adalah struktur data yang digunakan untuk merepresentasikan hubungan antar objek.
#Graph terdiri dari simpul (node) dan sisi (edge) yang menghubungkan simpul-simpul tersebut.
#Dalam contoh di atas, kita menggunakan dictionary untuk merepresentasikan graph,
#dimana setiap kunci adalah sebuah node dan nilainya adalah daftar tetangga (neighbor) dari node tersebut.
#Contoh di atas merepresentasikan sebuah graph sederhana dengan 4 node (A, B, C, D) dan hubungan antar node yang ditunjukkan oleh daftar tetangga.
#Output dari kode di atas akan menampilkan struktur graph yang telah dibuat.
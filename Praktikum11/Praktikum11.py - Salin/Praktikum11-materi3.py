#=================================================
# Nama : Muhammad Ibnu Akbar
# NIM  : J0403251028
# Kelas: B-P2
#=================================================
# Materi 3 : Implementasi DFS
#=================================================

#sruktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

#representasi graph menggunakan dictionary
graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
}


def dfs(graph,node,visited):
    #fungsi untuk melakukan penelusuran graph dengan DFS
    # graph : dictionary yang menyimpan struktur dari graph
    #node : menyimpan node yang sedang dikunjungi
    #visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #lakukan DFS secara rekursif tentangga tersebut
            dfs(graph,neighbor,visited)

#set visited
visited = set()

#menjalankan DFS dari A
dfs(graph,"A",visited)

#penjelasan :
#DFS (Depth-First Search) adalah algoritma penelusuran graph yang mengunjungi node sedalam mungkin sebelum kembali dan melanjutkan ke node berikutnya.
#DFS menggunakan pendekatan rekursif atau menggunakan stack untuk menyimpan node yang akan dikunjungi berikutnya.
#Dalam contoh di atas, kita menggunakan pendekatan rekursif untuk melakukan DFS.
#Output dari kode di atas akan menampilkan urutan node yang dikunjungi selama penelusuran DFS dimulai dari node A.
#=================================================
# Nama : Muhammad Ibnu Akbar
# NIM  : J0403251028
# Kelas: B-P2
#=================================================
# Materi 2 : Implementasi BFS
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

def bfs(graph,start):
    #fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dictionary yang menyimoan struktur dari graph
    # start : node awal penelusuran

    # queue digunakan unutuk menyimpan node yang akan diproses/dibaca
    queue = deque()

    #variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
    visited = set()

    #masukan node awal ke queue
    queue.append(start)

    #ditandai node awal sebagai yang sudah dikunjungi
    visited.add(start)

    while queue:
        #mengambil node paling depan dari queue
        node = queue.popleft()

        #tampilkan node yang sedang dikunjungi
        print(node,end=" ")

        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga sebelum dikunjungi
            if neighbor not in visited:
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #masukan tetangga ke queue unutuk diproses nanti
                queue.append(neighbor)
        
#menjalankan BFS dari node A
bfs(graph,'A')

#penjelasan :
#BFS (Breadth-First Search) adalah algoritma penelusuran graph yang mengunjungi semua node pada level yang sama sebelum melanjutkan ke level berikutnya.
#Dalam implementasi di atas, kita menggunakan queue untuk menyimpan node yang akan diproses. Kita juga menggunakan set untuk menyimpan node yang sudah dikunjungi agar tidak terjadi pengulangan.
#Algoritma BFS dimulai dengan memasukkan node awal ke dalam queue dan menandainya sebagai sudah dikunjungi. Kemudian, selama queue tidak kosong, kita mengambil node paling depan dari queue, menampilkannya, dan memeriksa semua tetangganya.
#Jika tetangga belum dikunjungi, kita menandainya sebagai sudah dikunjungi dan memasukkannya ke dalam queue untuk diproses nanti.
#Output dari kode di atas akan menampilkan urutan node yang dikunjungi selama penelusuran BFS, dimulai dari node A.
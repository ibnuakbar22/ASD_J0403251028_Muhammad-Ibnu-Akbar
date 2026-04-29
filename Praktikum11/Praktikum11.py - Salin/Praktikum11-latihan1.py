#======================================================
# Nama : Muhammad Ibnu Akbar
# NIM  : J0403251028
# Kelas: B-P2
#======================================================
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
#======================================================

#representasi graph menggunakan dictionary
graph = { 
    'Rumah': ['Sekolah', 'Toko'], 
    'Sekolah': ['Perpustakaan'], 
    'Toko': ['Pasar'], 
    'Perpustakaan': [], 
    'Pasar': [] 
} 


from collections import deque #mengimpor deque dari library collections untuk digunakan sebagai struktur data antrian
def bfs(graph, start): 
    visited = set() #set untuk menyimpan node yang sudah dikunjungi
    queue = deque([start]) #antrian untuk menyimpan node yang akan dikunjungi selanjutnya

    visited.add(start)  #menandai node awal sebagai sudah dikunjungi

    while queue: 
        node = queue.popleft() #mengambil node paling depan dari antrian
        print(node, end=" ") #menampilkan node yang sedang dikunjungi

        for neighbor in graph[node]: 
            if neighbor not in visited: #jika tetangga belum dikunjungi
                visited.add(neighbor) #menandai tetangga sebagai sudah dikunjungi
                queue.append(neighbor) #menambahkan tetangga ke antrian untuk dikunjungi nanti
print("BFS dari Rumah:") 
bfs(graph, 'Rumah') 

#penjelasan :
#BFS (Breadth-First Search) adalah algoritma penelusuran graph yang mengunjungi semua node pada level yang sama sebelum melanjutkan ke level berikutnya.
#BFS menggunakan pendekatan antrian untuk menyimpan node yang akan dikunjungi berikutnya.
#Dalam contoh di atas, kita menggunakan BFS untuk mencari jalur terdekat dari node 'Rumah' ke node-node lainnya dalam graph.
#Output dari kode di atas akan menampilkan urutan node yang dikunjungi selama penelusuran BFS dimulai dari node 'Rumah'. 

#Pertanyaan Analisis 
#1. Node mana yang dikunjungi pertama?  
#Jawab : node yang dikunjungi pertama adalah node 'Rumah' karena node tersebut adalah node awal yang dimasukan ke dalam queue.
#2. Mengapa BFS cocok untuk mencari jalur terdekat? 
#Jawab : BFS cocok untuk mencari jalur terdekat karena BFS mengunjungi semua node pada level yang sama sebelum melanjutkan ke level berikutnya.
#Dengan demikian, ketika BFS menemukan node tujuan, kita dapat yakin bahwa jalur yang ditemukan adalah jalur terdekat dari node awal ke node tujuan. 
#3. Apa perbedaan urutan BFS jika struktur graph diubah?
#Jawab : berdasarkan struktur graph diatas, urutan BFS dari node 'Rumah' adalah : Rumah -> Sekolah -> Toko -> Perpustakaan -> Pasar.
#Jika struktur graph diubah, maka urutan BFS juga akan berubah sesuai dengan hubungan antar node yang baru.
# Misalnya, jika kita menambahkan node 'Kantor' yang terhubung ke 'Sekolah', maka urutan BFS dari node 'Rumah' akan menjadi : Rumah -> Sekolah -> Toko -> Kantor -> Perpustakaan -> Pasar.

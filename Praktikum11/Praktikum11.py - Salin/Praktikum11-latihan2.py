#======================================================
# Nama : Muhammad Ibnu Akbar
# NIM  : J0403251028
# Kelas: B-P2
#======================================================
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur)
#======================================================

#representasi graph menggunakan dictionary
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 

#fungsi untuk melakukan penelusuran graph dengan DFS
def dfs(graph, node, visited): 
    visited.add(node) #menandai node saat ini sebagai node yang sudah dikunjungi
    print(node, end=" ") #menampilkan node yang sedang dikunjungi

    for neighbor in graph[node]: #periksa semua tetangga dari node saat ini
        if neighbor not in visited: #jika tetangga belum pernah dikunjungi
            dfs(graph, neighbor, visited) #lakukan DFS secara rekursif tentangga tersebut

visited = set() #set untuk menyimpan node yang sudah dikunjungi

#menjalankan DFS dari node A
print("DFS dari A:") 
dfs(graph, 'A', visited)

#penjelasan :
#DFS (Depth-First Search) adalah algoritma penelusuran graph yang mengunjungi node sedalam mungkin sebelum kembali dan melanjutkan ke node berikutnya.
#DFS menggunakan pendekatan rekursif atau menggunakan stack untuk menyimpan node yang akan dikunjungi berikutnya.
#Dalam contoh di atas, kita menggunakan pendekatan rekursif untuk melakukan DFS.
#Output dari kode di atas akan menampilkan urutan node yang dikunjungi selama penelusuran DFS dimulai dari node A.

#Pertanyaan Analisis 
#1. Mengapa DFS masuk ke node terdalam terlebih dahulu? 
#Jawab : DFS masuk ke node terdalam terlebih dahulu karena algoritma ini dirancang untuk mengeksplorasi jalur sedalam mungkin sebelum kembali dan melanjutkan ke jalur berikutnya.
#DFS menggunakan pendekatan rekursif atau stack untuk menyimpan node yang akan dikunjungi berikutnya,
#sehingga ketika DFS menemukan node yang belum dikunjungi, ia akan langsung masuk ke node tersebut tanpa memeriksa node lain pada level yang sama terlebih dahulu.
#2. Apa yang terjadi jika urutan neighbor diubah?  
#Jawab : jika urutan neighbor diubah, maka urutan node yang dikunjungi selama penelusuran DFS juga akan berubah.
#Misalnya, jika kita mengubah urutan neighbor dari node A menjadi ['C', 'B'], maka urutan DFS dari node A akan menjadi : A -> C -> F -> B -> D -> E.
#3. Bandingkan hasil DFS dengan BFS pada graph yang sama. 
#Jawab : jika kita menjalankan BFS pada graph yang sama, maka urutan node yang dikunjungi akan berbeda dengan DFS.
#Urutan BFS dari node A adalah : A -> B -> C -> D -> E -> F, sedangkan urutan DFS dari node A adalah : A -> B -> D -> E -> C -> F.
#Perbedaan ini terjadi karena BFS mengunjungi semua node pada level yang sama sebelum melanjutkan ke level berikutnya,
#sedangkan DFS mengunjungi node sedalam mungkin sebelum kembali dan melanjutkan ke node berikutnya.

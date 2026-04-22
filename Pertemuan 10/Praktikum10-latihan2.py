# ==========================================================
# Nama        : Muhammad Ibnu Akbar
# NIM         : J0403251028
# Kelas       : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 4: Membuat BST yang Tidak Seimbang 
# ========================================================== 
 
#Class Node untuk menyimpan data BST 
class Node: 
    def __init__(self, data): 
        self.data = data      #Menyimpan datapada node 
        self.left = None      #Child kiri, menyimpan referensi ke anak kiri
        self.right = None     #Child kanan, menyimpan referensi ke anak kanan
 
 
#Fungsi insert untuk BST 
def insert(root, data): 
    #Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) 
 
    #Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) 
 
    #Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) 
 
    return root 
 
 
#Fungsi preorder untuk melihat bentuk tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
#Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R")

#========================================================== 
# Program utama 
#==========================================================
root = None 
#Data dimasukkan berurutan naik 
data_list = [10, 20, 30] 
for data in data_list: 
    root = insert(root, data) 
print("Preorder BST:") 
preorder(root) 

print("\n\nStruktur BST:") 
tampil_struktur(root) 

#Alur fungsi insert pada BST yang tidak seimbang
#Fungsi insert digunakan untuk menambahkan data baru ke dalam BST.
#Jika root kosong, buat node baru dengan data tersebut.
#Jika data yang akan dimasukkan lebih kecil dari data pada node saat ini, maka rekursif ke anak kiri.
#Jika data yang akan dimasukkan lebih besar dari data pada node saat ini, maka rekursif ke anak kanan.
#Dalam kasus ini, data dimasukkan secara berurutan naik (10, 20, 30), sehingga setiap data baru selalu lebih besar dari data sebelumnya, yang menyebabkan semua node baru dimasukkan ke subtree kanan.
#Akibatnya, struktur BST menjadi tidak seimbang, dengan semua node berada di sisi kanan, dan tidak ada node di sisi kiri.

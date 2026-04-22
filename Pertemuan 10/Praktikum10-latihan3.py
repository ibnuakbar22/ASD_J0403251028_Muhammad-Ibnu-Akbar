# ==========================================================
# Nama        : Muhammad Ibnu Akbar
# NIM         : J0403251028
# Kelas       : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
#Latihan 5: Rotasi Kiri pada BST Tidak Seimbang 
#=========================================================== 
 
#Class Node untuk menyimpan data BST
class Node: 
    def __init__(self, data): 
        self.data = data #Menyimpan data pada node
        self.left = None #Child kiri, menyimpan referensi ke anak kiri
        self.right = None #Child kanan, menyimpan referensi ke anak kanan
 
 
#Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    if root is not None: #Jika node tidak kosong
        print(root.data, end=" ") #Menampilkan data node
        preorder(root.left) #Rekursif ke anak kiri
        preorder(root.right) #Rekursif ke anak kanan
 
 
#Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R") 
 
 
#Fungsi rotasi kiri 
def rotate_left(x): 
    #x adalah root lama 
    y = x.right       #y adalah child kanan x 
    T2 = y.left       #subtree kiri milik y disimpan sementara 
 
    # Proses rotasi 
    y.left = x        #x menjadi child kiri dari y 
    x.right = T2      #child kanan x diganti dengan T2 
 
    #y menjadi root baru 
    return y

#==========================================================
# Program utama
#==========================================================

#Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
root = Node(10) #Membuat root dengan data 10
root.right = Node(20) #Menambahkan node dengan data 20 sebagai child kanan dari root
root.right.right = Node(30) #Menambahkan node dengan data 30 sebagai child kanan dari node 20

print("Preorder sebelum rotasi kiri:") 
preorder(root) #Menampilkan isi tree sebelum rotasi kiri

print("\n\nStruktur sebelum rotasi kiri:") 
tampil_struktur(root) #Menampilkan struktur tree sebelum rotasi kiri

# Melakukan rotasi kiri pada root 
root = rotate_left(root) 

print("\nPreorder sesudah rotasi kiri:") 
preorder(root) 

print("\n\nStruktur sesudah rotasi kiri:") 
tampil_struktur(root)

#Alur fungsi rotate_left pada BST yang tidak seimbang
#Fungsi rotate_left digunakan untuk melakukan rotasi kiri pada sebuah node x dalam BST yang tidak seimbang.
#Node x adalah root lama yang akan diputar ke kiri.
#Node y adalah child kanan dari x yang akan menjadi root baru setelah rotasi.
#Subtree T2 adalah subtree kiri milik y yang disimpan sementara selama proses rotasi
#Proses rotasi dilakukan dengan mengubah hubungan antara x, y, dan T2:
#y menjadi root baru dengan menjadikan x sebagai child kiri dari y.
#Child kanan x diganti dengan T2, sehingga T2 menjadi child kanan dari x.
#Setelah rotasi, y menjadi root baru dari subtree tersebut, dan struktur BST menjadi lebih seimbang.
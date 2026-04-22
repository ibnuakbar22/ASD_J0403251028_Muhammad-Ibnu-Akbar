# ==========================================================
# Nama        : Muhammad Ibnu Akbar
# NIM         : J0403251028
# Kelas       : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
#Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
#===========================================================

#Class Node untuk menyimpan data BST
class Node: 
    def __init__(self, data): 
        self.data = data      #Menyimpan data pada node
        self.left = None      #Child kiri
        self.right = None     #Child kanan


#Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    if root is not None:          #Jika node tidak kosong
        print(root.data, end=" ") #Tampilkan data
        preorder(root.left)       #Ke kiri
        preorder(root.right)      #Ke kanan


#Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R") 


#Fungsi rotasi kanan
def rotate_right(x):
    #x adalah root lama yang tidak seimbang
    y = x.left        #y adalah child kiri dari x (akan jadi root baru)
    T2 = y.right      #subtree kanan milik y disimpan sementara

    #Proses rotasi
    y.right = x       #x menjadi child kanan dari y
    x.left = T2       #child kiri x diganti dengan T2

    #Mengembalikan root baru
    return y


#==========================================================
#Program utama
#==========================================================

# Membuat tree tidak seimbang:
root = Node(30)              #Root awal 30
root.left = Node(20)         #20 menjadi child kiri 30
root.left.left = Node(10)    #10 menjadi child kiri 20

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Melakukan rotasi kanan pada root
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)

#Alur fungsi rotate_right pada BST yang tidak seimbang
#Fungsi rotate_right digunakan untuk melakukan rotasi kanan pada BST yang tidak seimbang.
#Node x adalah root lama yang tidak seimbang, dan node y adalah child kiri dari x yang akan menjadi root baru setelah rotasi.
#Subtree kanan milik y (T2) disimpan sementara karena akan dipindahkan ke child kiri x setelah rotasi.
#Proses rotasi dilakukan dengan menjadikan x sebagai child kanan dari y, dan T2 sebagai child kiri dari x.
#Setelah rotasi, y menjadi root baru dari subtree tersebut, dan fungsi mengembalikan y sebagai hasil rotasi.
#Rotasi kanan ini membantu mengembalikan keseimbangan pada BST yang sebelumnya tidak seimbang ke kiri.
#Dengan melakukan rotasi kanan pada node 30, node 20 menjadi root baru, dengan node 10 sebagai child kiri dan node 30 sebagai child kanan, sehingga struktur tree menjadi lebih seimbang.
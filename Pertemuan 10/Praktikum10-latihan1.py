# ==========================================================
# Nama        : Muhammad Ibnu Akbar
# NIM         : J0403251028
# Kelas       : TPL/B-P2
# Mata Kuliah : Algoritma & Struktur Data
# ==========================================================
# Latihan 1: BST
# ==========================================================

# Membuat class Node untuk merepresentasikan satu node pada BST
class node:
    def __init__(self, data):       
        self.data = data         #Menyimpan data pada node  
        self.left = None         #Child kiri, menyimpan referensi ke anak kiri 
        self.right = None        #Child kanan, menyimpan referensi ke anak kanan

#Fungsi insert untuk menambahkan data baru ke dalam BST
def insert(root, data):
    if root is None:        #Jika root kosong, buat node baru 
        return node(data)   #Membuat node baru 
    
    if data < root.data:    #Jika data yang akan dimasukkan lebih kecil, maka rekursif ke anak kiri
            root.left = insert(root.left, data) #Memanggil fungsi insert pada anak kiri
    elif data > root.data:  #Jika data yang akan dimasukkan lebih besar, maka rekursif ke anak kanan
            root.right = insert(root.right, data) #Memanggil fungsi insert pada anak kanan
   
    return root #Mengembalikan root setelah penambahan data baru

#Mengisi data BST
root = None 
data_list = [50,30,70,20,40,50,80]

#Memasukkan data ke BST
for data in data_list:
    root = insert(root, data) #Memanggil fungsi insert

print("BST berhasil dibuat")

#Alur fungsi insert pada BST 
#Fungsi insert digunakan untuk menambahkan data baru ke dalam BST.
#Jika root kosong, buat node baru dengan data tersebut.
#Jika data yang akan dimasukkan lebih kecil dari data pada node saat ini, maka rekursif ke anak kiri.
#Jika data yang akan dimasukkan lebih besar dari data pada node saat ini, maka rekursif ke anak kanan.  
#Jika data sudah ada (sama dengan data pada node saat ini), maka tidak perlu menambahkan data tersebut.
#Fungsi ini memastikan bahwa struktur BST tetap terjaga setelah penambahan data baru.

#==========================================================
#Latihan 2 : Traversal Inorder
#==========================================================

#Fungsi inorder traversal
def inorder(root):
     if root is not None: #Jika node tidak kosong
          inorder(root.left) #Rekursif ke anak kiri
          print(root.data, end=" ") #Menampilkan data node
          inorder(root.right) #Rekursif ke anak kanan

print("Hasil Traversal Inorder:")
inorder(root)

#Alur fungsi inorder traversal pada BST
#Fungsi inorder traversal digunakan untuk menampilkan data pada BST dalam urutan yang terurut (sorted order).
#Jika node tidak kosong, maka rekursif ke anak kiri terlebih dahulu untuk menampilkan data yang lebih kecil.
#Setelah itu, tampilkan data pada node saat ini.
#Kemudian rekursif ke anak kanan untuk menampilkan data yang lebih besar.
#Dengan cara ini, semua data pada BST akan ditampilkan dalam urutan yang terurut (ascending order).

#==========================================================
#Latihan 3 : Search di BST
#==========================================================

#Fungsi search untuk mencari data di BST
def search(root, key):
    if root is None: #Jika node koosng, data tidak ditemukan
         return False
    
    if root.data == key: #Jika data ditemukan
         return True
    elif key < root.data: #Jika key lebih kecil
          return search(root.left, key) #Rekursif ke anak kiri
    else:
          return search(root.right, key) #Rekursif ke anak kanan
    
#Uji pencarian
key = 100

if search(root, key):
    print("Data ditemukan di BST")
else:
    print("Data tidak ditemukan di BST")

#Alur fungsi search pada BST
#Fungsi search digunakan untuk mencari data tertentu di dalam BST.
#Jika node kosong, maka data tidak ditemukan.
#Jika data pada node saat ini sama dengan key yang dicari, maka data ditemukan.
#Jika key yang dicari lebih kecil dari data pada node saat ini, maka rekursif ke anak kiri untuk mencari di sana.
#Jika key yang dicari lebih besar dari data pada node saat ini, maka rekursif ke anak kanan untuk mencari di sana.
#Dengan cara ini, fungsi search dapat dengan efisien mencari data di dalam BST dengan memanfaatkan sifat terurut dari struktur data tersebut.
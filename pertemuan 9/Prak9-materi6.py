#=========================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPLB2
#=====================================================
# Praktikum-materi 6 = Struktur Organisasi Perusahaan
#=====================================================

#Class node adalah unit visual pada tree
class node:
    def __init__(self,data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi preorder : Root --> Left --> Right
def preorder(node):
    if node is not None:
       preorder(node.left)
       print(node.data, end=" ")
       preorder(node.right)

#membuat Tree Struktur Organisasi
root = node("Direktur")

#membuat child Level 1
root.left = node("Manajer A")
root.right = node("Manajer D")

#membuat child level 2
root.left.left = node("Staff1")
root.left.right = node("Staff2")

root.right.right = node("staff3")

#menjalankan transversal 
print("Struktur Organisasi (preorder):")
preorder(root)

#Penjelasan
# Pada kode di atas, kita membuat sebuah class bernama node yang memiliki atribut data, left, dan right.
# Fungsi preorder digunakan untuk melakukan traversal pada tree secara preorder, yaitu dengan mengunjungi root, child kiri, lalu child kanan.
# Kemudian, kita membuat sebuah instance dari class node dengan nilai "Direktur" dan menyimpannya dalam variabel root.
# Setelah itu, kita menambahkan child kiri dan kanan untuk node root dengan nilai "Manajer A" dan "Manajer B".
# Kemudian, kita menambahkan child kiri dan kanan untuk node "Manajer A" dengan nilai "Staff 1" dan "Staff 2", serta menambahkan child kanan untuk node "Manajer B" dengan nilai "Staff 3".
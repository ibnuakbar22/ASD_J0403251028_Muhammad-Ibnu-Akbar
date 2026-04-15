#=========================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPLB2
#=====================================================
# Praktikum-materi 5 = Membuat Traversel Postorder
#=====================================================

#Class node adalah unit visual pada tree
class node:
    def __init__(self,data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat Transversal Postorder Left --> Right --> Root
def postorder(node):
    if node is not None:
        postorder(node.left)
        print(node.data, end=" ")
        postorder(node.right)
        print(node.data, end=" ")
#membuat tree
#membuat sebuah node root
root = node("A")

#membuat child Level 1
root.left = node("B")
root.right = node("C")

#memmbuat child level 2
root.left.left = node("D")
root.left.right = node("E")

#menjalankan transversal
print("Hasil Transversal Postorder:")
postorder(root)

#Penjelasan
# Pada kode di atas, kita membuat sebuah class bernama node yang memiliki atribut data, left, dan right.
# Fungsi postorder digunakan untuk melakukan traversal pada tree secara postorder, yaitu dengan mengunjungi child kiri, child kanan, lalu root.
# Kemudian, kita membuat sebuah instance dari class node dengan nilai "A" dan menyimpannya dalam variabel root.
# Setelah itu, kita menambahkan child kiri dan kanan untuk node root dengan nilai "B" dan "C".
# Kemudian, kita menambahkan child kiri dan kanan untuk node "B" dengan nilai "D" dan "E".
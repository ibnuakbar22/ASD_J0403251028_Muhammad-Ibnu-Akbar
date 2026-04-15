#=========================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPLB2
#=====================================================
# Praktikum-materi 1 = Membuat Node
#=====================================================

#Class node digunakan untuk dasar  dari tree 

class node:
    def __init__(self,data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat sebuah node root
root = node("A")

#menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

#pembahasan :.........................................
# Pada kode di atas, kita membuat sebuah class bernama node yang memiliki atribut data, left, dan right.
# Atribut data digunakan untuk menyimpan nilai dari node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan kanan dari node tersebut.
# Kemudian, kita membuat sebuah instance dari class node dengan nilai "A" dan menyimpannya dalam variabel root.
# Setelah itu, kita menampilkan isi dari node root, child kiri, dan child kanan.
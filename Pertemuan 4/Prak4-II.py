# ================================================
# Muhammad Ibnu Akbar
# J0403251028
# Implementasi Dasar : Node pada Linked List
# ================================================

#Membuat class Node ( merupakan unit dasar dari linked list )
class node:
    def _init_(self, data): #Konstruktor
        self.data = data #Menyimpan nilai data
        self.next = None #Pointer ke node berikutnya (awal=none)

# 1) Membuat Node satu per satu
nodeA = node("A")
nodeB = node("B")
nodeC = node("C")

# 2) Menghubungkan Node : A -> B -> C None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : Menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data) # Menampilkan data pada node saat ini
    current = current.next # Pindah ke node berikutnya

#====================================================================
#Implementasi Dasar : Linked List + Insert Awal
#====================================================================

class Linkedlist: #Class implementasi Linked List

    def _init_(self):
        self.head = None #Awalnya kosong
    def insert_awal(self, data):
        # 1) Buat node baru
        nodeBaru = node(data) #Panggil class node

        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # 3) head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self):
        data_terhapus = self.head.data # Simpan data yang akan dihapus untuk ditampilkan
        # Menggeser head ke node berikutnya
        self.head = self.head.next 
        print("Node yang dihapus adalah :", data_terhapus)

    def tampilkan(self): #Implememntasi traversal
       current = self.head 
       while current is not None:
           print(current.data) # Menampilkan data pada node saat ini
           current = current.next # Pindah ke node berikutnya


print("===List Baru===")
ll = Linkedlist() #Instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
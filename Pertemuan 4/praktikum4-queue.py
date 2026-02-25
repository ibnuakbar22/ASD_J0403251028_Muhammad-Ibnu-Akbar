# ================================================
# Muhammad Ibnu Akbar
# J0403251028
# Implementasi Dasar : Node pada Linked List
# ================================================

class node: 
    def __init__(self, data):
        self.data = data 
        self.next = None 

class QueueLL:
    def __init__(self):
        self.front = None 
        self.rear = None 

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        nodeBaru = node(data) 
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    # Sekarang sejajar dengan enqueue
    def dequeue(self):
        if self.is_empty():
            print("Queue Kosong!")
            return None

        data_terhapus = self.front.data
        self.front = self.front.next

        # Jika setelah dihapus front jadi None, rear juga harus None
        if self.front is None:
            self.rear = None
            
        print(f"Node {data_terhapus} telah dihapus.")
        return data_terhapus

    # Sekarang sejajar dengan enqueue
    def tampilkan(self):
        current = self.front
        print("front", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next # Perbaikan koma ke titik
        print("None (rear di node terakhir)")

# === Uji Coba ===
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()
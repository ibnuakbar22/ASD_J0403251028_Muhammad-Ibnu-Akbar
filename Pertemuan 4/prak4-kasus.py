# ================================================
# Muhammad Ibnu Akbar
# J0403251028
# Kelas TPLB2
# ================================================ 

# ================================================
# Studi Kasus : Sistem Antrian Layanan Akademik
# Implementasi Queue =>
# Enqueue : Memindahkan pointer rear (nambah data baru di belakang)
# Dequeue : Memindahkan pointer front (hapus data di depan)
# Front -> A-> B > C -> Rear
# ================================================

#1) Mendefinisikan Node (Unit dasar dari linked list)
class node:
    def __init__(self, nim, nama): #Konstruktor
        self.nim   = nim   #Menyimpan NIM mahasiswa
        self.nama  = nama  #Menyimpan nama mahasiswa
        self.next  = None  #pointer ke node berikutnya (awal = None)
        
#Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear  = None

    def is_empty(self):
        #Ketika queue kosong, front = rear = None
        return self.front is None
    
    def enqueue(self, nim, nama):
        nodeBaru = node(nim, nama) #Buat node baru dengan data mahasiswa
        #Jika data baru masuk dari queue yang kosong, maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear  = nodeBaru
            return  
    
        self.rear.next = nodeBaru # rear selalu menunjuk ke node baru
        self.rear = nodeBaru # rear pindah ke node baru

#menghapus data di depan (memberikan layanan akademik)
    def dequeue(self):
        if self.is_empty():
            print("Antrian Kosong. Tidak ada yang bisa dilayani")
            return None

        #lihat data bagian front, simpan di variabel data yang akan dilayani
        node_dilayani = self.front # Simpan data yang akan dilayani untuk ditampilkan

        #geser front ke node berikutnya
        self.front = self.front.next

        #Jika front menjadi None (data antrian terakhir yang dilayani), maka front = rear = None
        if self.front is None:
            self.rear = None

        return node_dilayani 

    def tampilkan(self):



        print("Daftar Antrian Mahasiswa (Front -> Rear):")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

#Program utama

def main(): 

    #instantiasi queue
    q = queueAkademik()

    while True:
        print("==== Sistem Antrian Akademik ====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == '1':
            nim = input("Masukkan NIM Mahasiswa: ").strip()
            nama = input("Masukkan Nama Mahasiswa: ").strip()

            q.enqueue(nim, nama)
            print("Mahasiswa Berhasil Ditambahkan ke Antrian")

        elif pilihan == '2':
            dilayani = q.dequeue()
            print(f"Mahasiswa yang dilayani: {dilayani.nim} - {dilayani.nama}")

        elif pilihan == '3':
            q.tampilkan()

        elif pilihan == '4':
            print("Program Selesai. Terima kasih telah menggunakan sistem antrian akademik!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-4.")

#penanda untuk menjalankan file utama
if __name__ == "__main__":
    main()

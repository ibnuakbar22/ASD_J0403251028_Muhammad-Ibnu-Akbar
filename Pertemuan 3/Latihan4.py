class Simpul:
    def __init__(self, data):
        self.info = data
        self.next = None

class RantaiData:
    def __init__(self):
        self.titik_awal = None

    # Fungsi untuk menambah data di akhir (untuk persiapan tes)
    def tambah(self, data_baru):
        baru = Simpul(data_baru)
        if self.titik_awal is None:
            self.titik_awal = baru
        else:
            pelacak = self.titik_awal
            while pelacak.next:
                pelacak = pelacak.next
            pelacak.next = baru

    # --- JAWABAN SOAL NO 4 ---
    def gabungkan_dengan(self, rantai_lain):
        # 1. Jika rantai kita sendiri kosong, langsung ambil rantai lain
        if self.titik_awal is None:
            self.titik_awal = rantai_lain.titik_awal
            return

        # 2. Jika rantai yang mau digabung kosong, tidak perlu lanjut
        if rantai_lain.titik_awal is None:
            return

        # 3. Cari node paling ujung di rantai pertama
        pelacak = self.titik_awal
        while pelacak.next:
            pelacak = pelacak.next
        
        # 4. Sambungkan 'next' node terakhir ke awal rantai kedua
        pelacak.next = rantai_lain.titik_awal
        print("Penggabungan berhasil dilakukan!")

    def tampilkan(self):
        pelacak = self.titik_awal
        print("Isi Rantai:", end=" ")
        while pelacak:
            print(f"{pelacak.info} ->", end=" ")
            pelacak = pelacak.next
        print("None")

# --- Demonstrasi Program ---
if __name__ == "__main__":
    # Membuat Rantai Pertama
    L1 = RantaiData()
    L1.tambah(1)
    L1.tambah(2)
    L1.tambah(3)
    
    # Membuat Rantai Kedua
    L2 = RantaiData()
    L2.tambah(4)
    L2.tambah(5)
    
    print("Sebelum digabung:")
    L1.tampilkan()
    L2.tampilkan()
    
    # Proses Penggabungan
    L1.gabungkan_dengan(L2)
    
    print("\nSetelah digabung (L1 + L2):")
    L1.tampilkan()
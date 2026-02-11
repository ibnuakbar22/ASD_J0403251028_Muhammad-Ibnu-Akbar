class NodeData: # Menggunakan NodeData sebagai ganti Node
    def __init__(self, val):
        self.isi = val
        self.next = None

class LingkaranData: # Nama kelas unik
    def __init__(self):
        self.awal = None # Menggunakan 'awal' sebagai ganti 'head'

    def input_baru(self, angka):
        baru = NodeData(angka)
        if self.awal is None:
            self.awal = baru
            baru.next = self.awal
        else:
            bantu = self.awal
            while bantu.next != self.awal:
                bantu = bantu.next
            bantu.next = baru
            baru.next = self.awal

    def cek_data(self, target):
        # Proteksi jika list masih kosong
        if not self.awal:
            print("List masih kosong, isi dulu ya!")
            return

        skrg = self.awal
        ketemu = False
        
        # Menggunakan logika: cek dulu, baru geser (loop manual)
        # Ini beda dengan kode modul yang pakai while True
        while True:
            if skrg.isi == target:
                ketemu = True
                break
            skrg = skrg.next
            if skrg == self.awal: # Berhenti kalau sudah balik ke awal
                break
        
        if ketemu:
            print(f"Sip! {target} ada di dalam list.")
        else:
            print(f"Yah, {target} nggak ketemu di list ini.")

# --- Bagian Main (Berbeda dari sebelumnya) ---
if __name__ == "__main__":
    my_list = LingkaranData()
    
    print("--- Program Cari Data (Circular) ---")
    raw_input = input("Masukkan angka (pisahkan spasi): ")
    
    if raw_input.strip():
        kumpulan_angka = [int(x) for x in raw_input.split()]
        for n in kumpulan_angka:
            my_list.input_baru(n)
            
    try:
        cari = int(input("Cari angka berapa? "))
        my_list.cek_data(cari)
    except:
        print("Input salah, harus angka!")
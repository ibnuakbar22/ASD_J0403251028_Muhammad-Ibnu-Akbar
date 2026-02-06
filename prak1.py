#konsep ADT dan file Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#=============================================
#membuka file dengan mode read ("r")
with open("data mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)


print("===Hasil Read===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("Jumlah baris", isi_file.count("\n")+1)

#membuka file per baris
print("===membaca file per baris===")
jumlah_baris = 0
with open("data mahasiswa.txt", "r", encoding= "utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris +1
        baris = baris
        print("baris ke-", jumlah_baris)
        print("isinya :", baris)

#Latihan dasar 2 : parsing barid menjadi kolom data

with open("data mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM :", nim, "| Nama :", "| Nilai :", nilai)

#Latihan dasar 3 : Membaca file dan menyimpan ke list

data_list = []  #List untuk menampung data mahasiswa
with open("data mahasiswa.txt", "r", encoding= "utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #simpan sbg list "[nim, nama, nilai]"
        data_list.append([nim,nama,int(nilai)])

print("=== Data Mahasiswa dalam LIST===")
print(data_list)

print("=== Jumlah Record dalam LIST===")
print("Jumlah Record", len(data_list))

print("===Menampilkan data Record Tertentu===")
print("Contoh Record pertama: ", data_list[0])

#Latihan dasar 4 : Membaca file dan menyimpan ke Dictionary

data_dict = {}
with open("data mahasiswa.txt", "r", encoding= "utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan data ke dictionary dengan key NIM
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("===Data Mahasiswa dalam Dictionary===")
print(data_dict)
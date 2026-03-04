#===========================================
#Nama : Muhammad Ibnu Akbar
#NIM : J0403251028
#Kelas : TPLB2
#Insertion Sort (Ascending)
#===========================================

def insertion_sort(data):
    #Loop mulai dari elemen kedua (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir dibagian sebelumnya
        #Loop untuk membandingkan key dengan elemen sebelumnya
        
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j + 1] = key
        return data
    
angka = [7,8,5,2,4,6]
print("Hasil Sorting : ", insertion_sort(angka))

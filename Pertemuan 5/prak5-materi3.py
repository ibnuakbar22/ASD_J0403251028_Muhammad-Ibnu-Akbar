# ================================================
# Muhammad Ibnu Akbar
# J0403251028
# Kelas TPLB2
# ================================================ 

# ================================================
#Materi Rekursif : Menjumlahkan ELement List
# ================================================

def jumlah_list(data, index=0):
    #base case
    if index == len(data): # Ketika index mencapai panjang list, berhenti
        return 0
    
    #rekursif case
    return data[index] + jumlah_list(data, index+1) #rekursif case
print("=== Program Jumlah List ===")
print(jumlah_list([2,4,5]))
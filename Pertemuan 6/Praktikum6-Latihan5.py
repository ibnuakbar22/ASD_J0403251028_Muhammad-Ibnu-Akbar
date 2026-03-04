#===========================================
# Nama : Muhammad Ibnu Akbar
# NIM : J0403251028
# Kelas : TPLB2
#Latihan 5 . Melengkapi Fungsi Merge
#===========================================
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if ...:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

#Soal:
#1. Lengkapi kondisi agar menjadi ascending.
#2. Jelaskan fungsi result.extend().

#Jawaban:
def merge(left, right):
    """
    Jawaban Latihan 5:
    1) Ascending: gunakan kondisi left[i] <= right[j]
        (<= membuat hasil stable saat nilai sama).
    2) result.extend(...) menambahkan sisa elemen yang sudah terurut sekaligus,
        setelah salah satu list habis.
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:     # kondisi ascending
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])         # tambahkan sisa left (kalau ada)
    result.extend(right[j:])        # tambahkan sisa right (kalau ada)
    return result
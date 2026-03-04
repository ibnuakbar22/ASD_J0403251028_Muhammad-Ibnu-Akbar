#===========================================
# Nama : Muhammad Ibnu Akbar
# NIM : J0403251028
# Kelas : TPLB2
# Merge Sort (Ascending)
#===========================================

def merge_sort(data, depth=0):
    indent = "  " * depth
    print(f"{indent}merge_sort({data})")

    # BASE CASE: Jika data cuma 1 elemen, kembalikan datanya langsung
    if len(data) <= 1:
        return data

    # Membagi data menjadi dua bagian
    mid = len(data) // 2 
    Left = data[:mid]
    Right = data[mid:]
    
    print(f"{indent}divide -> left = {Left} | right = {Right}")

    # Rekursif: Pastikan hasil ditampung
    left_sorted = merge_sort(Left, depth + 1) 
    right_sorted = merge_sort(Right, depth + 1)

    # Proses menggabungkan
    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")

    return merged

def merge(left, right):
    result = []
    i = 0
    j = 0

    # Membandingkan elemen dari kedua bagian
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Eksekusi Program
angka = [13, 7, 28, 5, 19, 36, 4]
print("-" * 50)
hasil = merge_sort(angka)
print("-" * 50)
print("Hasil Sorting : ", hasil)
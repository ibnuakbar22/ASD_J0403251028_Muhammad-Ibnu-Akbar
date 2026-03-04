#===========================================
# Nama : Muhammad Ibnu Akbar
# NIM : J0403251028
# Kelas : TPLB2
# Merge Sort (Ascending)
#===========================================

def merge_sort(data):
    if len(data) > 1:
        return data 
         # Membagi data menjadi dua bagian
        mid = len(data) // 2 
        Left = data[:mid]    # slicing untuk bagian kiri 
        Right = data[mid:]      #slicing untuk bagian kanan
  
  #recursive call
        left_sorterd = merge_sort(Left) 
        right_sorted = merge_sort(Right)

        return merge(left_sorterd, right_sorted)

def merge(left,right):
    
    result = []
    i = 0
    j = 0

    #membandingkan elemen dari kedua bagian dan menambahkan yang lebih kecil ke hasil
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Eksekusi Program
angka = [13,7,28,5,19,36,4]
print("Hasil Sorting : ", merge_sort(angka))

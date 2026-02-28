# ================================================
# Muhammad Ibnu Akbar
# J0403251028
# Kelas TPLB2
# ================================================ 

# ================================================
#Materi Rekursif : Call Stack
# racing bilangan (masuk-keluar)
# input 3
# masuk 1-2-3 
# keluar 
# ================================================

def hitung(n):
    #base case
    if n == 0: 
        print("Selesai!")
        return
    
    print(f"Masuk {n}")
    hitung(n-1) # Rekursif case
    print("Keluar", n) # Base case

print("=== Program Tracing ===")
hitung(3)
# ================================================
# Muhammad Ibnu Akbar
# J0403251028
# Kelas TPLB2
# ================================================ 

# ================================================
#Materi Rekursif : Faktorial
# recursif case => 3! = 3 * 2 * 1
# base case => 0 berhenti 
# ================================================

def faktorial(n):
    #base case
    if n == 0: 
        return 1
    return n * faktorial(n-1) #n-1*n-2*n-3*... n-?
print("=== Program Faktorial ===")
print ("Hasil Faktorial : ", faktorial(3))



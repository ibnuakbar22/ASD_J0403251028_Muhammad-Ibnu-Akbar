#==========================================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path 
#==========================================================


def bellman_ford(graph, start):

    # Inisialisasi semua jarak dengan tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # ── FASE RELAKSASI ──────────────────────────────────────────
    # Ulangi relaksasi sebanyak (V - 1) kali, di mana V = jumlah node.
    # Ini menjamin semua jalur terpendek ditemukan pada graf tanpa
    # negative cycle, karena jalur terpendek maksimal memiliki (V-1) edge.
    for _ in range(len(graph) - 1):

        # Iterasi setiap node dalam graf
        for node in graph:

            # Lewati node yang belum bisa dijangkau dari node awal
            if distances[node] == float('inf'):
                continue

            # Periksa semua tetangga dari node saat ini
            for neighbor, weight in graph[node].items():

                # Hitung jarak baru menuju tetangga melalui node saat ini
                new_distance = distances[node] + weight

                # Jika ditemukan jarak lebih kecil, perbarui jarak tetangga
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    # ── DETEKSI NEGATIVE CYCLE ──────────────────────────────────
    # Lakukan satu iterasi relaksasi tambahan (iterasi ke-V).
    # Jika masih ada jarak yang bisa diperbarui, berarti terdapat
    # negative cycle — kondisi di mana jarak bisa terus mengecil tanpa batas.
    for node in graph:
        if distances[node] == float('inf'):
            continue

        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                print("⚠️  Peringatan: Negative cycle terdeteksi!")
                return None  # Graf mengandung siklus berbobot negatif

    return distances


# ── CONTOH PENGGUNAAN ───────────────────────────────────────────
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Jalankan algoritma Bellman-Ford mulai dari node 'A'
hasil = bellman_ford(graph, 'A')

# Tampilkan hasil jarak terpendek dari 'A' ke semua node
if hasil:
    print(hasil)

#==========================================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================
import heapq

# Representasi graph berbobot antar kota menggunakan dictionary
# Bobot merepresentasikan jarak (dalam satuan tertentu, misal km)
graph = {
    'Bogor':   {'Jakarta': 5, 'Depok': 2},
    'Depok':   {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Mencari jarak terpendek dari node start ke semua node lain.

    Args:
        graph : dict - Graf berbobot (adjacency dictionary)
        start : str  - Node awal pencarian

    Returns:
        distances : dict - Jarak minimum ke setiap node
    """
    # Inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue: (jarak, node) — selalu proses jarak terkecil dulu
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil saat ini
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika node ini sudah diproses dengan jarak optimal
        if current_distance > distances[current_node]:
            continue

        # Periksa semua kota tetangga dari kota saat ini
        for neighbor, weight in graph[current_node].items():

            # Hitung total jarak menuju tetangga melalui node saat ini
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil, perbarui dan masukkan ke antrian
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Tentukan node awal: Bogor
start_node = 'Bogor'

# Jalankan algoritma Dijkstra
hasil = dijkstra(graph, start_node)

# Tampilkan jarak terpendek dari Bogor ke semua kota
print(f"Jarak terpendek dari {start_node}:")
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")

# ==========================================================
# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
#    Jawab: Bogor
#
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Jawab: Depok = 2 (jalur langsung Bogor -> Depok)
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Jawab: Bandung = 8 melalui Bogor -> Depok -> Bandung (2+6=8),
#    lebih pendek dari Bogor -> Jakarta -> Bandung (5+7=12)
#
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini.
#    Jawab:
#    - Mulai dari Bogor dengan jarak 0, semua kota lain = inf
#    - Proses Bogor: update Depok=2, Jakarta=5
#    - Proses Depok (terkecil=2): update Jakarta=min(5, 2+2)=4, Bandung=2+6=8
#    - Proses Jakarta (terkecil=4): cek Bandung=min(8, 4+7)=8 (tidak berubah)
#    - Proses Bandung (terkecil=8): tidak ada tetangga
#    - Hasil akhir: Bogor=0, Depok=2, Jakarta=4, Bandung=8
# ========================================================== 
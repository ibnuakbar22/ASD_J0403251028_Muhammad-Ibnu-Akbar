#==========================================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path 
#  ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================
import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati (node sudah diproses optimal)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
#    Jawab: 4 (langsung A -> B)
#
# 2. Berapa jarak terpendek dari A ke C?
#    Jawab: 2 (langsung A -> C)
#
# 3. Berapa jarak terpendek dari A ke D?
#    Jawab: 3 (melalui A -> C -> D = 2 + 1)
#
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Jawab: Jalur A->C->D = 2+1 = 3, sedangkan A->B->D = 4+5 = 9.
#    Meskipun harus melewati node tambahan (C), total bobotnya jauh
#    lebih kecil karena bobot tiap edge-nya lebih ringan.
#
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Jawab: Priority queue memastikan node dengan jarak terkecil
#    selalu diproses terlebih dahulu (greedy). Ini menjamin bahwa
#    saat sebuah node dikeluarkan dari antrian, jaraknya sudah optimal.
#
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Jawab: Dijkstra mengasumsikan bahwa setelah sebuah node diproses,
#    jaraknya sudah final (tidak bisa lebih kecil lagi). Bobot negatif
#    bisa membuat jalur yang sebelumnya diabaikan menjadi lebih pendek,
#    sehingga asumsi ini menjadi salah dan hasil tidak akurat.
# ==========================================================
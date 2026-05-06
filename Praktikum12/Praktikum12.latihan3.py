#==========================================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
#    Jawab: 5 (A -> B secara langsung)
#
# 2. Berapa total bobot jalur A -> C -> B?
#    Jawab: A->C = 4, C->B = -2 → total = 2
#
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jawab: A -> C -> B dengan total bobot = 2, lebih kecil dari
#    jalur langsung A -> B = 5.
#
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Jawab: Karena Bellman-Ford tidak langsung "mengunci" jarak suatu node.
#    Ia melakukan relaksasi berulang (V-1 kali) sehingga pembaruan jarak
#    bisa terjadi kapan saja, termasuk saat menemukan edge berbobot negatif.
#
# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Jawab: Relaksasi adalah proses memeriksa apakah jarak menuju suatu node
#    bisa dipersingkat melalui node lain. Jika distances[node] + weight
#    < distances[neighbor], maka distances[neighbor] diperbarui.
#
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Jawab:
#    - Dijkstra lebih cepat O((V+E) log V), tapi hanya untuk bobot positif.
#    - Bellman-Ford lebih lambat O(V×E), tapi bisa menangani bobot negatif
#      dan mendeteksi negative cycle.
# ==========================================================
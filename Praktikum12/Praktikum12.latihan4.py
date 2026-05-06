#==========================================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================


import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang':       {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan':  {'Lab': 3},
    'Kantin':        {'Lab': 4, 'Aula': 7},
    'Lab':           {'Aula': 1},
    'Aula':          {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# ==========================================================
# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Jawab: Kantin = 2 menit (jalur langsung Gerbang -> Kantin)
#
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jawab: 7 menit melalui Gerbang -> Kantin -> Lab -> Aula
#           (2 + 4 + 1 = 7), lebih cepat dari Gerbang -> Kantin -> Aula (9)
#           maupun Gerbang -> Perpustakaan -> Lab -> Aula (10)
#
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Jawab: Tidak selalu. Contohnya Gerbang ke Aula tidak ada jalur langsung,
#    dan jalur melalui Kantin+Lab (7 menit) lebih cepat dari
#    Kantin langsung ke Aula (2+7 = 9 menit). Jalur tidak langsung bisa
#    lebih efisien jika bobot edge perantaranya kecil.
#
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Jawab: Karena semua bobot (waktu tempuh) bernilai positif.
#    Dijkstra efisien untuk kasus seperti ini karena selalu memproses
#    lokasi terdekat lebih dulu, menjamin hasil optimal dengan cepat.
# ==========================================================
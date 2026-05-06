#==========================================================
# Nama  : Muhammad Ibnu Akbar
# NIM   : J0403251028
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path 
#==========================================================


import heapq 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
}   
def dijkstra(graph, start):
    # Menyimpan jarak minimum     
    distances = {node: float('inf') for node in graph}
    
    # Jarak node awal = 0     
    distances[start] = 0      
    # Priority queue     
    pq = [(0, start)]      
    while pq:         
        current_distance, current_node = heapq.heappop(pq)        # Ambil node dengan jarak terkecil dari priority queue  
        
        # Periksa semua tetangga         
        for neighbor, weight in graph[current_node].items(): # Hitung total jarak menuju tetangga melalui node saat ini             
            
            distance = current_distance + weight
            # Jika ditemukan jarak lebih kecil             
            if distance < distances [neighbor]:          
            
                distances[neighbor] = distance

                heapq.heappush(pq, (distance, neighbor))      # Masukkan tetangga ke priority queue dengan jarak yang diperbarui
    return distances  
hasil = dijkstra(graph, 'A')  # Jalankan algoritma Dijkstra mulai dari node 'A'
print(hasil) # Tampilkan jarak terpendek dari 'A' ke semua node
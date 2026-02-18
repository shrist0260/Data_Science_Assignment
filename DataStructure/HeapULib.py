#Heap using library 
import heapq
heap = []
heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
print("Min Heap:", heap)
print("Extract Min:", heapq.heappop(heap))
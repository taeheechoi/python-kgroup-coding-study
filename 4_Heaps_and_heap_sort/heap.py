import heapq

# heappush
heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
print(heap) # [10, 50, 30]

# heapify
heap2 = [9, 5, 3]
heapq.heapify(heap2)
print(heap2) # [3, 5, 9]

# heappop
r = heapq.heappop(heap)
print(r) # 10
print(heap) # [30, 50]

r2 = heap[0]
print(r2) # 30
print(heap) # [30, 50]

# max heap: x -> tuple (-x, x) 왜냐하면 heapq 최소 힙으로 구현
heap_items = [1,3,5,7,9]
max_heap = []
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))
print(max_heap) # [(-9, 9), (-7, 7), (-3, 3), (-1, 1), (-5, 5)]
max_item = heapq.heappop(max_heap)[1]
print(max_item) # 9





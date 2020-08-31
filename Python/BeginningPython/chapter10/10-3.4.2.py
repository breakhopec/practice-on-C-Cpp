from heapq import *

heap = [6, 5, 4, 3, 2, 1]
heapify(heap)
print(heap)
print(heappop(heap))
print(nlargest(3, range(10)), nsmallest(3, range(90, 100)))
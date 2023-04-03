import sys
import heapq

input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x),x))
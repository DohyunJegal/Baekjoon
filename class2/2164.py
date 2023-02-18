import sys
# list.pop(0), list.index, list.insert, list.count, x in list, list[:-1] 등 O(N)
# list를 큐 또는 덱으로 사용하면 안됨. 반드시 collections.deque를 사용할 것!
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque(i for i in range(1, n+1))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(queue[0])

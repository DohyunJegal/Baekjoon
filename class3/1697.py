import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()
        if v == k:
            return arr[v]
        for i in (v-1, v+1, v*2):
            if 0 <= i < limit and arr[i] == 0:
                arr[i] = arr[v] + 1
                queue.append(i)

limit = 100001
arr = [0] * limit
n, k = map(int, input().split())
print(bfs(n))
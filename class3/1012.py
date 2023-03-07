import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < m:
            if graph[tx][ty] == 1:
                graph[tx][ty] = 0
                dfs(tx, ty)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = deque([0] * m for _ in range(n))
    count = 0
    for _ in range(k):
        s, e = map(int, input().split())
        graph[e][s] = 1
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                dfs(a, b)
                count += 1
    print(count)
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
queue = deque([])
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
res = 0

def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()

        for a in range(4):
            tx = x + dx[a]
            ty = y + dy[a]

            if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] == 0:
                graph[tx][ty] = graph[x][y] + 1
                queue.append((tx, ty))

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    res = max(res, max(i))

print(res-1)
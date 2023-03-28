import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = []
queue = deque([])
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append((i, j, k))
    graph.append(tmp)
res = 0

def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dz = [1, -1]

    while queue:
        z, x, y = queue.popleft()

        for a in range(4):
            tx = x + dx[a]
            ty = y + dy[a]

            if 0 <= tx < n and 0 <= ty < m and graph[z][tx][ty] == 0:
                graph[z][tx][ty] = graph[z][x][y] + 1
                queue.append((z, tx, ty))
        for b in range(2):
            tz = z + dz[b]

            if 0<= tz < h and graph[tz][x][y] == 0:
                graph[tz][x][y] = graph[z][x][y] + 1
                queue.append((tz, x, ty))

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        res = max(res, max(j))
print(res-1)
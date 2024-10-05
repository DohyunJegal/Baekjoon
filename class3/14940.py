import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
res = [[0]*m for _ in range(n)]

def bfs(i, j):
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque([(i, j)])
    visited[i][j] = 1
    res[i][j] = 0
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                res[nx][ny] = res[x][y] + 1
                visited[nx][ny] = 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and res[i][j] == 0:
            print(-1, end=' ')
        else:
            print(res[i][j], end=' ')
    print()
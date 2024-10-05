import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(a, b):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited[a][b] = 1
    q = deque([(a, b)])
    res = 0
    while q:
        x, y = q.popleft()
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and campus[nx][ny] != 'X':
                if campus[nx][ny] == 'P':
                    res += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
    return res

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            r = bfs(i, j)
            print(r if r!=0 else 'TT')
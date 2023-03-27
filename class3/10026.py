import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
pic = []
for _ in range(n):
    pic.append(list(input()))
visited = deque([0] * n for _ in range(n))
cnt = 0
cntRG = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    curr_color = pic[x][y]
    visited[x][y] = 1

    for a in range(4):
        tx = x + dx[a]
        ty = y + dy[a]

        if 0 <= tx < n and 0 <= ty < n:
            if visited[tx][ty] == 0 and pic[tx][ty] == curr_color:
                dfs(tx, ty)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

for i in range(n):
    for j in range(n):
        if pic[i][j] == 'G':
            pic[i][j] = 'R'

visited = deque([0] * n for _ in range(n))

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cntRG += 1

print(cnt, cntRG)

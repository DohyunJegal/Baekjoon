import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    global count
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    if 0 <= x < n and 0 <= y < n:
        if lst[x][y] == 1:
            lst[x][y] = 0
            count += 1
            for a in range(4):
                tx = x + dx[a]
                ty = y + dy[a]
                dfs(tx, ty)

n = int(input())
lst = [list(map(int, input().rstrip())) for _ in range(n)]
res = []
count = 0

for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            dfs(i, j)
            res.append(count)
            count = 0

res.sort()
print(len(res))
for k in res:
    print(k)
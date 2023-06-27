import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
d = [[0]*(m+1) for _ in range(n+1)]
for a in range(1, n + 1):
    for b in range(1, m + 1):
        d[a][b] = lst[a-1][b-1] + d[a-1][b] + d[a][b-1] - d[a-1][b-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(d[x][y] - d[x][j-1] - d[i-1][y] + d[i-1][j-1])

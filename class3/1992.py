import sys
input = sys.stdin.readline

n = int(input())
video = [list(map(int, input().rstrip())) for _ in range(n)]
res = []

def divide(x, y, z):
    number = video[x][y]
    for i in range(x, x+z):
        for j in range(y, y+z):
            if video[i][j] != number:
                res.append('(')
                divide(x, y, z//2)
                divide(x, y+z//2, z//2)
                divide(x+z//2, y, z//2)
                divide(x+z//2, y+z//2, z//2)
                res.append(')')
                return
    if number == 1:
        res.append(1)
    else:
        res.append(0)

divide(0, 0, n)
for k in res:
    print(k, end='')
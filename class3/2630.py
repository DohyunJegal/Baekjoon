import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
res = []

def divide(x, y, z):
    color = paper[x][y]
    for i in range(x, x+z):
        for j in range(y, y+z):
            if paper[i][j] != color:
                divide(x, y, z//2)
                divide(x, y+z//2, z//2)
                divide(x+z//2, y, z//2)
                divide(x+z//2, y+z//2, z//2)
                return
    if color == 1:
        res.append(1)
    else:
        res.append(0)

divide(0, 0, n)
print(res.count(0))
print(res.count(1))
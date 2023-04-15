import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
res = []

def divide(x, y, z):
    number = paper[x][y]
    for i in range(x, x+z):
        for j in range(y, y+z):
            if paper[i][j] != number:
                divide(x, y, z//3)
                divide(x, y+z//3, z//3)
                divide(x, y+2*(z//3), z//3)
                divide(x+z//3, y, z // 3)
                divide(x+z//3, y + z // 3, z // 3)
                divide(x+z//3, y + 2 * (z // 3), z // 3)
                divide(x+2*(z//3), y, z // 3)
                divide(x+2*(z//3), y + z // 3, z // 3)
                divide(x+2*(z//3), y + 2 * (z // 3), z // 3)
                return
    if number == 1:
        res.append(1)
    elif number == 0:
        res.append(0)
    else:
        res.append(-1)

divide(0, 0, n)
print(res.count(-1))
print(res.count(0))
print(res.count(1))
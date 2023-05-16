import sys
input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        # 처음
        if j == 0:
            tri[i][j] += tri[i-1][j]
        # 마지막
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        # 중간
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[n-1]))
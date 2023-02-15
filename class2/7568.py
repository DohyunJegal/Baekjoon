import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())    # x = weight, y = height
    lst.append([x, y, 1])

for i in range(n):
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            lst[i][2] += 1

for k in range(n):
    print(lst[k][2], end=' ')
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
d1, d2 = [1]*n, [1]*n

for i in range(1, n):
    if lst[i] <= lst[i-1]:
        d1[i] = max(d1[i], d1[i-1]+1)
    if lst[i] >= lst[i-1]:
        d2[i] = max(d2[1], d2[i-1]+1)

print(max(max(d1), max(d2)))
import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))

m, c = 0, 0
for i in range(n):
    if m < lst[i]*(n-i):
        m = lst[i]*(n-i)
        c = lst[i]

print(m, c)
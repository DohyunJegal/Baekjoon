import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
d = [0]*n
m = lst[0]

for i in range(1, n):
    m = min(m, lst[i])
    d[i] = max(d[i-1], lst[i]-m)

print(*d)
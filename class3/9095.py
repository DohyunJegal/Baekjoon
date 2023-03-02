import sys
input = sys.stdin.readline

r = int(input())
for _ in range(r):
    n = int(input())
    d = list(i for i in range(n+1))
    d[0] = 1
    for j in range(3, n+1):
        d[j] = d[j-1] + d[j-2] + d[j-3]
    print(d[-1])
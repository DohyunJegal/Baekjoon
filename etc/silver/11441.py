import sys
input = sys.stdin.readline

n = int(input())
d = [0]*(n+1)
lst = list(map(int, input().split()))
for i in range(1, n+1):
    d[i] = d[i-1] + lst[i-1]
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(d[b]-d[a-1])

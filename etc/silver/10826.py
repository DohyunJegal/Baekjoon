import sys
input = sys.stdin.readline

d = [0, 1]
n = int(input())
for i in range(2, n+1):
    d.append(d[i-2]+d[i-1])

print(d[n])

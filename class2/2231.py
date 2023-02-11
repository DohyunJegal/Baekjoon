import sys
input = sys.stdin.readline

n = int(input())
res = 0

for i in range(1, n):
    s = sum([int(j) for j in str(i)])
    if i + s == n:
        res = i
        break

print(0 if res == 0 else res)
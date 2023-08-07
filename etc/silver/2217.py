import sys
input = sys.stdin.readline

n = int(input())
k = []
for i in range(n):
    k.append(int(input()))
k.sort(reverse=True)

res = 0
for i in range(len(k)):
    res = max(k[i]*(i+1), res)
print(res)
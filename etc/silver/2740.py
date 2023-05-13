import sys
input = sys.stdin.readline

A = []
n, m = map(int, input().split())
for _ in range(n):
    A.append(list(map(int, input().split())))
B = []
m, k = map(int, input().split())
for _ in range(m):
    B.append(list(map(int, input().split())))
res = []
for _ in range(n):
    res.append([0]*k)

# n*m 행렬, m*k 행렬 곱셈 > n*k행렬
for x in range(n):
    for y in range(k):
        for z in range(m):
            res[x][y] += A[x][z] * B[z][y]

for a in res:
    for b in a:
        print(b, end=' ')
    print()
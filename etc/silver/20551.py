import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = sorted([int(input()) for _ in range(n)])
B = {}
for i in range(n):
    if A[i] not in B:
        B[A[i]] = i

for _ in range(m):
    D = int(input())
    print(B[D] if D in B else -1)
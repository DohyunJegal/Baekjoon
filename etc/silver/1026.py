import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

res = 0
for i in range(n):
    res += A[i]*B[i]
print(res)

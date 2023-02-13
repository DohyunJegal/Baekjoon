import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if M >= lst[i] + lst[j] + lst[k] > res:
                res = lst[i] + lst[j] + lst[k]
print(res)